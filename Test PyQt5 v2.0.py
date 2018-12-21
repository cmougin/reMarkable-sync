#!/usr/bin/python
# -*- coding : utf-8 -*-
# librement inspire du ebook "PyQt5 101 - A Begginer's guide to PyQt5" by Eddie Nambulous
import sys, os
import argparse
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QScrollArea, QFileSystemModel, QTreeView, QTreeWidget, QTreeWidgetItem
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import * #KeepAspectRatio, FastTransformation, pyqtSlot, ...
from GetFileArbo import GetFileArbo, noeud, TreeWidget
from scrollAreaMiniaturePage import scrollAreaMiniaturePage, VBoxLayoutMiniatures
from scrollAreaPagePleine import *#ScrollAreaPagePleine

class WidgetEcranPrincipal(QWidget):
    def __init__(self, subdir):
        super().__init__()
        self.repertoire = os.path.join(subdir, "reMarkable-backup/home/root/.local/share/remarkable/xochitl")

        self.initUI()
        self.connectWidgets()

    def initUI(self):
        self.setWindowTitle('essai Christophe 15 décembre 2018')
        HBoxLayoutEcranPrincipal = QHBoxLayout()
        self.treeWidget = TreeWidget(self.repertoire)
        HBoxLayoutEcranPrincipal.addWidget(self.treeWidget)
        self.vBoxLayoutMiniatures = VBoxLayoutMiniatures(self.repertoire)
        HBoxLayoutEcranPrincipal.addLayout(self.vBoxLayoutMiniatures)
        HBoxLayoutEcranPrincipal.addWidget(scrollAreaPagePleine(self.repertoire))
        self.setLayout(HBoxLayoutEcranPrincipal)
        self.show()

    def connectWidgets(self):
        #void itemClicked(QTreeWidgetItem *item, int column)
        self.treeWidget.itemClicked.connect(self.slotTreewidgetClicked)

    #@pyqtSlot(QWQTreeWidgetItem, int) #pas correct. sert à optimiser, mais n'a aucun effet apparent
    def slotTreewidgetClicked(self, ItemClicked, column):
        self.vBoxLayoutMiniatures.updateMiniatures(ItemClicked.text(2)) #text(2) soit la valeur cachée par setdata(2, ...) çàd le NoeudID
        # for noeudID in noeud.noeudIDs.keys(): #recherche du noeud cliqué dans le dictionnaire de la classe
        #     if noeud.noeudIDs[noeudID].TreeWidget == ItemClicked: #bingo
        #         self.vBoxLayoutMiniatures.updateMiniatures(noeud.noeudIDs[noeudID].ID) #ID est le nom du sous répertoire voulu
        #         print(self.noeudIDs[noeudID].ID, "clicked")

if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description="un peu d'aide:", epilog="merci de réessayer")
    parser.add_argument('--dropboxDir', action='store', dest="DropboxDir", default=False, help='merci de fournir le homdir de Dropbox')
    arguments = parser.parse_args()

    app = QApplication(sys.argv)
    FenetrePrincipale = WidgetEcranPrincipal(subdir=arguments.DropboxDir)#r"Dropbox\reMarkable-backup\home\root\.local\share\remarkable\xochitl")
    sys.exit(app.exec_())