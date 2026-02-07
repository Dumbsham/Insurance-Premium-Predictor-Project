# 🏥 Insurance Premium Predictor

A machine learning project that predicts insurance premiums based on demographic and health factors using Linear Regression. Includes an interactive Streamlit web application for real-time predictions.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Model Performance](#model-performance)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This project analyzes insurance data to predict premium charges based on various factors such as age, BMI, smoking status, and region. The model achieves strong predictive performance and is deployed as an interactive web application using Streamlit.

### Key Highlights

- **Exploratory Data Analysis (EDA)** with comprehensive visualizations
- **Feature Engineering** including BMI categorization and one-hot encoding
- **Statistical Analysis** using Pearson correlation and Chi-squared tests
- **Linear Regression Model** with R² score optimization
- **Interactive Web App** for real-time premium predictions

## ✨ Features

- 📊 **Data Visualization**: Histograms, box plots, and correlation heatmaps
- 🔧 **Feature Engineering**: Smart encoding and scaling of features
- 📈 **Statistical Testing**: Rigorous feature selection using statistical methods
- 🤖 **Machine Learning**: Trained Linear Regression model
- 🌐 **Web Interface**: User-friendly Streamlit application
- 💾 **Model Persistence**: Saved models for easy deployment

## 📊 Dataset

The dataset contains **1,338 records** with the following features:

| Feature | Description | Type |
|---------|-------------|------|
| `age` | Age of the policyholder | Numerical |
| `sex` | Gender (male/female) | Categorical |
| `bmi` | Body Mass Index | Numerical |
| `children` | Number of dependents | Numerical |
| `smoker` | Smoking status (yes/no) | Categorical |
| `region` | Residential region (northeast, northwest, southeast, southwest) | Categorical |
| `charges` | Insurance premium amount (target variable) | Numerical |

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/insurance-premium-predictor.git
   cd insurance-premium-predictor
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download the dataset**
   - Place `insurance.csv` in the project root directory

## 💻 Usage

### Training the Model

Run the Jupyter notebook or Python script to train the model:

```bash
jupyter notebook insurance.ipynb
# OR
python insurance.py
```

This will:
- Perform exploratory data analysis
- Clean and preprocess the data
- Train the Linear Regression model
- Save `model.pkl` and `scaler.pkl`

### Running the Web Application

Launch the Streamlit app:

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

### Making Predictions

1. Enter your details in the web interface:
   - Age (18-100)
   - Sex (Male/Female)
   - BMI (10.0-60.0)
   - Number of Children (0-10)
   - Smoker Status (Yes/No)
   - Region (Northeast, Northwest, Southeast, Southwest)

2. Click **"Calculate Premium"**

3. View your estimated insurance charge

## 📁 Project Structure

```
insurance-premium-predictor/
│
├── insurance.ipynb          # Jupyter notebook with full analysis
├── insurance.py             # Python script version
├── app.py                   # Streamlit web application
├── insurance.csv            # Dataset (not included in repo)
├── model.pkl                # Trained model (generated)
├── scaler.pkl               # Feature scaler (generated)
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── .gitignore              # Git ignore file
```

## 📈 Model Performance

### Final Model Metrics

| Metric | Value |
|--------|-------|
| **R² Score** | ~0.80 |
| **Adjusted R²** | ~0.79 |
| **RMSE** | ~$6,000 |
| **RMSE as % of Mean** | ~42% |

### Selected Features

The final model uses 8 features selected through statistical analysis:

1. `age` - Standardized age
2. `is_female` - Gender indicator
3. `bmi` - Standardized BMI
4. `children` - Standardized number of children
5. `is_smoker` - Smoking status (strongest predictor)
6. `region_southeast` - Region indicator
7. `region_northwest` - Region indicator
8. `bmi_category_Obese` - BMI category indicator

### Key Insights

- **Smoking status** is the strongest predictor of insurance charges
- **Age** and **BMI** show positive correlation with premiums
- **Region** has moderate impact on pricing
- **Gender** shows minimal effect on charges

## 🛠️ Technologies Used

### Data Analysis & ML
- **pandas** - Data manipulation
- **numpy** - Numerical computing
- **scikit-learn** - Machine learning algorithms
- **scipy** - Statistical analysis

### Visualization
- **matplotlib** - Plotting library
- **seaborn** - Statistical visualizations

### Web Application
- **streamlit** - Interactive web interface

### Others
- **pickle** - Model serialization

## 📦 Requirements

Create a `requirements.txt` file with:

```
numpy==1.24.3
pandas==2.0.3
seaborn==0.12.2
matplotlib==3.7.2
scikit-learn==1.3.0
scipy==1.11.1
streamlit==1.25.0
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

Your Name
- GitHub: [@yourusername](https://github.com/saksham14sharma)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/Dumbsham)

## 🙏 Acknowledgments

- Dataset source: [Kaggle Medical Cost Personal Dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance)
- Inspiration from various machine learning tutorials and courses

## 📧 Contact

For questions or feedback, please reach out via [email](mailto:sakshamnoida37@gmail.com) or open an issue on GitHub.

---

⭐ If you found this project helpful, please consider giving it a star!