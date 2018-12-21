import json, sys, re, os, pprint
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem
from PyQt5.QtCore import *

class TreeWidget(QTreeWidget):
    def __init__(self, repertoire):
        super().__init__()
        GetFileArbo(repertoire)
        self.initUI()

    def initUI(self):
        self.setColumnCount(1)
        self.setHeaderLabels(["reMarkable files"])
        noeud.updateTreeWidget(parent=self)

class noeud():
    pereIDs = dict() #arbo des noeuds, la  racine a pour ID "0"
    noeudIDs = dict() # liste des noeuds, pour les retrouver

    def __init__(self, ID, visibleName = "", pereID = "0", TreeWidget = None):
        self.ID = ID
        self.pereID = pereID
        self.visibleName = visibleName
        self.TreeWidget = TreeWidget
        self.addPereID(ID, pereID)
        self.addNoeudID(ID)

    def addNoeudID(self, ID):
        self.noeudIDs[ID] = self

    def addPereID(self, filsID, pereID):
        if pereID in self.pereIDs.keys():
            try:
                listeDesFils = self.pereIDs[pereID]
                listeDesFils.append(filsID)
                self.pereIDs.update({pereID: listeDesFils})
            except Exception as e:
                pprint.pprint(e)
                print("impossible d'ajouter .{filsID}. à self.pereIDs[{pereID}] qui vaut ({self.pereIDs[pereID]})".format(filsID, pereID, self.pereIDs[pereID]))
        else:
            self.pereIDs[pereID] = [filsID]

    @classmethod
    def updateTreeWidget(self, parent, pereID = "0"):
        if pereID in self.pereIDs.keys():
            for noeudID in self.pereIDs[pereID]:
                #creer le Widget
                newTreeWidget = QTreeWidgetItem(parent)
                newTreeWidget.setText(0, self.noeudIDs[noeudID].visibleName)
                #inspiré librement de https://gist.github.com/fredrikaverpil/1fa4f3360ffdb1e69507
                #on peut associer à chaque feuille de l'arbo une valeur cachée, ici "noeudID":
                newTreeWidget.setData(2, Qt.DisplayRole, noeudID) # Data set to column 2, which is not visible
                self.noeudIDs[noeudID].TreeWidget = newTreeWidget
                #iterer récursivement avec les filsID du pereID
                self.updateTreeWidget(parent=newTreeWidget, pereID=noeudID)

def GetFileArbo(repertoire):
    regexp = re.compile('.*metadata') #les noms de fichiers finissant par "metadata"
    for f in filter(regexp.match, os.listdir(path=repertoire)): #pour tous les fichiers du répertoire, dont le nom matche
        fileID = f.rstrip(".metadata")
        with open(os.path.join(repertoire, f), "r") as FluxJson:
            donnees = json.load(FluxJson)
        if donnees["parent"] == "": #si donnees["parent"]=="" alors c'est un document racine
            parent = "0"
        else:
            parent = donnees["parent"] 
        #print(f, ":", donnees["parent"], donnees["visibleName"])
        n = noeud(fileID, visibleName=donnees["visibleName"], pereID=parent)

if __name__ == "__main__":
    GetFileArbo(r"C:\Utilisateurs\FR20340\Dropbox\reMarkable-backup\home\root\.local\share\remarkable\xochitl")
    pprint.pprint(noeud.pereIDs)