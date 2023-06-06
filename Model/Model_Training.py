import tensorflow as tf

import os


def main():
    '''It is the main function to train the model'''

    # Path
    train_dir = os.path.abspath(os.path.join(os.path.dirname(__file__))) + '\\Dataset\\Training Data\\'
    validation_dir = os.path.abspath(os.path.join(os.path.dirname(__file__))) + '\\Dataset\\Validation Data\\'

    # Save Path
    model_save = os.path.abspath(os.path.join(os.path.dirname(__file__))) + '\\Model_Data\\'

    # Defaults
    batch = 32
    img_size = (350, 350)

    # Datasets
    train_dataset = tf.keras.utils.image_dataset_from_directory(train_dir, labels='inferred', label_mode='binary', shuffle=True, batch_size=batch, image_size=img_size)
    validation_dataset = tf.keras.utils.image_dataset_from_directory(validation_dir, labels='inferred', label_mode='binary', shuffle=True, batch_size=batch, image_size=img_size)

    # Test Dataset
    val_batches = tf.data.experimental.cardinality(validation_dataset)
    test_dataset = validation_dataset.take(val_batches // 5)
    validation_dataset = validation_dataset.skip(val_batches // 5)

    # Performance
    autotune = tf.data.AUTOTUNE

    train_dataset = train_dataset.prefetch(buffer_size=autotune)
    validation_dataset = validation_dataset.prefetch(buffer_size=autotune)
    test_dataset = test_dataset.prefetch(buffer_size=autotune)

    # Data augmentation
    data_augmentation = tf.keras.Sequential([
        tf.keras.layers.RandomFlip('horizontal'),
        tf.keras.layers.RandomRotation(0.2),
    ])

    # ResNet50V2 Pre-trained model
    img_shape = img_size + (3,)
    base_model = tf.keras.applications.resnet_rs.ResNetRS50(input_shape=img_shape, include_top=False, weights='imagenet')
    base_model.trainable = False

    global_average_layer = tf.keras.layers.GlobalAveragePooling2D()
    prediction_layer = tf.keras.layers.Dense(1)

    # Base Model
    base_model.summary()

    # Customizing the base model
    inputs = tf.keras.Input(shape=(350, 350, 3))
    x = data_augmentation(inputs)
    x = base_model(x, training=False)
    x = global_average_layer(x)
    x = tf.keras.layers.Dropout(0.2)(x)
    outputs = prediction_layer(x)

    model = tf.keras.Model(inputs, outputs)

    base_learning_rate = 0.0001
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=base_learning_rate),
                loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
                metrics=['accuracy'])
    
    model.summary() # Customized model

    initial_epochs = 100
    model.evaluate(validation_dataset) # Before training test

    # Callbacks
    es_callback = tf.keras.callbacks.EarlyStopping(patience=3, verbose=1)

    # Train the model
    model.fit(train_dataset, epochs=initial_epochs, validation_data=validation_dataset, callbacks=[es_callback])

    model.save(model_save) # Save the model


if __name__ == '__main__':
    main()
