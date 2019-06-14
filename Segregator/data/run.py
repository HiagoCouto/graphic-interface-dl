#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 10:52:30 2019

@author: hiago
"""
from preparation import Preparation
from zipExtract import ZipExtract


def run(zipPath):
    folderName = ZipExtract().get_zip_file(zipPath)
    data = Preparation(folderName).getInstance()
    data.train_test_move_to_dirs(data.train_test_separation
                                 (data.train_test_make_dirs()))


"""
class Main(object):
    The summary line for a class docstring should fit on one line.

    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.


    __instance = None
    folder = ""

    def __init__(self, folder):
        Classe para obtenção do .zip e extração do mesmo

            Args:
                folder:

        self.folder = folder

        if Main.__instance is not None:
            Main.folder = folder
            self.__instance = Main.__instance
        else:
            Main.__instance = self

    @staticmethod
    def getInstance():
        if Main.__instance is None:
            Main()
        return Main.__instance
"""