import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import os

# Load the model
model = load_model('butterfly_model.h5')

# Define class names (replace with your actual classes)
class_names = ['Monarch', 'Painted Lady', 'Swallowtail', 'Other']  # <-- update this

def predict(img_path):
    if not os.path.exists(img_path):
        print(f"File not found: {img_path}")
        return

    try:
        img = image.load_img(img_path, target_size=(224, 224))
        img = image.img_to_array(img) / 255.0
        img = np.expand_dims(img, axis=0)

        predictions = model.predict(img)
        class_index = np.argmax(predictions)
        confidence = predictions[0][class_index] * 100

        print(f"Predicted class index: {class_index}")
        print(f"Class: {class_names[class_index]}")
        print(f"Confidence: {confidence:.2f}%")

    except Exception as e:
        print("Error loading or processing image:", e)

# Example usage:
predict('sample_test.jpg')
model = tf.keras.models.load_model('butterfly_model.h5', compile=False)
