import streamlit as st
from PIL import Image
import numpy as np

# Set page config
st.set_page_config(
    page_title="Smart Agro - AI",
    page_icon="🌾",
    layout="centered"
)

# Custom CSS for fonts and colors
st.markdown("""
<style>
/* Title style */
h1 {
    color: #2E8B57;
    font-family: 'Arial Black', Gadget, sans-serif;
    font-size: 48px;
}

/* Subtitle style */
h3 {
    color: #3CB371;
    font-family: 'Verdana', sans-serif;
    font-size: 24px;
}

/* Info box style */
.stAlert > div {
    background-color: #E0F7FA;
    color: #00796B;
    font-family: 'Calibri', sans-serif;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# Title and subtitle
st.markdown("<h1>🌾 Smart Agro - AI</h1>", unsafe_allow_html=True)
st.markdown("<h3>Automated Fertilizer and Disease Detection System for Paddy Crop</h3>", unsafe_allow_html=True)
st.markdown("<hr style='border:2px solid #3CB371'>", unsafe_allow_html=True)
st.markdown("Upload an image of a rice leaf and get instant **disease detection** along with **fertilizer recommendations**.", unsafe_allow_html=True)

# Dummy disease prediction function
def predict_disease(img_array):
    green_mean = np.mean(img_array[:, :, 1])
    if green_mean < 80:
        return 'Bacterial_Leaf_Blight'
    elif green_mean < 150:
        return 'Brown_Spot'
    elif green_mean < 180:
        return 'Leaf_Smut'
    elif green_mean < 200:
        return 'Tungro'
    else:
        return 'Healthy_Leaf'

# Fertilizer recommendations
fertilizer_recommendations = {
    'Bacterial_Leaf_Blight': (
        "💧 Water management: Avoid excessive irrigation.\n"
        "💊 Fungicide: Use Copper-based fungicides or Streptomycin sprays.\n"
        "🌱 Fertilizer: Balanced NPK; avoid excess nitrogen.\n"
        "🧹 Field sanitation: Remove infected leaves."
    ),
    'Brown_Spot': (
        "💊 Fungicide: Apply Mancozeb or Copper Oxychloride.\n"
        "🌱 Fertilizer: Use Potassium-rich fertilizers (K2O).\n"
        "⚖️ Avoid excess nitrogen.\n"
        "🧹 Remove infected residues."
    ),
    'Leaf_Smut': (
        "💊 Fungicide: Systemic fungicides like Propiconazole or Carbendazim.\n"
        "🌱 Fertilizer: Balanced NPK, slightly higher Potassium.\n"
        "🌾 Crop rotation: Avoid continuous planting.\n"
        "🧹 Maintain proper spacing."
    ),
    'Tungro': (
        "🦟 Control leafhopper vector using insecticides.\n"
        "🌱 Balanced NPK; Zinc application improves tolerance.\n"
        "🧹 Remove diseased plants.\n"
        "💧 Avoid excessive water logging."
    ),
    'Healthy_Leaf': (
        "✅ Plant is healthy.\n"
        "🌱 Maintain balanced NPK fertilization.\n"
        "💧 Proper irrigation.\n"
        "🧹 Regular monitoring to prevent disease."
    )
}

# Upload image
uploaded_file = st.file_uploader("📂 Upload a rice leaf image", type=["jpg","jpeg","png"])
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption='Uploaded Image', use_column_width=True)

    # Preprocess image
    img_array = np.array(img.resize((256, 256)))

    # Predict disease
    with st.spinner("🔍 Detecting disease..."):
        predicted_class = predict_disease(img_array)

    # Display result with colors
    st.markdown(f"<h3 style='color:#FF4500;'>Predicted Disease: {predicted_class}</h3>", unsafe_allow_html=True)

    # Display fertilizer recommendations in a styled info box
    st.info(fertilizer_recommendations[predicted_class])

    st.markdown("<hr style='border:1px solid #3CB371'>", unsafe_allow_html=True)
    st.markdown("💡 **Tip:** Maintain proper irrigation, balanced fertilizers, and monitor regularly.", unsafe_allow_html=True)