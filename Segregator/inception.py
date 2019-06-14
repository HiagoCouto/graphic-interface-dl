#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 16:06:41 2019

@author: hiago
"""
from keras.models import Model
from keras.layers import Dense, GlobalAveragePooling2D, Dropout
from keras.applications.inception_v3 import InceptionV3, preprocess_input
from keras.preprocessing.image import ImageDataGenerator
from data.utils import get_labels
from data.utils import retrieve_from_list_file


def inceptionV3():
    DATASET = retrieve_from_list_file('data/datasets/folder.txt')[0]
    CLASSES = len(get_labels('data/datasets/' + DATASET))
    WIDTH = 299
    HEIGHT = 299
    BATCH_SIZE = 32

    # setup model
    base_model = InceptionV3(weights='imagenet', include_top=False)

    x = base_model.output
    x = GlobalAveragePooling2D(name='avg_pool')(x)
    x = Dropout(0.4)(x)
    predictions = Dense(CLASSES, activation='softmax')(x)
    model = Model(inputs=base_model.input, outputs=predictions)

    # transfer learning
    for layer in base_model.layers:
        layer.trainable = False

    model.compile(optimizer='rmsprop',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    # data prep
    train_datagen = ImageDataGenerator(
        preprocessing_function=preprocess_input,
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

    validation_datagen = ImageDataGenerator(
        preprocessing_function=preprocess_input,
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

    train_generator = train_datagen.flow_from_directory(
        'data/datasets/' + DATASET + '/test',
        target_size=(HEIGHT, WIDTH),
        batch_size=BATCH_SIZE,
        class_mode='categorical')

    validation_generator = validation_datagen.flow_from_directory(
        'data/datasets/' + DATASET + '/train',
        target_size=(HEIGHT, WIDTH),
        batch_size=BATCH_SIZE,
        class_mode='categorical')

    EPOCHS = 5
    BATCH_SIZE = 32
    STEPS_PER_EPOCH = 320
    VALIDATION_STEPS = 64

    MODEL_FILE = 'Segregator.model'

    model.fit_generator(
        train_generator,
        epochs=EPOCHS,
        steps_per_epoch=STEPS_PER_EPOCH,
        validation_data=validation_generator,
        validation_steps=VALIDATION_STEPS)

    model.save(MODEL_FILE)
    return MODEL_FILE
