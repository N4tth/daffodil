import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel,QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from dwPl import downloadYT

class DaffodilApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DAFFODIL MP3")
        self.setGeometry(100,100,600,400)

        layout = QVBoxLayout()

        title = QLabel("DAFFODIL")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(title)

        self.urlInput = QLineEdit()
        self.urlInput.setPlaceholderText("URL here")
        layout.addWidget(self.urlInput)

        downloadButton = QPushButton("Download")
        downloadButton.clicked.connect(self.startDownload)
        layout.addWidget(downloadButton)

        self.messages = QTextEdit()
        self.messages.setReadOnly(True)
        layout.addWidget(self.messages)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def updateMss(self,text):
        self.messages.append(text)
    def startDownload(self):
        url = self.urlInput.text()
        if url:
            try:
                self.updateMss(f"Jelo jelo iniciating...")
                downloadYT(url)
                self.updateMss("Done!")
            except Exception as e:
                self.updateMss(f"Error: {e}")
        else:
            self.updateMss("Invalid url")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DaffodilApp()
    window.show()
    sys.exit(app.exec_())


