from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QListWidget,
    QFileDialog,
    QMainWindow,
    QSlider,
    QLabel,
)
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl, Qt, QSize
from PyQt5.QtGui import QIcon


class Widgets(QWidget):
    """this class will handle layouts and placing of the widgets"""

    def __init__(self):
        super().__init__()
        # make layout settings here
        self.main = QWidget()
        self.horiz_layout = QHBoxLayout()
        self.horiz_layout2 = QHBoxLayout()
        self.vertc_layout = QVBoxLayout()
        self.main.setLayout(self.vertc_layout)

        # make widgets here
        # make an instance of song player
        self.playlist = QListWidget()
        self.playlist.setStyleSheet("font-size:18px;")

        # self.playlist.itemDoubleClicked.connect(self.play_selected_song)

        self.play_btn = QPushButton()
        self.play_btn.setIcon(QIcon("./assets/play.png"))
        self.play_btn.setIconSize(QSize(25, 25))

        self.pause_btn = QPushButton()
        self.pause_btn.setIcon(QIcon("./assets/pause2.png"))
        self.pause_btn.setIconSize(QSize(20, 20))
        self.back_btn = QPushButton()
        self.back_btn.setIcon(QIcon("./assets/back.png"))
        self.back_btn.setIconSize(QSize(20, 20))
        self.next_btn = QPushButton()
        self.next_btn.setIcon(QIcon("./assets/next.png"))
        self.next_btn.setIconSize(QSize(20, 20))

        # song progress
        self.song_progress = QSlider(Qt.Horizontal)
        # style the song progress
        self.song_progress.setStyleSheet(
            """
                  QSlider::handle:horizontal {
                       background: transparent;

                  }
              """
        )
        # song progress time
        self.start_time = QLabel("00:00")
        self.end_time = QLabel("00:00")

        # song volume control
        self.song_volume = QSlider(Qt.Horizontal)
        self.song_volume.setMinimumWidth(200)
        self.song_volume.setMaximumWidth(200)
        self.song_volume.setMinimum(0)
        self.song_volume.setValue(50)
        self.song_volume.setMaximum(100)

        # song volume labels
        self.vol_up = QLabel("+")
        self.vol_up.setStyleSheet("font-size:20;")
        self.vol_down = QLabel("-")
        self.vol_down.setStyleSheet("font-size:20px;")

        # ADDING THE WIDGETS TO THE LAYOUT

        self.vertc_layout.addWidget(self.playlist)

        self.horiz_layout2.addWidget(self.start_time)
        self.horiz_layout2.addWidget(self.song_progress)
        self.horiz_layout2.addWidget(self.end_time)
        self.vertc_layout.addLayout(self.horiz_layout2)

        self.horiz_layout.addWidget(self.play_btn)
        self.horiz_layout.addStretch()
        self.horiz_layout.addWidget(self.back_btn)
        self.horiz_layout.addWidget(self.pause_btn)
        self.horiz_layout.addWidget(self.next_btn)
        self.horiz_layout.addStretch()
        # add volume up and down hints
        self.horiz_layout.addWidget(self.vol_down)
        self.horiz_layout.addWidget(self.song_volume)
        self.horiz_layout.addWidget(self.vol_up)

        self.vertc_layout.addLayout(self.horiz_layout)


class SongPlayer:
    def __init__(self, parent: QMainWindow, base_widget: QWidget):
        self.parent = parent
        self.base_widget = base_widget
        # make a media player
        self.player = QMediaPlayer()
        self.player.setVolume(50)

        # song player signals
        # self.player.durationChanged.connect(self.update_song_progress)

        # song file paths
        self.file_paths = []

        # current song index
        self.currentIndex = 0

        # signal for auto advancing in the playlist
        self.player.mediaStatusChanged.connect(self.handle_media_status)

    def open_media(self, index=0):
        # this method should load in as many files as the user chose
        selected_songs, _ = QFileDialog.getOpenFileNames(
            self.parent, "sedelect songs", "", "songs (*.mp3)"
        )

        self.file_paths.extend(selected_songs)

        for path in self.file_paths:
            self.base_widget.playlist.addItem(path.split("/")[-1])

    def configure_sound(self, Index=0):
        self.currentIndex = Index
        # make and configure the sound player

        if self.file_paths:
            self.song_url = QUrl.fromLocalFile(self.file_paths[self.currentIndex])
            # add all the songs selected to the playlist
            self.song_content = QMediaContent(self.song_url)
            self.player.setMedia(self.song_content)

        else:
            pass

    def next_song(self):
        if self.currentIndex < len(self.file_paths) - 1:
            self.currentIndex += 1
            self.configure_sound(self.currentIndex)
            self.player.play()

        if self.currentIndex > len(self.file_paths) - 1:
            self.currentIndex = 0
            self.configure_sound(self.currentIndex)
            self.player.play()

    def previous_song(self):
        if self.currentIndex > 0:
            self.currentIndex -= 1
            self.configure_sound(self.currentIndex)
            self.player.play()

    def handle_media_status(self, status):
        if status == QMediaPlayer.EndOfMedia:
            self.currentIndex += 1
            if self.currentIndex < len(self.file_paths):
                self.configure_sound(self.currentIndex)
                self.player.play()
