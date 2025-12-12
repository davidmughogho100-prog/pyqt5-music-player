"""
this is a music player module using pyqt5
planning on no external libraries for easy compilation using pyinstaller

"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon

from utils.menu_builder import ConfigureMenuBar
from utils.widgets import Widgets, SongPlayer


class MusicPlayer(QMainWindow):
    """this is the main class it will focus on the application logic
    it will handle signals comming from the widgets class
    """

    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 500, 500)
        self.setWindowTitle("Jsound")
        self.setWindowIcon(QIcon("./assets/vlc.png"))
        # instantiate the menu class
        self.menu = self.menuBar()
        self.file = self.menu.addMenu("file")

        self.open_ = self.file.addAction("open")
        self.open_.setIcon(QIcon("./assets/open1.png"))
        self.open_.setShortcut("Ctrl+O")
        self.open_.triggered.connect(self.load_songs)
        self.close = self.file.addAction("Quit")
        self.close.setIcon(QIcon("./assets/quit.png"))
        self.close.setShortcut("Ctrl+Q")
        self.menu_config = ConfigureMenuBar(self)
        self.menu_config.help_.setIcon(QIcon("./assets/info.png"))
        # self.open.triggered.connect(self.open_meadia)

        # instatiate the widgets class
        self.widget = Widgets()
        self.play = SongPlayer(self, self.widget)

        self.play.player.durationChanged.connect(self.update_slider_range)
        self.play.player.positionChanged.connect(self.update_slider_pos)

        # activate the widgets from the widgets class
        self.widget.play_btn.clicked.connect(self.play_song)
        self.widget.pause_btn.clicked.connect(self.pause_song)
        self.widget.next_btn.clicked.connect(self.play_next_song)
        self.widget.back_btn.clicked.connect(self.play_previous_song)

        self.widget.song_progress.sliderMoved.connect(self.seek_song)
        self.widget.song_volume.valueChanged.connect(self.change_volume)

        self.widget.playlist.itemDoubleClicked.connect(self.play_choice)
        self.setCentralWidget(self.widget.main)

    def load_songs(self):
        self.play.open_media()
        self.play.player.play()

    def play_song(self):
        self.play.configure_sound()
        self.play.player.play()

        # testing button animation

    def pause_song(self):
        self.play.player.pause()
        if self.play.player.state() == 2:
            self.widget.pause_btn.setIcon(QIcon("./assets/play2.png"))

    def play_next_song(self):
        self.play.next_song()

    def play_previous_song(self):
        self.play.previous_song()

    def play_choice(self, item):
        song_index = self.widget.playlist.row(item)
        self.play.configure_sound(song_index)
        # self.play.open_media(song_index)
        self.play.player.play()

    def seek_song(self, pos):
        # self.position = self.widget.song_progress.value()
        self.play.player.setPosition(pos)

    def change_volume(self):
        self.volume = self.widget.song_volume.value()
        self.play.player.setVolume(self.volume)

    def update_slider_range(self, duration):
        self.widget.song_progress.setMinimum(0)
        self.widget.end_time.setText(self.time_converter(duration))
        self.widget.song_progress.setMaximum(duration)

        # also display the seconds and minutes passed
        # self.seconds = duration // 1000
        # self.widget.start_time.setText(str(self.seconds))

    def update_slider_pos(self, position):
        if not self.widget.song_progress.isSliderDown():
            self.widget.song_progress.setValue(position)

    def time_converter(self, miliseconds):
        self.total_seconds = miliseconds // 1000
        self.minutes = self.total_seconds // 60
        self.seconds = self.total_seconds % 60

        return f"{self.minutes}:{self.seconds}"


def main():
    app = QApplication(sys.argv)
    window = MusicPlayer()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
