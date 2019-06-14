#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 04:57:37 2019

@author: hiago
"""
import os


def retrieve_from_list_file(path):
    """Classe para obtenção do .zip e extração do mesmo

    Args:
        path: Recebe uma String representando o caminho do diretório

    Returns:
        Uma lista com os labels (nomes das pastas) se sucesso,
        False em outro caso.

    """
    labels_txt = open(path, 'r')
    _labels = labels_txt.readlines()

    labels = []
    for idx, item in enumerate(_labels):
        labels.append(_labels[idx].replace('\n', ''))

    labels_txt.close()

    return labels


def get_labels(path):
    """Classe para obtenção do .zip e extração do mesmo

    Args:
        path: Recebe uma String representando o caminho do diretório

    Returns:
        Uma lista com os labels (nomes das pastas) se sucesso,
        False em outro caso.

    """
    if os.path.isfile(path + 'labels.txt'):
        return retrieve_from_list_file(path + 'labels.txt')
    else:
        try:
            _dirs = os.listdir(path)
            if not _dirs:
                raise ValueError("O diretorio está vazio")
        except ValueError as ve:
            print(ve)
            return False

        dirs = list(filter(lambda x: os.path.isdir(path + x), _dirs))
        labels = open(path + 'labels.txt', 'w')

        for label in dirs:
            labels.write(label + "\n")
        labels.close()

        return dirs


def write_folder(folderName):
    folder = open('data/datasets/folder.txt', 'w')

    folder.write(folderName + "\n")
    folder.close()
