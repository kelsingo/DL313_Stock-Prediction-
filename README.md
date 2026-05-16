# Stock Prediction

Deep learning project for stock price prediction on both the Nasdaq market and the Vietnam stock market.

The project explores time-series forecasting using neural network models to predict stock prices and technical indicators from historical market data.

---

# Data Sources

#### 1. Nasdaq Dataset
Historical stock data from major Nasdaq-listed companies.

#### 2. Vietnam Stock Market
Historical stock data from the Vietnamese stock market. 

---

# Project Layout

```bash
DL313_Stock-Prediction/
│
├── api/
│   ├── api_tester.py
│   ├── main.py
│
├── app/
│   ├── pb_data
│   ├── pb_public
│   ├── pb_migrations
│
├── nasdaq/
│   ├── datasets/
│   ├── models/
│   ├── 220061-project-notebook.ipynb
│
├── Vietnam-stock-market/
│   ├── 220061-project-notebook-VN.ipynb
│
└── README.md
```

---

# Features

- Stock price forecasting using deep learning
- Nasdaq and Vietnam stock market experiments
- Technical indicator prediction (e.g., RSI)
- Visualization of prediction performance
- Multi-day forecasting analysis
- Jupyter notebook-based workflow

--- 
# Project Deployment
1. Model Deployment

The production model (trained on AAPL) is fully deployed and accessible via a REST API endpoint. It accepts inference requests and returns model predictions.

- Endpoint: [https://dlmdkelsi.cung.io.vn/predict](https://dlmdkelsi.cung.io.vn/predict)

2. SaaS User Interface

Database: ```NVDA.csv``` is stored as structured SQL tables within a Pocketbase database instance.

A dedicated HTML web interface has been built to fetch data from Pocketbase and visualize the model's prediction results at predefined intervals, providing an intuitive dashboard for end-users.

Webpage: [https://dldbkelsi.cung.io.vn](https://dldbkelsi.cung.io.vn)

3. Automation Workflow (In Development)
To fully automate the pipeline from data ingestion to user visualization, the workflow is structured into the following sequential steps:

*Step 1: Data Preparation (Completed)*

The raw market data (NVDA.csv) is ingested, parsed, and stored as structured SQL tables within a Pocketbase database instance.

*Step 2: Realtime Database Update
Update realtime stock data to the database for realtime prediction.  

*Step 3: Automated Feature Engineering & Inference*

A script to pull the latest data from Pocketbase, preprocess it into the required model, and send a batch request to the FastAPI /predict endpoint.


---
# Run Experiments on your own 

## Recommended Environment

This project is best run on Google Colab:

- No local setup is required
- GPU acceleration is available
- Jupyter notebooks are already supported
- Easier dependency management

---

## Run on Google Colab (Recommended)

### 1. Clone the repository

```python
!git clone https://github.com/kelsingo/DL313_Stock-Prediction-.git
%cd DL313_Stock-Prediction-
```

### 2. Load datasets

- For Nasdaq stock prediction: Load all datasets from ```nasdaq/datasets``` to Google Colab. 

- For Vietnam stock prediction: datasets are already loaded using ```vnstock``` library in the notebook. 
### 3. Open notebooks

Run either:

- `nasdaq/220061-project-notebook.ipynb`
- `Vietnam-stock-market/220061-project-notebook-VN.ipynb`

---

## Local Installation (Optional)

### 1. Clone repository

```bash
git clone https://github.com/kelsingo/DL313_Stock-Prediction-.git
cd DL313_Stock-Prediction-
```

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate environment:

#### macOS/Linux

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install pandas numpy matplotlib scikit-learn tensorflow yfinance vnstock
```

---

# Technologies Used

- Python
- TensorFlow / Keras
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- yfinance

---

# Results

The project evaluates prediction quality using:

- Mean Squared Error (MSE)
- Actual vs predicted stock price plots
- RSI prediction comparison

Results show that the LSTM model is robust on the Nasdaq dataset with stable resutl. Conversely, prediction on Vietnam stock market is less stable, and short-term forecasting generally achieves lower prediction error, while longer forecasting windows become more challenging due to market volatility.

---

# Future Improvements

- Transformer-based forecasting models
- Sentiment analysis using financial news
- More technical indicators
- Hyperparameter optimization
- Real-time prediction API deployment

