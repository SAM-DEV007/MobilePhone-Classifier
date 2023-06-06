from bing_image_downloader import downloader

import os


def main():
    '''The main function to download images from internet'''

    # Query
    samsung_queries = [
        "Samsung phone", "Samsung Galaxy", "Samsung New", "Samsung S series", "Samsung phone series", "Samsung A series", "samsung latest phone"
    ]
    iphone_queries = [
        "Iphone", "Iphone New"
    ]

    # Iphone_Pre contains almost 500 images
    # which was included, and not downloaded from this script.
    # That's why, the Samsung have more queries.

    # Save path
    save_dir_samsung = os.path.abspath(os.path.join(os.path.dirname(__file__))) + '\\Raw Data\\Samsung\\'
    save_dir_iphone = os.path.abspath(os.path.join(os.path.dirname(__file__))) + '\\Raw Data\\Iphone\\'

    # Images
    for q in samsung_queries:
        downloader.download(
            q, 100, save_dir_samsung, timeout=3
        )
    for q in iphone_queries:
        downloader.download(
            q, 100, save_dir_iphone, timeout=3
        )


if __name__ == '__main__':
    main()
