# Waste Detection using YOLO (Computer Vision Project)

Computer vision system developed for an intelligent waste-collecting robot, capable of detecting waste and trash bins using a YOLO-based object detection model.

This repository contains the model training pipeline and the inference module used to evaluate detection performance.

---

## Features

* YOLO-based object detection training
* Supervised learning workflow (dataset preparation, training, validation)
* GPU training using Google Colab
* Image / video inference testing
* Bounding box visualization
* Model export after training

---

## Technologies

* Python
* Ultralytics YOLO
* PyTorch
* OpenCV
* Google Colab

---

## Project Structure

train.py
→ Script used to train the object detection model

test_reconocimiento.py
→ Script used to test detection performance

requirements.txt
→ Required Python libraries

---

## My Contribution

This was a collaborative academic project.

My responsibilities included:

* Configuring the training environment
* Participating in dataset preparation and labeling workflow
* Running model training experiments
* Implementing the detection testing script
* Evaluating detection performance

---

## Notes

Training was performed using a cloud GPU environment via Google Colab.

Large datasets and trained weights are NOT included in this repository.

---

## How to Run

Install dependencies:

pip install -r requirements.txt

Run detection test:

python test_reconocimiento.py

---

## Disclaimer

Dataset paths, Google Drive links, and API keys were intentionally removed for security reasons.
