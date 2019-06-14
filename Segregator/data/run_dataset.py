#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 10:52:30 2019

@author: hiago
"""
from data.preparation import Preparation
from data.zipExtract import ZipExtract


def run_dataset(zipPath):
    folderName = ZipExtract().get_zip_file(zipPath)
    data = Preparation(folderName).getInstance()
    data.train_test_move_to_dirs(data.train_test_separation
                                 (data.train_test_make_dirs()))
