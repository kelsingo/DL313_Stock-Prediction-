import pandas as pd
import requests
import json

# --- CONFIGURATION ---
CSV_FILE = "/opt/s26dl/kelsi/DL313_Stock-Prediction-/nasdaq/datasets/NVDA.csv"
API_URL = "http://cung.io.vn:10012/predict"
# List the columns that need to be divided by 1,000
# COLUMNS_TO_SCALE = ['volume', 'low', 'high', 'close', 'open']


def test_api_with_30_rows():
    try:
        try:
            health = requests.get("https://dlmdkelsi.cung.io.vn/health", timeout=5)
            print(f"Health check: {health.json()}")
        except:
            print("Server is not responding to health check. Is main.py running?")
            return
        # 1. Read first 30 lines
        
        df = pd.read_csv(CSV_FILE, skiprows=range(1, 5978), nrows=50, header=0)
        df.drop(columns=['Date'], inplace=True)  # Drop the Date column
        df. drop(columns=['Adjusted Close'], inplace=True)  
        df.drop(columns=['Volume'], inplace=True)
        
        matrix = df.values.tolist()
        print(f"Original data shape: {df.shape}")

        # 4. Prepare the payload
        # The API expects {"data": [[...], [...]]}
        payload = {"data": matrix}
        print(f"Prepared payload: {payload}")

        print(f"Sending table of shape ({len(matrix)} rows, {len(matrix[0])} columns)...")

        # 5. Send to API
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            print("Successfully received prediction:")
            print(response.json())
        else:
            print(f"Error {response.status_code}: {response.text}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    test_api_with_30_rows()