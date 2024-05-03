import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from pytube import YouTube

class YouTubeDownloader(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("YouTube Video Downloader")
        self.setGeometry(100, 100, 400, 200)

        # URL label and input
        self.url_label = QLabel("Enter YouTube Video URL:", self)
        self.url_label.move(20, 20)
        self.url_entry = QLineEdit(self)
        self.url_entry.setGeometry(180, 20, 200, 20)

        # Output path label and input
        self.path_label = QLabel("Enter Output Directory Path:", self)
        self.path_label.move(20, 60)
        self.path_entry = QLineEdit(self)
        self.path_entry.setGeometry(180, 60, 200, 20)

        # Download button
        self.download_button = QPushButton("Download Video", self)
        self.download_button.setGeometry(150, 100, 120, 30)
        self.download_button.clicked.connect(self.download_video)

    def download_video(self):
        video_url = self.url_entry.text()
        output_path = self.path_entry.text()
        
        try:
            # Create a YouTube object
            yt = YouTube(video_url)

            # Get the highest resolution stream
            stream = yt.streams.get_highest_resolution()

            # Download the video
            stream.download(output_path)

            QMessageBox.information(self, "Success", "Video downloaded successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to download video: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = YouTubeDownloader()
    window.show()
    sys.exit(app.exec_())
