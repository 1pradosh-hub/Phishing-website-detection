import tkinter as tk
from tkinter import messagebox
import pickle
import pandas as pd

# Load the model
with open('Models/random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Example feature names used in the model
feature_names = [
    'Have_IP', 'Have_At', 'URL_Length', 'URL_Depth', 'Redirection',
    'https_Domain', 'TinyURL', 'Prefix/Suffix', 'DNS_Record', 'Web_Traffic',
    'Domain_Age', 'Domain_End', 'iFrame', 'Mouse_Over', 'Right_Click', 'Web_Forwards'
]

# Function to extract features from a given URL
def extract_features(url):
    # Replace this with actual feature extraction logic
    features = {
        'Have_IP': 0,                   # Replace with actual logic
        'Have_At': 0,                   # Replace with actual logic
        'URL_Length': len(url),         # Example logic: length of the URL
        'URL_Depth': url.count('/'),    # Example logic: count of '/' in the URL
        'Redirection': 0,               # Replace with actual logic
        'https_Domain': 1,              # Replace with actual logic
        'TinyURL': 0,                   # Replace with actual logic
        'Prefix/Suffix': 0,             # Replace with actual logic
        'DNS_Record': 1,                # Replace with actual logic
        'Web_Traffic': 1000,            # Replace with actual logic
        'Domain_Age': 12,               # Replace with actual logic
        'Domain_End': 24,               # Replace with actual logic
        'iFrame': 1,                    # Replace with actual logic
        'Mouse_Over': 0,                # Replace with actual logic
        'Right_Click': 0,               # Replace with actual logic
        'Web_Forwards': 1               # Replace with actual logic
    }
    return features

# Function to preprocess input data
def preprocess_input(data):
    # Convert to DataFrame
    input_df = pd.DataFrame([data])

    # One-hot encode categorical features
    categorical_features = [
        'Have_IP', 'Have_At', 'Redirection', 'https_Domain', 'TinyURL', 'iFrame', 'Mouse_Over', 'Right_Click'
    ]
    input_df = pd.get_dummies(input_df, columns=categorical_features)

    # Ensure the DataFrame has the same columns as the model was trained with
    input_df = input_df.reindex(columns=feature_names, fill_value=0)

    return input_df

# Function to take URL input and make prediction
def predict_url(url):
    # Extract features from the URL
    features = extract_features(url)

    # Preprocess input data
    processed_input = preprocess_input(features)

    # Make prediction
    prediction = model.predict(processed_input)
    result = "Phishing" if prediction[0] == 1 else "Legitimate"

    return result

# Tkinter GUI setup
def check_url():
    url = url_entry.get()
    result = predict_url(url)
    messagebox.showinfo("Detection Result", f"The URL is predicted to be: {result}")

# Set up the Tkinter window
root = tk.Tk()
root.title("Phishing Detection System")

# URL input label and entry
tk.Label(root, text="Enter URL:").pack(pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Check button
check_button = tk.Button(root, text="Check URL", command=check_url)
check_button.pack(pady=20)

# Run the GUI loop
root.mainloop()
