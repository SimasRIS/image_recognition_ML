# Image Recognition with HOG + Random Forest

## Project overview

This simple image recognition program can identify four types of images: cars, cats, dogs, and paintings. It uses basic machine learning techniques to analyze and classify images.

The program is written in a file called **`iamge_recognition_ML.py`** (note: there's a typo in the filename). When tested, it can correctly identify images about 72% of the time.

Main point: This basic approach works decently for small sets of images, but to get better results, you'd need more images or improved settings.

---

## How it works

| Step | Program part | What it does                                                                                                                                                 |
| --- | --- |--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **1 — Organizing images** | variable`data_set_path` | Images are stored in folders named 'car', 'cat', 'dog', and 'painting'                                                                                       |
| **2 — Processing images** | loop over`categories` | · Loads each image <br/>· Converts colorful images to black and white <br/>· Makes all images the same size (128 × 64 pixels) <br/>· Analyzes image patterns |
| **3 — Splitting data** | `StratifiedShuffleSplit` | Splits images into two groups: 55% for training and 45% for testing                                                                                          |
| **4 — Learning** | `RandomForestClassifier` | Uses 100 decision trees to learn patterns in images                                                                                                          |
| **5 — Testing** | `accuracy_score` | Shows how well it works (72% accuracy) and displays results with images                                                                                      |

---

## How to start

```
# 1. Get the program files
$ git clone https://github.com/SimasRIS/hog‑rf‑image‑recog.git
$ cd image_recognition_ML

# 2. (Optional) set up a separate environment
$ python -m venv venv
$ source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. Install needed software
$ pip install -r requirements.txt

# 4. Organize your images like this:
img/
├── car/
│   ├── car1.jpg
│   └── …
├── cat/
│   └── …
├── dog/
│   └── …
└── painting/
    └── …

# 5. Run the program
$ python iamge_recognition_ML.py
```

---

## Understanding the 72% accuracy

| Question | Answer                                                                                                                                   |
| --- |------------------------------------------------------------------------------------------------------------------------------------------|
| **What does it mean?** | The program correctly identifies 72 out of every 100 images it tests.                                                                    |
| **Why isn't it better?** | · Not enough example images <br/>· Some images look similar (like cats and dogs) <br/>· The program can't use color information          |
| **How could we improve it?** | · Add more images <br/>· Try different program settings <br/>· Use more advanced AI technology Include color information in the analysis |

---
