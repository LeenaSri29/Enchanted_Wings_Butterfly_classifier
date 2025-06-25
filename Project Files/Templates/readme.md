
---

### 📁 `templates/README.md`
```markdown
# 📁 Templates Folder

This folder contains the **HTML templates** used by Flask in the Enchanted Wings web application.

## 🧩 Contents

- **index.html**  
  Home page with a welcome message and a link to start the butterfly identification process.

- **input.html**  
  Page where the user uploads a butterfly image for prediction.

- **output.html**  
  Results page that displays the predicted butterfly species and confidence score.

## 🧠 How Flask Uses These Templates

The templates are rendered using `render_template()` in `app.py`, for example:

```python
@app.route("/")
def index():
    return render_template("index.html")
