# 📁 Static Folder

This folder contains **static assets** for the Enchanted Wings Butterfly Classifier web application.

## 🎨 Contents

- **style.css**  
  Contains all visual styling used across HTML templates, including:
  - Light, professional background (`#e3f2fd`)
  - Dark text (`#1a237e`) for contrast and readability
  - Accent color (`#00796b`) for elements like labels
  - Button styling (default and hover states)
  - Uses the `'Nunito'` font from Google Fonts

## ✅ Usage in Templates

All templates include this CSS using Flask’s `url_for()` method:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
