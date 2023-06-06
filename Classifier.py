from PIL import Image
from tensorflow.keras import utils, models
from tensorflow import nn

import tensorflow as tf
import numpy as np

import os
import shutil


if __name__ == '__main__':
    # Paths
    model = models.load_model(os.path.abspath(os.path.join(os.path.dirname(__file__))) + '\\Model\\Model_Data\\')

    print('Model loaded!')

    input_path = (os.path.abspath(os.path.join(os.path.dirname(__file__))) + '\\Input Images\\')
    output_path = (os.path.abspath(os.path.join(os.path.dirname(__file__))) + '\\Classified Images\\')

    # Clear output folder
    print('\nClearing Classified Images (.jpg) images...')
    for file in os.listdir(output_path):
        if os.path.exists(os.path.join(output_path + '\\Samsung\\')):
            shutil.rmtree(output_path+'Samsung\\')
        if os.path.exists(os.path.join(output_path + '\\Iphone\\')):
            shutil.rmtree(output_path+'Iphone\\')
        if file.endswith('.jpg'):
            os.remove(os.path.join(output_path, file))
    print('Classified Images folder cleared!')

    # Cache
    if not os.path.exists(os.path.join(input_path + '\\Cache\\')):
        os.mkdir(input_path + 'Cache\\') # Creates a cached folder for predicting image one by one
        cache_path = input_path + 'Cache\\'
    else:
        # Cleares the folder
        cache_path = input_path + 'Cache\\'
        for file in os.listdir(cache_path):
            if file.endswith('.jpg'):
                os.remove(cache_path + file)
    
    # Copy and predict
    count = 0 # To check the availibility of image
    print('\nStarting image scan...')
    for file in os.listdir(input_path):
        if file.endswith(('.jpg', '.png', '.jpeg')):
            count = 1
            f = file.replace(f".{file.split('.')[-1]}", '')

            print(f'Predicting {f}...')

            img = Image.open(input_path+file).convert('RGB')
            img.save(os.path.join(cache_path, f'{f}.jpg')) # Saves in cache folder

            # Prediction
            data = utils.image_dataset_from_directory(cache_path, labels=None, image_size=(350, 350))
            data = tf.nn.sigmoid(model.predict(data)).numpy() # Sigmoid function for binary classification
            data = np.rint(np.squeeze(data)) # Gets the prediction

            # 0 -> Iphone
            # 1 -> Samsung
            label = {0: 'Iphone', 1: 'Samsung'}
            print(f'{f} has {label[data]} image!')
            if not os.path.exists(output_path + f'//{label[data]}//'):
                os.mkdir(output_path + f'//{label[data]}//')
            shutil.copy2(cache_path+f+'.jpg', output_path + f'{label[data]}//' + f'//{f}.jpg')
            os.remove(os.path.join(cache_path+f+'.jpg'))
            
    if not count: print(f'\nNo images found! If you have entered the images, check if they are located in {input_path}. If not, check if they are of supported file type, refer to README.md for that.')

    # Removes Cache folder
    if os.path.exists(os.path.join(input_path + '\\Cache\\')):
        shutil.rmtree(cache_path)
