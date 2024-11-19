import pickle
import pandas as pd

# Load the model
with open('Models/random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Example feature names used in the model
feature_names = ['Have_IP', 'Have_At', 'URL_Length', 'URL_Depth', 'Redirection',
                 'https_Domain', 'TinyURL', 'Prefix/Suffix', 'DNS_Record', 'Web_Traffic',
                 'Domain_Age', 'Domain_End', 'iFrame', 'Mouse_Over','Right_Click', 'Web_Forwards']

# Function to extract features from a given URL
def extract_features(url):
    # Replace this function with actual feature extraction logic
    # Here we are using dummy values for illustration purposes
    features = {
        'Have_IP': 0,                   # Replace with actual logic
        'Have_At': 0,                   # Replace with actual logic
        'URL_Length': len(url),            # Example logic: length of the URL
        'URL_Depth': url.count('/'),       # Example logic: count of '/' in the URL
        'Redirection': 0,               # Replace with actual logic
        'https_Domain': 1,             # Replace with actual logic
        'TinyURL': 0,                   # Replace with actual logic
        'Prefix/Suffix': 0,                # Replace with actual logic
        'DNS_Record': 1,                   # Replace with actual logic
        'Web_Traffic': 1000,               # Replace with actual logic
        'Domain_Age': 12,                  # Replace with actual logic
        'Domain_End': 24,                  # Replace with actual logic
        'iFrame': 1,                   # Replace with actual logic
        'Mouse_Over': 0,                # Replace with actual logic
        'Right_Click': 0,                # Replace with actual logic
        'Web_Forwards': 1                  # Replace with actual logic
    }
    return features

# Function to preprocess input data
def preprocess_input(data):
    # Convert to DataFrame
    input_df = pd.DataFrame([data])

    # One-hot encode categorical features
    categorical_features = ['Have_IP', 'Have_At', 'Redirection', 'https_Domain', 'TinyURL', 'iFrame', 'Mouse_Over', 'Right_Click']
    input_df = pd.get_dummies(input_df, columns=categorical_features)

    # Ensure the DataFrame has the same columns as the model was trained with
    required_columns = ['Have_IP', 'Have_At', 'URL_Length', 'URL_Depth', 'Redirection',
                 'https_Domain', 'TinyURL', 'Prefix/Suffix', 'DNS_Record', 'Web_Traffic',
                 'Domain_Age', 'Domain_End', 'iFrame', 'Mouse_Over','Right_Click', 'Web_Forwards']

    # Reindex the DataFrame to match the model's training features, filling missing values with 0
    input_df = input_df.reindex(columns=required_columns, fill_value=0)

    return input_df

# Main function to take URL input and make prediction
def predict_url(url):
    # Extract features from the URL
    features = extract_features(url)

    # Preprocess input data
    processed_input = preprocess_input(features)

    # Make prediction
    prediction = model.predict(processed_input)
    result = "Phishing" if prediction[0] == 1 else "Legitimate"

    return result

# Example usage
if __name__ == "__main__":
    # Input URL from the user
    url = input("Enter URL: ")

    # Predict whether the URL is phishing or legitimate
    result = predict_url(url)

    # Print the result
    print(f'The URL is predicted to be: {result}')
