import streamlit as st
import numpy as np
import pickle

with open("Iris_model.pkl", 'rb') as f:
    model = pickle.load(f)

st.title("Iris Flower Prediction")

sepal_length = st.slider("Sepla length(cm)",4.0, 8.0 )
sepal_width = st.slider("Sepla width(cm)",4.0, 8.0 )
petal_length = st.slider("petal length(cm)",4.0, 8.0 )
petal_width = st.slider("petal width(cm)",4.0, 8.0 )

if st.button("prediction"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)
    species = ['setosa', 'Versicolor', 'Virginica']
    st.success(f"Prediction Iris Specis: {species[prediction[0]]}")