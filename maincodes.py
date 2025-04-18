import streamlit as st
import numpy as np
import pickle
import joblib
from  tensorflow.keras.models import load_model

import   streamlit  as st; from PIL import Image; import numpy  as np
import pandas  as pd; import pickle

import os

filename1 = 'https://raw.githubusercontent.com/imsb1371/ZCAprediction/refs/heads/main/Capture1.PNG'
filename2 = 'https://raw.githubusercontent.com/imsb1371/ZCAprediction/refs/heads/main/Capture2.PNG'

st.title('Predicting Zinc, Cadmium, and Arsenic Levels in European Soils')
with st.container():
    st.image(filename1)
    st.image(filename2)

st.title('Predicting Zinc, Cadmium, and Arsenic Levels in European Soils')

# Helper function for min-max normalization to [-1, 1]
def normalize(value, min_val, max_val):
    return (2 * (value - min_val) / (max_val - min_val)) - 1

# --- New 30 Input Features with Min-Max Ranges ---
feature_info = [
    ("Albite", 0, 23),
    ("Anorthite", 0, 13.7),
    ("Chalcopyrite", 0, 1.8),
    ("Chlorite", 0, 27.2),
    ("Goethite", 0, 27.3),
    ("Gypsum", 0, 3),
    ("Jarosite", 0, 19.4),
    ("Muscovite", 0, 22.3),
    ("Pyrite", 0, 5.5),
    ("Quartz", 18.3, 66.4),
    ("AtomicVolume", 8.098176455, 117.4560158),
    ("AtomicWeight", 6.941, 238.02891),
    ("BoilingT", 887, 5093),
    ("CovalentRadius", 96, 244),
    ("Density", 535, 19050),
    ("ElectronAffinity", 0, 125.6),
    ("Electronegativity", 0.79, 2.33),
    ("FirstIonizationEnergy", 3.893905, 9.7886),
    ("FusionEnthalpy", 2.09, 37.48),
    ("HeatCapacityMass", 0.116, 3.582),
    ("HeatCapacityMolar", 16.443, 32.21),
    ("HeatFusion", 2.09, 37.48),
    ("MendeleevNumber", 1, 86),
    ("NdUnfilled", 0, 9),
    ("NfValence", 0, 14),
    ("Number", 3, 92),
    ("NUnfilled", 0, 22),
    ("NValence", 1, 29),
    ("total concentration", 0.06, 246000),
    ("Extract Step", 1, 6)
]

st.subheader("Mineral and Element Properties (New Inputs)")
new_inputs = []
normalized_new = []

for i in range(0, len(feature_info), 3):
    cols = st.columns(3)
    for j in range(3):
        if i + j < len(feature_info):
            name, min_val, max_val = feature_info[i + j]
            with cols[j]:
                val = st.number_input(f"{name}", min_value=float(min_val), max_value=float(max_val), value=float(min_val))
                new_inputs.append(val)
                normalized_new.append(normalize(val, min_val, max_val))


# Check for zeros
zero_count = sum(1 for value in normalized_new if value == 0)



# Load models and predict the outputs when the button is pressed
if st.button('Run'):

     ## Validation: If more than 3 inputs are zero, show a warning message
    if zero_count > 3:
        st.error(f"Error: More than three input values are zero. Please provide valid inputs for at least 15 features.")
    else:

        ## load model
        model2 = joblib.load('mybest.pkl')
        output = model2.predict(normalized_new)
        col19, col20, col21 = st.columns(3)
        # Display predictions
        with col19:
            st.write("Morphological fractions", np.round(abs(output), decimals=4))


filename7 = 'https://raw.githubusercontent.com/imsb1371/ZCAprediction/refs/heads/main/Capture3.PNG'
filename8 = 'https://raw.githubusercontent.com/imsb1371/ZCAprediction/refs/heads/main/Capture4.PNG'

col22, col23 = st.columns(2)
with col22:
    with st.container():
        st.markdown("<h5>Developer:</h5>", unsafe_allow_html=True)
        st.image(filename8)

with col23:
    with st.container():
        st.markdown("<h5>Supervisor:</h5>", unsafe_allow_html=True)
        st.image(filename7) 


footer = """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        color: black;
        text-align: center;
        padding: 10px;
        font-size: 12px;
    }
    </style>
    <div class="footer">
    This web app was developed in School of Resources and Safety Engineering, Central South University, Changsha 410083, China
    </div>
"""
st.markdown(footer, unsafe_allow_html=True)









