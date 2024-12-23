import sys
from time import sleep

from PySide6.QtWidgets import QApplication, QMainWindow
from pybass3.playlist import Playlist
from pybass3 import Song

from lamov_music import Ui_MainWindow
from player import Json


class Gui(QMainWindow):
    def __init__(self):
        super(Gui, self).__init__()
        self.ui = Ui_MainWindow()
        self.playlist = Playlist()
        self.ui.setupUi(self)
        self.json = Json()
        self.view_songs()
        self.connect()
        self.json_flag = False
        self.song = Song(self.json.get_json_song())
        self.playlist.add_directory(self.json.music, recurse=True)

    def connect(self):
        self.ui.new_json.clicked.connect(self.update_json)
        self.ui.previous.clicked.connect(self.previous)
        self.ui.play.clicked.connect(self.play)
        self.ui.stop.clicked.connect(self.stop)
        self.ui.next.clicked.connect(self.next)
        self.ui.json_queue.clicked.connect(self.play_json)
        self.ui.normal_queue.clicked.connect(self.play_normal)

    def stop(self):
        self.playlist.stop()
        self.song.stop()

    def play(self):
        self.stop()
        if self.json_flag:
            self.song.play()
        else:
            self.playlist.play()

    def previous(self):
        if not self.json_flag:
            self.playlist.previous()

    def next(self):
        if not self.json_flag:
            self.playlist.next()

    def view_songs(self):
        self.ui.listwidget.clear()
        self.ui.listwidget.addItems(self.json.get_json())

    def update_json(self):
        self.json.set_json()
        self.view_songs()
        print(
            self.playlist.current.file_path.name,
            self.playlist.current.position_time,
            self.playlist.current.duration_time
        )

    def play_normal(self):
        self.json_flag = False
        self.stop()
        self.playlist.play()

    def play_json(self):
        self.json_flag = True
        self.stop()
        self.song = Song(self.json.get_json_song())
        self.song.play()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Gui()
    window.show()
    sys.exit(app.exec())