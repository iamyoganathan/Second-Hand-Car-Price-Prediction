import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Page config
st.set_page_config(page_title="Car Price Prediction", page_icon="🚗")

# Load model and data
@st.cache_resource
def load_model():
    return pickle.load(open("CarPricePrediction.pickle", "rb"))

@st.cache_data
def load_data():
    df = pd.read_csv("Quikr_car.csv")
    return df

model = load_model()
df = load_data()

# Get unique values from the dataset
companies = sorted(df['Company'].dropna().unique().tolist())
locations = sorted(df['Location'].dropna().unique().tolist())
fuel_types = sorted(df['Fuel_type'].dropna().unique().tolist())
labels = sorted(df['Label'].dropna().unique().tolist())

# Get car names grouped by company
car_names_by_company = {}
for company in companies:
    names = df[df['Company'] == company]['Name'].dropna().unique().tolist()
    car_names_by_company[company] = sorted(names)

st.title("🚗 Car Price Prediction App")
st.markdown("Predict the **selling price of a car** using Machine Learning")

st.divider()

# Input fields in columns
col1, col2 = st.columns(2)

with col1:
    company = st.selectbox("Car Company", companies)
    
    # Filter car names by selected company
    available_names = car_names_by_company.get(company, [])
    if available_names:
        name = st.selectbox("Car Model Name", available_names)
    else:
        name = st.text_input("Car Model Name (manual entry)")
    
    year = st.slider("Year of Purchase", 1990, 2024, 2015)

with col2:
    kms_driven = st.number_input("Kilometers Driven", min_value=0, max_value=500000, value=50000, step=1000)
    fuel_type = st.selectbox("Fuel Type", fuel_types)
    location = st.selectbox("Location", locations)
    label = st.selectbox("Label/Category", labels)

# Predict button
if st.button("Predict Price", type="primary"):
    # Create a dataframe with all features initialized to 0
    feature_names = model.feature_names_in_
    input_data = pd.DataFrame(0, index=[0], columns=feature_names)
    
    # Set numeric features
    input_data['Year'] = year
    input_data['Kms_driven'] = kms_driven
    
    # Set Label (label encoded: GOLD=0, PLATINUM=1)
    label_encoding = {'GOLD': 0, 'PLATINUM': 1}
    input_data['Label'] = label_encoding.get(label, 0)
    
    # Set categorical features (one-hot encoded)
    # Location
    if location in feature_names:
        input_data[location] = 1
    
    # Fuel type
    if fuel_type in feature_names:
        input_data[fuel_type] = 1
    
    # Car name (try to find matching name in features)
    # First try exact match
    if name in feature_names:
        input_data[name] = 1
    else:
        # Try to find partial match (car names might be shortened)
        matching_names = [f for f in feature_names if name.split(' ')[0] in f and company in f]
        if matching_names:
            input_data[matching_names[0]] = 1
    
    # Company
    if company in feature_names:
        input_data[company] = 1
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    
    st.success(f"💰 Estimated Car Price: ₹ {prediction:,.2f}")
    
    # Display input summary
    with st.expander("View Input Details"):
        st.write(f"**Company:** {company}")
        st.write(f"**Model:** {name}")
        st.write(f"**Year:** {year}")
        st.write(f"**Kilometers Driven:** {kms_driven:,}")
        st.write(f"**Fuel Type:** {fuel_type}")
        st.write(f"**Location:** {location}")
        st.write(f"**Label:** {label}")

