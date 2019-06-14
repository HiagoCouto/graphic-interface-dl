#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 00:19:01 2019

@author: hiago
"""

from data.utils import get_labels
from os import makedirs, rename
from glob import glob
from sklearn.model_selection import train_test_split
from re import search


class Preparation(object):
    """The summary line for a class docstring should fit on one line.

    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    Properties created with the ``@property`` decorator should be documented
    in the property's ttter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    __instance = None
    path = ""
    folder = ""
    labels = []

    def __init__(self, folder):
        """Classe para obtenção do .zip e extração do mesmo

            Args:
                folder:
        """
        self.folder = folder
        self.path = 'data/datasets/' + folder + '/'
        self.labels = get_labels(self.path)

        if Preparation.__instance is not None:
            self.__instance = Preparation.__instance
        else:
            Preparation.__instance = self

    @staticmethod
    def getInstance():
        if Preparation.__instance is None:
            Preparation()
        return Preparation.__instance

    def train_test_make_dirs(self):
        """Classe para obtenção do .zip e extração do mesmo

        Args:

        Returns:
            Um dicionário contendo o path para as imagens de cada label,
            False em outro caso.

        """
        makedirs(self.path + "train/")
        for label in self.labels:
            makedirs(self.path + "train/" + label)

        makedirs(self.path + "test/")
        for label in self.labels:
            makedirs(self.path + "test/" + label)

        data = dict()
        for label in self.labels:
            data[label] = glob(self.path + label + '/*.jpg')

        return data

    def train_test_separation(self, _data):
        """Classe para obtenção do .zip e extração do mesmo

        Args:
            data: Um dicionário contendo os path's das imagens de cada label

        Returns:
            True,
            False em outro caso.

        """
        pacote = dict()
        for (label, paths) in _data.items():
            pacote[label + '_train'], pacote[label + '_test'] =\
                train_test_split(paths, test_size=0.30)

        return pacote

    def train_test_move_to_dirs(self, pacote):
        """Classe para obtenção do .zip e extração do mesmo

        Args:
            data: Um dicionário contendo os path's das imagens de cada label

        Returns:
            True,
            False em outro caso.

        """
        for (label, paths) in pacote.items():
            tes = search(".*?(_test)$", label)
            tr = search(".*?(_train)$", label)
            if tes:
                for path in paths:
                    rename(path,
                           self.path + "test/" +
                           label.replace(label[-5:], "") + "/" +
                           path.split("/")[-1])

            if tr:
                for path in paths:
                    rename(path,
                           self.path + "train/" +
                           label.replace(label[-6:], "") + "/" +
                           path.split("/")[-1])

        return pacote
