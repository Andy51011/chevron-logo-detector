from PyQt6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QFileDialog


class DetectorUi(QWidget):
    def __init__(self):
        super().__init__()
        self.verticalLayout = None
        self.setWindowTitle("Chevron Logo Filter")
        self.setGeometry(300, 300, 500, 200)
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self.userPath = None
        self.startBtn = QPushButton("Select a folder to filter")
        self.cancelBtn = QPushButton("Cancel")

        self.layout.addWidget(self.startBtn)
        self.layout.addWidget(self.cancelBtn)

    def getDirectory(self):
        self.userPath = QFileDialog.getExistingDirectory(
            parent=self,
            caption="Select a directory"
        )
        return self.userPath
