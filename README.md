# [Project Name]: Object Detection using YOLO11n

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![YOLO11](https://img.shields.io/badge/model-YOLO11n-green)

## 📌 Abstract

This repository contains the official implementation of the research project: **Implementation of a Transfer Learning-Based YOLO11n Model for Recyclable Waste Detection**.
We utilize the YOLO11n architecture with transfer learning to detect **Recyclable and Organic Waste** in **Real World Environment**. This project aims to **improve automated recyclable waste detection** by implementing a **YOLO11n model with transfer learning and evaluating layer-freezing strategies** to achieve an optimal balance between detection accuracy and computational efficiency.

## 🏗️ Model Architecture

We employ **YOLO11n (Nano)** due to its balance between inference speed and accuracy, suitable for edge devices.

- **Pre-trained Weights:** COCO dataset
- **Transfer Learning:** Fine-tuned on a custom dataset of 2.462 images
- **Modifications:** Standard Architecture

## 📂 Dataset

The dataset used for training is **Recycle Trash Computer Vision Dataset**.

- **Source:** [**Recycle Trash Computer Vision Dataset**](https://universe.roboflow.com/serba-serbi-labelling/recycle-trash-tlwso/dataset/3)
- **Classes:** `metal`, `plastic`, `paper`, `cardboard`, `glass`, `organic`
- **Structure:**
  - Train: 1970 images
  - Val: 247 images
  - Test: 245 images

> **Note:** The dataset is not included in this repo due to size. You can download it here: [**Recycle Trash Computer Vision Dataset**](https://universe.roboflow.com/serba-serbi-labelling/recycle-trash-tlwso/dataset/3).

## ⚙️ Installation

1. **Clone the repository:**

   ```bash
   git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
   cd your-repo-name
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Linux: venv\vin\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Training

To train the model from scratch (or fine-tune), verify `config/data.yaml` paths and run:

    ```bash
    yolo task=detect mode=train model=yolo11n data=config/data.yaml # Change the model path accordingly, 'yolo11n' is the default pretrained model
    ```

_Artifacts (weights, logs) will be saved in the `runs/detect/train` directory_

See more training settings here: https://docs.ultralytics.com/modes/train/#train-settings

## 📊 Evaluation & Results

To evaluate the model on the test set :

    ```bash
    yolo task=detect mode=val model=model/yolo11n_backbone_freeze_best.pt data=config/data.yaml split=test # Change the model path accordingly
    ```

See more arguments for YOLO model validation here: https://docs.ultralytics.com/modes/val/#arguments-for-yolo-model-validation

## 🔍 Inference

Run inference on a custom image or video:

    ```bash
    yolo task=detect mode=predict model=runs/detect/train/weights/best.pt source='path/to/image.jpg' show=True # Change the 'model' and 'source' path accordingly
    ```

## Export

Export the model to a custom format:

    ```bash
    yolo export model=runs/detect/train/weights/best.pt format=onnx # Change the model path and format accordingly
    ```

See more available Ultraltics export format here: https://docs.ultralytics.com/usage/cli/#export

## 📜 Citation

If you use this code for your research, please cite:

    ```BibTeX
    @misc{YourName2025,
        author = {Valent Tio Inkiriwang},
        title = {Object Detection Project with YOLO11n},
        year = {2025},
        publisher = {GitHub},
        journal = {GitHub repository},
        howpublished = {\url{[https://github.com/your-username/your-repo](https://github.com/your-username/your-repo)}}
    }
    ```

## 🤝 Contributing

**Contributions are welcome!** Please check `CONTRIBUTING.md` for guidelines.

## 📄 License

`null`
