from PyQt5.QtWidgets import QLabel, QScrollArea, QVBoxLayout
from PyQt5.QtGui import QPixmap
import os, re

class scrollAreaMiniaturePage(QScrollArea):
    def __init__(self, fichier):
        super().__init__()
        self.initUI(fichier)

    def initUI(self, fichier):
        PixmapMiniaturePage = QPixmap(fichier)
        LabelMiniaturePage = QLabel()
        LabelMiniaturePage.setPixmap(PixmapMiniaturePage)
        self.setWidget(LabelMiniaturePage)

class VBoxLayoutMiniatures(QVBoxLayout):
    def __init__(self, repertoire):
        super().__init__()
        self.mesWidgets = []
        self.repertoire = repertoire
        #self.initUI(repertoire)

    def initUI(self, repertoire):
        self.mesWidgets.append(scrollAreaMiniaturePage(os.path.join(repertoire, r"05f88dec-87f5-44f8-85fc-dd20b99bd66d.thumbnails/1.jpg")))
        self.addWidget(self.mesWidgets[-1]) #le dernier de la liste, donc celui qu'on vient d'ajouter
        self.mesWidgets.append(scrollAreaMiniaturePage(os.path.join(repertoire, r"05f88dec-87f5-44f8-85fc-dd20b99bd66d.thumbnails/0.jpg")))
        self.addWidget(self.mesWidgets[-1])

    def updateMiniatures(self, subdir):
        print("bien reçu:", subdir)
        for w in self.mesWidgets:
            self.removeWidget(w)
        self.mesWidgets=[]
        dossier = os.path.join(self.repertoire, subdir+'.thumbnails')
        regexp = re.compile(r'.*jpg') #les noms de fichiers finissant par "metadata"
        for f in filter(regexp.match, os.listdir(path=dossier)): #pour tous les fichiers du répertoire, dont le nom matche
            self.mesWidgets.append(scrollAreaMiniaturePage(os.path.join(dossier, f)))
            self.addWidget(self.mesWidgets[-1])