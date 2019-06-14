# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 18:28:06 2019

@author: hiago
"""
from zipfile import ZipFile, is_zipfile
from data.utils import write_folder
from os import getcwd


class ZipExtract(object):
    """The summary line for a class docstring should fit on one line.

    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """
    __instance = None

    def __init__(self):
        if ZipExtract.__instance is not None:
            self.__instance = ZipExtract.__instance
        else:
            ZipExtract.__instance = self

    @staticmethod
    def getInstance():
        if ZipExtract.__instance is None:
            ZipExtract()
        return ZipExtract.__instance

    def get_zip_file(self, path):
        """Classe para obtenção do .zip e extração do mesmo

        Args:
            path: Uma string com o caminho do arquivo .zip.

        Returns:
            True se sucesso, False em outro caso.

        """
        try:
            if not is_zipfile(path):
                raise ValueError("Este não é um arquivo .zip")
        except ValueError as ve:
            print(ve)

        _path = getcwd() + "/data/datasets"

        file = ZipFile(path)
        file.extractall(_path)
        file.close()

        fileName = path.split("/")[-1]
        folder = fileName.replace(".zip", "")
        write_folder(folder)
        return folder
