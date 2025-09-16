from flask import Flask, request, render_template, jsonify
import tensorflow as tf
from PIL import Image
import numpy as np
import os
import io

app = Flask(__name__)

# Load the trained model
model_path = 'models/image_model.h5'
model = None

def load_model():
    global model
    if os.path.exists(model_path):
        model = tf.keras.models.load_model(model_path)
        print("Model loaded successfully!")
    else:
        print(f"Model not found at {model_path}. Please train the model first.")

def preprocess_image(image):
    """Preprocess image for model prediction"""
    # Resize image to 224x224 (standard for many CNN models)
    image = image.resize((224, 224))
    # Convert to RGB if needed
    if image.mode != 'RGB':
        image = image.convert('RGB')
    # Convert to numpy array and normalize
    image_array = np.array(image) / 255.0
    # Add batch dimension
    image_array = np.expand_dims(image_array, axis=0)
    return image_array

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if model is None:
            return jsonify({'error': 'Model not loaded. Please train the model first.'}), 500
        
        # Get uploaded file
        file = request.files['image']
        if file is None:
            return jsonify({'error': 'No image file provided'}), 400
        
        # Read and preprocess image
        image = Image.open(io.BytesIO(file.read()))
        processed_image = preprocess_image(image)
        
        # Make prediction
        prediction = model.predict(processed_image)
        
        # Get class with highest probability
        predicted_class = np.argmax(prediction[0])
        confidence = float(np.max(prediction[0]))
        
        # Define class names (update these based on your training data)
        class_names = ['Class 0', 'Class 1', 'Class 2']  # Update with your actual class names
        
        result = {
            'predicted_class': class_names[predicted_class],
            'confidence': confidence,
            'all_predictions': prediction[0].tolist()
        }
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    load_model()
    app.run(debug=True, host='0.0.0.0', port=5000)
