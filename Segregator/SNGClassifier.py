#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 20:59:40 2019

@author: hiago
"""


import sys
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog
from PyQt5.uic import loadUi
from data.run_dataset import run_dataset
from main import run


class SNGClassifier(QDialog):
    imgPath = ""

    def __init__(self):
        super(SNGClassifier, self).__init__()
        loadUi('interface/dialog.ui', self)
        self.setWindowTitle('Singaro Classifier')
        self.UpDstBtn.clicked.connect(self.on_pushDatasetBtn_clicked)
        self.UpSubBtn.clicked.connect(self.on_pushImgBtn_clicked)
        self.StartBtn.clicked.connect(self.on_startBtn_clicked)

    @pyqtSlot()
    def on_pushDatasetBtn_clicked(self):
        filePath = QFileDialog.getOpenFileName(self, ".ZIP", "~/", "*.zip")
        if filePath:
            self.DstStateLb.setText(run_dataset(filePath[0]))

    @pyqtSlot()
    def on_pushImgBtn_clicked(self):
        filePath = QFileDialog.getOpenFileName(self,
                                               "Imagem para Classificação",
                                               "~/", "*.jpg, *.jpeg")
        if filePath:
            self.imgPath = filePath[0]
            self.SubStateLb.setText(self.imgPath.split("/")[-1])

    @pyqtSlot()
    def on_startBtn_clicked(self):
        if self.imgPath:
            run(self.imgPath)


app = QApplication(sys.argv)
widget = SNGClassifier()
widget.show()
sys.exit(app.exec_())
