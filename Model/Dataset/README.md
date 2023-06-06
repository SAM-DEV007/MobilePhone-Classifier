# Dataset
  Most of the dataset generated is from the internet, especially from bing. Kaggle has [Iphone dataset](https://www.kaggle.com/datasets/radvian/apple-products-image-dataset)
  with over 500 images. Other than that, the Samsung dataset is generated from Bing Images with different keywords.
  [Generate_Data.py](Generate_Data.py) is used to download the images from the internet.
  
  [Raw Data](Raw%20Data) folder contains all the generated and pre-downloaded dataset. It is, then, checked manually for
  anomalies and are deleted. Therefore, the Raw Data folder contains over 1,257 files of both Samsung and Iphone.
  
  After the data is being checked, it is then divided between [Training Data](Training%20Data) and [Validation Data](Validation%20Data)
  in the ratio 70:30 respectfully. It is done by [Transfer_Data.py](Transfer_Data.py) file.
