from PyQt5.QtWidgets import QLabel, QScrollArea
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import * #KeepAspectRatio, FastTransformation

class scrollAreaPagePleine(QScrollArea):
    def __init__(self, repertoire):
        super().__init__()
        self.initUI(repertoire)

    def initUI(self, repertoire):
        PixmapPagePleine = QPixmap(repertoire + r"/05f88dec-87f5-44f8-85fc-dd20b99bd66d.cache/1.png")
        PixmapPagePleine = PixmapPagePleine.scaled(500, 500, Qt.KeepAspectRatio, Qt.FastTransformation)
        LabelPagePleine = QLabel()
        LabelPagePleine.setPixmap(PixmapPagePleine)
        self.setWidget(LabelPagePleine)
