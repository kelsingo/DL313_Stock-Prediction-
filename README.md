# Stock Prediction

Deep learning project for stock price prediction on both the Nasdaq market and the Vietnam stock market.

The project explores time-series forecasting using neural network models to predict stock prices and technical indicators from historical market data.

---

# Data Sources

## 1. Nasdaq Dataset
Historical stock data from major Nasdaq-listed companies.

## 2. Vietnam Stock Market
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
│   ├── nasdaq.ipynb
│   ├── hose.ipynb
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

# Recommended Environment

This project is best run on Google Colab:

- No local setup is required
- GPU acceleration is available
- Jupyter notebooks are already supported
- Easier dependency management

---

# Run on Google Colab (Recommended)

## 1. Clone the repository

```python
!git clone https://github.com/kelsingo/DL313_Stock-Prediction-.git
%cd DL313_Stock-Prediction-
```

## 2. Load datasets

- For Nasdaq stock prediction: Load all datasets from ```nasdaq/datasets``` to Google Colab. 

- For Vietnam stock prediction: datasets are already loaded using ```vnstock``` library in the notebook. 
## 3. Open notebooks

Run either:

- `nasdaq/220061-project-notebook.ipynb`
- `Vietnam-stock-market/220061-project-notebook-VN.ipynb`

---

# Local Installation (Optional)

## 1. Clone repository

```bash
git clone https://github.com/kelsingo/DL313_Stock-Prediction-.git
cd DL313_Stock-Prediction-
```

## 2. Create virtual environment

```bash
python -m venv venv
```

Activate environment:

### macOS/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

## 3. Install dependencies

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
- Forecast horizon analysis

Results show that short-term forecasting generally achieves lower prediction error, while longer forecasting windows become more challenging due to market volatility.

---

# Future Improvements

- Transformer-based forecasting models
- Sentiment analysis using financial news
- More technical indicators
- Hyperparameter optimization
- Real-time prediction API deployment

