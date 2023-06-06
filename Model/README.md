# Model
  This model is a CNN Binary classifier with Base Model as Resnet-RS 50. The learning parameters are `1,024` and the rest of the
  layers frozen. The weights from the pre-trained model is from `imagenet`.
  
  `Adam` optimizer is used for the last layer, along with `Binary Crossentropy` as the loss function. The prediction from the
  trained model is from `[-inf, inf]` as there is no activation function in the last layer. Rather, `sigmoid` activation function
  is used on the data returned in [Classifier.py](/Classifier.py).
  
  The model obtained `88.64%` accuracy, with 35 epochs of training.
  
  There is no pre-processing included, as the Resnet-RS 50 is itself capable of preprocessing it. [Model_Training.py](Model_Training.py)
  is used to train and save the model. [Model_Data](Model_Data) folder contains the saved trained model.
