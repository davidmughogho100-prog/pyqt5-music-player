import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QTextEdit, QVBoxLayout
from PyQt5.QtGui import QIcon


class ConfigureMenuBar:
    """this class contains the code for the
    top menu of the music player
    """

    def __init__(self, parent: QMainWindow):
        super().__init__()
        self.parent = parent
        self.helop = self.parent.menu.addMenu("help")
        self.help_ = self.helop.addAction("jsound manual")

        self.configure_menubar()
        # menus

    def configure_menubar(self):
        self.help_.setShortcut("F1")
        self.help_.triggered.connect(self.explain_jsound)
        self.about = self.parent.menu.addMenu("about")
        self.author = self.about.addAction("about jsound")
        self.author.triggered.connect(self.about_Jsound)

        self.parent.close.triggered.connect(self.exit)

    def exit(self):
        sys.exit()

    def explain_jsound(self):
        self.about_win = QWidget()
        self.about_win.setWindowTitle("help")
        self.about_win.setGeometry(500, 0, 800, 600)
        self.about_win.setFixedSize(800, 600)
        self.about_win.show()
        self.about_layout = QVBoxLayout()
        self.info = QTextEdit()
        self.info.setReadOnly(True)
        self.info.setHtml(
            """
                            <html>
                                <head>
                                    <style>
                                            .head{
                                                text-align:center;
                                                color:royalblue;
                                            }
                                            #contact{
                                                text-align:center;
                                            }
                                            #bdy{
                                                font-size:23px;
                                            }
                                    </style>
                                </head>
                                <body id = "bdy">
                                    <h1 class = 'head'>Jsound Usage</h1>
                                    <p>
                                        Jsound is a an easy to use cross platform music player.
                                        To use it:
                                        <ul>
                                            <li>
                                                --> click on open select the song or songs you
                                                    want then click the big play button.
                                                    also clicking the song on the playlist menu
                                                    does the same thing

                                            </li>

                                            <li>
                                                --> press the previous next and pause icon to
                                                    interact to advance songs or pause them
                                            </li>

                                        shortcut keybord keys:
                                            <li>
                                                --> use Ctrl + Q to quit Jsound
                                            </li>
                                            
                                            <li>
                                                --> use Ctrl + O to open songs in your device
                                            </li>

                                            <li>
                                                --> use F1 key to open the this help manual
                                            </li>
                                        </ul>
                                    <p>
        
                                    <p>
                                        The J in <b>Jsound</b> stands for jesus who
                                        goes before me every where i go.
                                    </p>
        
                                    <p id="contact">
                                        Contact me:
                                        <b class = 'head'>davidmughogho@gmail.com<b>
                                    </p
                                </body>
                            <html>
                """
        )
        self.about_layout.addWidget(self.info)
        self.about_win.setLayout(self.about_layout)

    def about_Jsound(self):
        self.about_win = QWidget()
        self.about_win.setWindowTitle("about")
        self.about_win.setGeometry(500, 0, 500, 400)
        self.about_win.setFixedSize(500, 400)
        self.about_win.show()
        self.about_layout = QVBoxLayout()
        self.info = QTextEdit()
        self.info.setReadOnly(True)
        self.info.setHtml(
            """
                    <html>
                        <head>
                            <style>
                                    .head{
                                        text-align:center;
                                        color:royalblue;
                                    }
                                    #contact{
                                        text-align:center;
                                    }

                                    #bdy{
                                        font-size:23px;
                                    }
                            </style>
                        </head>
                        <body id = "bdy">
                            <h1 class = 'head'>About Jsound</h1>
                            <p>
                                Jsound is a cross platform music player written
                                in <b>python</b>. The app uses the builtin <b>sys</b>
                                module of python and <b>pyqt5</b> only.
                            <p>

                            <p>
                                The J in <b>Jsound</b> stands for jesus who
                                goes before me every where i go.
                            </p>

                            <p id="contact">
                                Contact me:
                                <b class = 'head'>davidmughogho@gmail.com<b>
                            </p>
                        </body>
                    <html>
        """
        )
        self.about_layout.addWidget(self.info)
        self.about_win.setLayout(self.about_layout)
