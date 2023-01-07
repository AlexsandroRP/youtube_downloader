from PySide2.QtWidgets import *
from ui_main import Ui_MainWindow
import sys
from pytube import YouTube, Playlist
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Youtube Downloader")

        self.btn_download.clicked.connect(self.youtube_download)
        self.btn_open.clicked.connect(self.open_file)
        self.btn_convert.clicked.connect(self.cut_video)

    def youtube_download(self):
        video_url = self.txt_link.text()
        if self.rb_video.isChecked():
            # pegar qualidade melhor do vide
            try:
                YouTube(video_url).streams.filter(res='720p').first().download()
            except:
                YouTube(video_url).streams.filter(res='480p').first().download()


            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText('Vídeo baixado com sucesso!')
            msg.exec_()

        elif self.rb_audio.isChecked():
            YouTube(video_url).streams.filter(only_audio=True).first().download()    

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText('Áudio baixado com sucesso!')
            msg.exec_()

        elif self.rb_playlist.isChecked():
            playlist = Playlist(video_url)
            for video in playlist.videos:
                try:
                    video.streams.filter(res='720p').first().download()
                except:
                    video.streams.filter(res='480p').first().download()    

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText('Playlist baixada com sucesso!')
            msg.exec_()     

    def open_file(self):
        self.file = QFileDialog.getOpenFileName(self, "Selecione o vídeo desejado:")
        self.txt_file.setText(str(self.file[0]))

    def cut_video(self):
        ffmpeg_extract_subclip(self.txt_file.text(),
                                int(self.txt_segundo_inicial.text()), 
                                int(self.txt_segundo_final.text()), targetname="video_cortado.mp4")

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText('Vídeo cortado com sucesso!')
        msg.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

