import streamlit as st
import numpy as np
import cv2
from tensorflow.keras.models import load_model

# Define your classes list
classes=["Aloevera", "Amla", "Amruta_Balli", "Arali", "Ashoka","Ashwagandha","Avacado","Bamboo","Basale","Betel", "Betel_Nut", "Brahmi", "Castor", "Curry_Leaf", "Doddapatre", "Ekka","Ganike", "Gauva", "Geranium", "Henna", "Hibiscus", "Honge", "Insulin", "Jasmine","Lemon","Lemon_grass","Mango","Mint","Nagadali","Neem","Nithyapushpa","Nooni","Pappaya","Pepper","Pomegranate","Raktachandini","Rose","Sapota","Tulasi","Wood_sorel"]


# Load your pre-trained model
model = load_model('mobilenet_model.h5')

# Prediction function
def predict_image_with_confidence(image, confidence_threshold=0.6):
    img = cv2.resize(image, (224, 224))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    predictions = model.predict(img)
    predicted_confidence = np.max(predictions)
    if predicted_confidence > confidence_threshold:
        predicted_class = classes[np.argmax(predictions)]
        return f"Predicted class: {predicted_class} with confidence: {predicted_confidence:.2f}"
    else:
        return "Prediction confidence is too low. Unable to classify image."

# Streamlit UI
st.title('Medicinal Plant Detection')

uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_image is not None:
    # Convert the file to an opencv image.
    file_bytes = np.asarray(bytearray(uploaded_image.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)

    # Display the uploaded image
    st.image(opencv_image, channels="BGR", caption="Uploaded Image")

    # Predict and display the result
    result = predict_image_with_confidence(opencv_image)
    st.write(result)
