# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from ui_parallelline import Ui_ParallelLine
import os, sys

class ParallelLineGui(QDialog, Ui_ParallelLine):
  
    def __init__(self, parent, flags):
        QDialog.__init__(self, parent, flags)
        self.setupUi(self)
        
        self.method = "fixed"
        
        self.okButton = self.buttonBox.button(QDialogButtonBox.Ok)
        self.connect(self.okButton, SIGNAL("accepted()"), self.accept)

        self.cancelButton = self.buttonBox.button(QDialogButtonBox.Cancel)
        self.connect(self.cancelButton, SIGNAL("clicked()"), self.close)        
        

    def initGui(self):
        self.spinBoxDistance.setMinimum(-10000000)
        self.spinBoxDistance.setMaximum(10000000)
        self.spinBoxDistance.setDecimals(3)
        
        self.radioFixed.setChecked(True)
        self.radioVertex.setChecked(False)
        pass
        
        
    @pyqtSignature("on_radioVertex_clicked()")    
    def on_radioVertex_clicked(self):     
        self.method = "fixed"
        self.spinBoxDistance.setEnabled(False)


    @pyqtSignature("on_radioFixed_clicked()")    
    def on_radioFixed_clicked(self):      
        self.method = "vertex"
        self.spinBoxDistance.setEnabled(True)
        
        
    def accept(self):
        self.emit( SIGNAL("okClicked(QString, double)"),  self.method,  self.spinBoxDistance.value())
        pass
        
    
    def close(self):
        self.emit(SIGNAL("unsetTool()")) 
        pass