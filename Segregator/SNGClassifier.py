#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 20:59:40 2019

@author: hiago
"""


import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog
from PyQt5.uic import loadUi
from data.run_dataset import run_dataset


class SNGClassifier(QDialog):
    def __init__(self):
        super(SNGClassifier, self).__init__()
        loadUi('interface/dialog.ui', self)
        self.setWindowTitle('Singaro Classifier')
        self.UpDstBtn.clicked.connect(self.on_pushButton_clicked)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        filePath = QFileDialog.getOpenFileName(self, ".ZIP", "~/", "*.zip")
        if filePath:
            run_dataset(filePath[0])

       # self.labe1.setText('Welcome: ' + self.lineEdit.text())


app = QApplication(sys.argv)
widget = SNGClassifier()
widget.show()
sys.exit(app.exec_())
