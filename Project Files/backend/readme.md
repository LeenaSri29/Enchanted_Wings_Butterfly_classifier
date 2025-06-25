
---

## 📘 `backend/README.md`
Place this in your root folder or create a `backend/` folder with your Python files.

```markdown
# 🧠 Backend - Enchanted Wings

This folder contains all **backend logic** and **AI prediction code** for the Enchanted Wings butterfly classifier.

## 🗂 Files

- `app.py`: Main Flask application that:
  - Loads the trained model (`butterfly_model.h5`)
  - Handles routes for the web app (`/`, `/input`, `/output`)
  - Processes image uploads and makes predictions

- `Model.predict.py`: (Optional) Standalone script to test prediction logic separately from Flask.

- `butterfly_model.h5`: Pretrained Keras model for butterfly species classification.

- `dataset/` and `butterfly_dataset/`: Image data used for training/validation.

- `Scripts/`: Contains preprocessing, training, or helper Python scripts.

## 🔁 Workflow

1. User uploads image via frontend.
2. Image is passed to `app.py`.
3. Model predicts species using `model.predict(img_array)`.
4. Prediction and confidence are shown on `output.html`.

## 🔧 Libraries Used

- Flask
- TensorFlow / Keras
- NumPy
- Pillow (PIL)
- OS, datetime

## 🚀 To Run

```bash
python app.py
