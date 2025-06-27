import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras import layers, models

os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

train_path = 'dataset/train'
val_path = 'dataset/val'

img_size = (224, 224)
batch_size = 32
epochs = 5

train_gen = ImageDataGenerator(rescale=1./255).flow_from_directory(
    train_path, target_size=img_size, batch_size=batch_size, class_mode='categorical')

val_gen = ImageDataGenerator(rescale=1./255).flow_from_directory(
    val_path, target_size=img_size, batch_size=batch_size, class_mode='categorical')

base_model = MobileNetV2(input_shape=img_size + (3,), include_top=False, weights='imagenet')
base_model.trainable = False

model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(train_gen.num_classes, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(train_gen, validation_data=val_gen, epochs=epochs)
model.save("butterfly_model.h5")
