from PIL import Image

import os


if __name__ == '__main__':
    # Defaults
    count = 1

    # File path
    samsung_galaxy = os.path.abspath(os.path.join(os.path.dirname(__file__))) + '\\Raw Data\\Samsung\\Samsung Galaxy\\'
    samsung_new = os.path.abspath(os.path.join(os.path.dirname(__file__))) + '\\Raw Data\\Samsung\\Samsung New\\'
    samsung_phone = os.path.abspath(os.path.join(os.path.dirname(__file__))) + '\\Raw Data\\Samsung\\Samsung phone\\'
    samsung_series = os.path.abspath(os.path.join(os.path.dirname(__file__))) + '\\Raw Data\\Samsung\\Samsung phone series\\'
    samsung_a = os.path.abspath(os.path.join(os.path.dirname(__file__))) + '\\Raw Data\\Samsung\\Samsung A series\\'
    samsung_s = os.path.abspath(os.path.join(os.path.dirname(__file__))) + '\\Raw Data\\Samsung\\Samsung S series\\'
    samsung_latest = os.path.abspath(os.path.join(os.path.dirname(__file__))) + '\\Raw Data\\Samsung\\samsung latest phone\\'

    iphone_f = os.path.abspath(os.path.join(os.path.dirname(__file__))) + '\\Raw Data\\Iphone\\Iphone\\'
    iphone_pre = os.path.abspath(os.path.join(os.path.dirname(__file__))) + '\\Raw Data\\Iphone\\Iphone_Pre\\'
    iphone_new = os.path.abspath(os.path.join(os.path.dirname(__file__))) + '\\Raw Data\\Iphone\\Iphone New\\'

    # Save path
    samsung = os.path.abspath(os.path.join(os.path.dirname(__file__))) + '\\Training Data\\Samsung\\'
    iphone = os.path.abspath(os.path.join(os.path.dirname(__file__))) + '\\Training Data\\Iphone\\'

    samsung_validation = os.path.abspath(os.path.join(os.path.dirname(__file__))) + '\\Validation Data\\Samsung\\'
    iphone_validation = os.path.abspath(os.path.join(os.path.dirname(__file__))) + '\\Validation Data\\Iphone\\'

    # Rename the files and saves them
    samsung_list = [samsung_galaxy, samsung_new, samsung_phone, samsung_series, samsung_a, samsung_s]
    iphone_list = [iphone_f, iphone_new, iphone_pre]

    def initialise(iter_list: list, dest, valid):
        '''Initializes the files from Raw Data to Training or Validation Data'''

        global count

        p_val = 0

        for path in iter_list:
            # Gets the total no. of images

            total_img = len(os.listdir(path))
            val = round(total_img - ((total_img * 0.2, total_img * 0.3)[total_img > 100]))
            p_val += val

            for x in os.listdir(path):
                img = Image.open(path+x).convert('RGB')

                # Training or Validation
                if len(os.listdir(dest)) <= p_val: img.save(f'{dest}{str(count)}.jpg')
                else: img.save(f'{valid}{str(count)}.jpg')

                count += 1
    

    initialise(samsung_list, samsung, samsung_validation)
    count = 1 # Count reset
    initialise(iphone_list, iphone, iphone_validation)

