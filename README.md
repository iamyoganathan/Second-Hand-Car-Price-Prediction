# 🚗 Second Hand Car Price Prediction

A machine learning web application built with Streamlit that predicts the selling price of used cars based on various features like company, model, year, kilometers driven, fuel type, and location.

## 📋 Project Overview

This project uses a Linear Regression model trained on the Quikr car dataset to predict second-hand car prices in India. The model considers 302 features including one-hot encoded categorical variables for location, fuel type, car models, and companies.

## ✨ Features

- **Interactive Web Interface**: User-friendly Streamlit application
- **Dynamic Car Selection**: Car model dropdown filtered by selected company
- **Multiple Input Parameters**:
  - Car Company (25 brands)
  - Car Model Name (237 models)
  - Year of Purchase (1990-2024)
  - Kilometers Driven
  - Fuel Type (Petrol, Diesel, CNG, LPG, Electric, Hybrid)
  - Location (38 cities across India)
  - Label/Category (PLATINUM, GOLD)
- **Real-time Predictions**: Instant price estimation based on inputs
- **Input Summary**: Detailed view of all entered parameters

## 🛠️ Technology Stack

- **Python 3.13**
- **Streamlit**: Web application framework
- **scikit-learn**: Machine learning model (Linear Regression)
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Pickle**: Model serialization

## 📁 Project Structure

```
.
├── app.py                      # Main Streamlit application
├── CarPricePrediction.pickle   # Trained ML model
├── Quikr_car.csv              # Dataset (1032 records)
├── README.md                   # Project documentation
└── .venv/                      # Virtual environment
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "Project 4 (Second Hand Car Price Prediction)"
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   
   - **Windows (PowerShell)**:
     ```powershell
     .venv\Scripts\Activate.ps1
     ```
   
   - **Windows (Command Prompt)**:
     ```cmd
     .venv\Scripts\activate.bat
     ```
   
   - **macOS/Linux**:
     ```bash
     source .venv/bin/activate
     ```

4. **Install required packages**
   ```bash
   pip install streamlit pandas numpy scikit-learn
   ```

### Running the Application

1. **Start the Streamlit app**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser**
   
   The application will automatically open at `http://localhost:8501`

3. **Use the application**
   - Select the car company
   - Choose the car model from the filtered dropdown
   - Set the year of purchase using the slider
   - Enter kilometers driven
   - Select fuel type and location
   - Choose the label/category
   - Click "Predict Price" to get the estimated price

## 📊 Dataset Information

- **Source**: Quikr Car Listings
- **Records**: 1,032 car listings
- **Features**:
  - Name: Full car model name
  - Company: Car manufacturer
  - Year: Year of purchase
  - Kms_driven: Kilometers driven
  - Fuel_type: Type of fuel
  - Location: City of listing
  - Label: Category (PLATINUM/GOLD)
  - Price: Selling price (target variable)

## 🧠 Model Information

- **Algorithm**: Linear Regression
- **Features**: 302 (after preprocessing)
  - Numeric: Year, Kms_driven
  - Label Encoded: Label (GOLD=0, PLATINUM=1)
  - One-Hot Encoded: Location, Fuel_type, Car Name, Company
- **Training Library**: scikit-learn 1.7.1
- **Model File**: `CarPricePrediction.pickle`

### Feature Categories

| Category | Count | Type |
|----------|-------|------|
| Locations | 38 | One-Hot Encoded |
| Fuel Types | 9 | One-Hot Encoded |
| Car Models | 237 | One-Hot Encoded |
| Companies | 25 | One-Hot Encoded |
| Numeric | 2 | Direct (Year, Kms_driven) |
| Label | 1 | Label Encoded |

## 🎯 Use Cases

- **Buyers**: Estimate fair market value before purchasing
- **Sellers**: Price their cars competitively
- **Dealers**: Quick price assessment for inventory
- **Market Research**: Understand pricing trends

## ⚠️ Known Limitations

- Model trained on Indian car market data (Quikr platform)
- Limited to cars from 1990 onwards
- Price predictions based on historical data
- Model version mismatch warning (trained on sklearn 1.7.1, may run on 1.8.0+)

## 🔮 Future Enhancements

- [ ] Add data visualization (price trends, brand comparison)
- [ ] Implement model retraining pipeline
- [ ] Add more car brands and models
- [ ] Include additional features (owner history, service records)
- [ ] Deploy to cloud platform (Streamlit Cloud, Heroku, AWS)
- [ ] Add price comparison with market averages
- [ ] Implement model performance metrics display

## 📝 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 👨‍💻 Author

Your Name / GitHub Profile

## 🙏 Acknowledgments

- Dataset sourced from Quikr car listings
- Built with Streamlit framework
- Machine learning powered by scikit-learn

---

**Note**: This is a demonstration project for educational purposes. Price predictions should be used as estimates only and verified with market research before making purchasing decisions.
