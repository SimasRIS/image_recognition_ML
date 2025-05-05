# Picture Recognition Program

## What Does This Program Do?

This program can look at pictures and tell if they show cars, cats, dogs, or paintings. It uses simple artificial intelligence to figure out what's in each picture.

The program is saved in a file named **`iamge_recognition_ML.py`** (there's a spelling mistake in the name). When we tested it, it gets the right answer about 72% of the time.

Quick summary: The program works okay with a small number of pictures, but it could do better if we gave it more pictures to learn from.

---

## How Does It Work?

| Step | Part of Program | What It Does                                                                                              |
| --- | --- |-----------------------------------------------------------------------------------------------------------|
| **1 — Setting Up Pictures** | folder system | Pictures are put into separate folders for cars, cats, dogs, and paintings                                |
| **2 — Getting Pictures Ready** | picture processing | · Opens each picture <br/>· Makes them black and white <br/>· Makes all pictures the same size <br/>· Looks for patterns |
| **3 — Dividing Pictures** | sorting system | Splits pictures into two groups: one for teaching the program (55%) and one for testing it (45%)          |
| **4 — Learning** | AI learning system | Uses 100 different ways to learn what makes each type of picture unique                                   |
| **5 — Checking Results** | testing system | Shows how well the program can identify pictures (gets 72% right)                                         |

---

## Getting Started

1. Get the program files
```
$ git clone https://github.com/SimasRIS/image_recognition_ML.git
```
```
$ cd image_recognition_ML
```
2. (Optional) set up a separate environment
```
$ python -m venv venv
```
```
$ source venv/bin/activate   
```
Windows: 
```
venv\Scripts\activate
```
3. Install needed software
```
$ pip install -r requirements.txt
```
4. Put your pictures in folders like this:
```
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
```
5. Start the program
```
$ python iamge_recognition_ML.py
```

---

## About the 72% Success Rate

| Question | Answer                                                                                                                                                |
| --- |-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **What does 72% mean?** | Out of every 100 pictures, the program correctly identifies 72 of them.                                                                               |
| **Why isn't it more accurate?** | · We don't have enough example pictures<br/>· Some pictures (like cats and dogs) can look very similar<br/>· The program only sees in black and white |
| **How can we make it better?** | · Use more pictures for training <br/>· Adjust the program's settings <br/>· Use newer AI technology <br/>· Let the program use color information                    |

