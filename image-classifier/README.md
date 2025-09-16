# Image Classifier

A machine learning project for image classification using TensorFlow/Keras and Flask.

## Project Structure

```
image-classifier/
├── data/
│   └── images/          # Training and test images
├── models/
│   └── image_model.h5   # Trained model file
├── app.py               # Flask web application
├── train.ipynb          # Jupyter notebook for training
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Features

- **Image Classification**: Train a CNN model to classify images
- **Web Interface**: Flask-based web app for real-time predictions
- **Model Training**: Jupyter notebook for training and evaluation
- **Easy Setup**: Simple installation and usage

## Installation

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Training the Model

1. Place your training images in the `data/images/` directory
2. Organize images into subdirectories by class (e.g., `data/images/cat/`, `data/images/dog/`)
3. Open `train.ipynb` in Jupyter Notebook
4. Run all cells to train your model
5. The trained model will be saved as `models/image_model.h5`

### Running the Web App

1. Make sure you have a trained model in `models/image_model.h5`
2. Run the Flask application:
   ```bash
   python app.py
   ```
3. Open your browser and go to `http://localhost:5000`
4. Upload an image to get predictions

## Model Architecture

The default model uses a CNN architecture suitable for image classification:
- Convolutional layers with ReLU activation
- Max pooling layers
- Dropout for regularization
- Dense layers for classification

## Customization

- **Classes**: Update the `class_names` list in `app.py` to match your training data
- **Image Size**: Modify the preprocessing function in `app.py` if you trained with different image dimensions
- **Model Architecture**: Customize the model in `train.ipynb` for your specific needs

## Requirements

- Python 3.8+
- TensorFlow 2.13+
- Flask 2.3+
- Pillow (PIL)
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook

## License

This project is open source and available under the MIT License.
