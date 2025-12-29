# Student ML API

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Deployed on Render](https://img.shields.io/badge/deployed-Render-46E3B7.svg)](https://student-ml-api-4z9d.onrender.com)

> A production-ready machine learning API that predicts student performance (Pass/Fail) based on study hours, attendance, and previous scores. Built with Flask, scikit-learn, and deployed on Render with both REST API and web interface.

**🔗 Live API:** [https://student-ml-api-4z9d.onrender.com](https://student-ml-api-4z9d.onrender.com)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Quick Start](#quick-start)
- [API Documentation](#api-documentation)
- [Web Interface](#web-interface)
- [Project Structure](#project-structure)
- [Model Details](#model-details)
- [Local Development](#local-development)
- [Deployment](#deployment)
- [Testing](#testing)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

This project demonstrates a complete machine learning workflow from data exploration to production deployment. The API predicts whether a student will pass or fail based on three key factors: hours studied, attendance percentage, and previous exam scores.

**Tech Stack:**
- **Machine Learning**: scikit-learn (Random Forest Classifier)
- **Backend**: Flask (Python web framework)
- **Deployment**: Render (cloud platform)
- **Model Serialization**: joblib

**Use Cases:**
- Learning end-to-end ML deployment
- Portfolio demonstration for data science roles
- Template for productionizing classification models
- Reference implementation for Flask-based ML APIs

---

## ✨ Features

- ✅ **Dual Interface** — REST API + Web form for predictions
- ✅ **Optimized Model** — Random Forest with 200 estimators, 75% accuracy
- ✅ **Robust API** — Input validation and error handling
- ✅ **Production Ready** — Deployed and accessible via HTTPS
- ✅ **Clean Architecture** — Separation of concerns (model, API, templates)
- ✅ **Complete ML Pipeline** — Data exploration to deployment
- ✅ **Reproducible** — Pinned dependencies and random state

---

## 🚀 Quick Start

### Test the Live API

**Using cURL (JSON API):**
```bash
# Make a prediction via REST API
curl -X POST https://student-ml-api-4z9d.onrender.com/predict \
  -H "Content-Type: application/json" \
  -d '{
    "hours_studied": 7,
    "attendance": 85,
    "previous_score": 72
  }'

# Expected response: {"result": 1}  (1 = Pass, 0 = Fail)
```

**Using the Web Interface:**
Simply visit [https://student-ml-api-4z9d.onrender.com](https://student-ml-api-4z9d.onrender.com) and fill out the form!

### Run Locally

```bash
# Clone the repository
git clone https://github.com/TechGenDM/student-ml-api.git
cd student-ml-api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the server
python app.py
```

The application will be available at `http://127.0.0.1:8000`

---

## 📚 API Documentation

### Base URLs
```
Production: https://student-ml-api-9qkf.onrender.com
Local: http://127.0.0.1:8000
```

### Endpoints

#### `GET /`
Returns the web interface for predictions.

**Response:** HTML form

---

#### `POST /predict`
Generate predictions via JSON API.

**Request:**
```json
{
  "hours_studied": 7,
  "attendance": 85,
  "previous_score": 72
}
```

**Response (Success - 200):**
```json
{
  "result": 1
}
```
- `result`: Integer (0 = Fail, 1 = Pass)

**Response (Error - 400):**
```json
{
  "error": "hours_studied is missing"
}
```

**Required Fields:**
- `hours_studied` (float): Hours spent studying (e.g., 1-10)
- `attendance` (float): Attendance percentage (e.g., 50-100)
- `previous_score` (float): Previous exam score (e.g., 30-90)

**Status Codes:**
- `200` — Success
- `400` — Invalid input (missing fields or invalid JSON)

---

#### `POST /predict-form`
Form-based prediction endpoint (used by web interface).

**Form Data:**
- `hours_studied`
- `attendance`
- `previous_score`

**Response:** HTML page with prediction result

---

## 🌐 Web Interface

The application includes a user-friendly web form for non-technical users:

1. Navigate to the home page (`/`)
2. Enter the three required values:
   - Hours Studied
   - Attendance (%)
   - Previous Score
3. Click "Predict"
4. View the result (Pass/Fail) on the page

Perfect for demonstrations, non-technical stakeholders, or quick manual tests!

---

## 📁 Project Structure

```
student-ml-api/
├── app.py                    # Flask application & API endpoints
├── student_model.pkl         # Serialized trained Random Forest model
├── ML_End_to_End.ipynb      # Complete ML training pipeline
├── requirements.txt          # Python dependencies
├── students.csv             # Training dataset (20 samples)
├── templates/
│   └── index.html           # Web form interface
└── README.md                # Project documentation
```

### Key Files

- **`app.py`** — Main Flask application with three routes:
  - `/` - Serves the web form
  - `/predict` - JSON API endpoint
  - `/predict-form` - Form submission handler

- **`ML_End_to_End.ipynb`** — Complete ML workflow:
  - Data exploration and statistics
  - Train/test split (80/20)
  - Model comparison (Logistic Regression vs Random Forest)
  - Hyperparameter tuning (n_estimators=200, max_depth=5)
  - Evaluation metrics (accuracy, precision, recall, F1-score)
  - Model serialization with joblib

- **`student_model.pkl`** — Trained Random Forest classifier ready for inference

- **`templates/index.html`** — Clean HTML form for web-based predictions

---

## 🤖 Model Details

**Algorithm:** Random Forest Classifier

**Hyperparameters:**
- `n_estimators`: 200 (number of decision trees)
- `max_depth`: 5 (maximum tree depth)
- `min_samples_split`: 4 (minimum samples to split node)
- `random_state`: 42 (reproducibility)

**Features:**
1. Hours Studied (1-10)
2. Attendance Percentage (50-96)
3. Previous Score (30-90)

**Target:**
- 0 = Fail
- 1 = Pass

**Performance:**
- **Accuracy**: 75% on test set
- **Precision**: 100% (no false positives)
- **Recall**: 50% (misses some pass cases)
- **F1-Score**: 0.67

**Training Data:**
- 20 samples total
- 16 training, 4 test samples
- Balanced classes (55% pass rate)

**Model Comparison:**
Both Logistic Regression and Random Forest achieved 75% accuracy. Random Forest was selected for its ability to capture non-linear relationships and better generalization potential with more data.

---

## 💻 Local Development

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Virtual environment tool (venv recommended)

### Setup Instructions

1. **Clone and navigate:**
   ```bash
   git clone https://github.com/TechGenDM/student-ml-api.git
   cd student-ml-api
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   
   Dependencies:
   - `flask` — Web framework
   - `numpy` — Numerical computing
   - `joblib` — Model serialization
   - `scikit-learn` — Machine learning library

4. **Verify model file exists:**
   ```bash
   ls student_model.pkl  # Should exist in root directory
   ```

5. **Start the server:**
   ```bash
   python app.py
   ```
   
   Server starts on port 8000 with debug mode enabled.

6. **Test the API:**
   ```bash
   # Test web interface
   open http://127.0.0.1:8000  # or visit in browser
   
   # Test JSON API
   curl -X POST http://127.0.0.1:8000/predict \
     -H "Content-Type: application/json" \
     -d '{"hours_studied": 8, "attendance": 90, "previous_score": 75}'
   ```

### Retraining the Model

1. Open `ML_End_to_End.ipynb` in Jupyter Notebook
2. Modify hyperparameters or add more data
3. Run all cells to retrain
4. The last cell exports the new model: `joblib.dump(rf, "student_model.pkl")`
5. Restart `app.py` to load the updated model

---

## 🌐 Deployment

The API is deployed on **Render** with automatic deployments from the main branch.

**Deployment URL:** [https://student-ml-api-9qkf.onrender.com](https://student-ml-api-9qkf.onrender.com)

### Deploy Your Own Instance

1. **Fork this repository** to your GitHub account

2. **Create a Render account** at [render.com](https://render.com)

3. **Create a new Web Service:**
   - Connect your forked repository
   - Runtime: Python 3
   - Build command: `pip install -r requirements.txt`
   - Start command: `python app.py`

4. **Environment variables** (optional):
   - `PORT`: Automatically set by Render
   - Add any custom variables if needed

5. **Deploy** and access via the provided Render URL

### Production Checklist

- ✅ `requirements.txt` with all dependencies
- ✅ `student_model.pkl` in repository root
- ✅ `app.py` configured for `0.0.0.0` host
- ✅ `templates/` folder with `index.html`
- ✅ Error handling for all endpoints
- ⚠️ Consider disabling debug mode in production (currently enabled)

---

## 🧪 Testing

### Manual Testing

**Test Web Interface:**
```bash
# Open in browser
http://127.0.0.1:8000

# Enter values like:
# Hours Studied: 8
# Attendance: 85
# Previous Score: 70
```

**Test JSON API with valid data:**
```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"hours_studied": 7, "attendance": 85, "previous_score": 72}'

# Expected: {"result": 1}
```

**Test with missing fields (should return 400):**
```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"hours_studied": 7}'

# Expected: {"error": "attendance is missing"}
```

**Test with invalid JSON (should return 400):**
```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d 'not json'

# Expected: {"error": "Request body must be JSON"}
```

### Test Cases Coverage

- ✅ Model loads successfully on startup
- ✅ Valid predictions return 0 or 1
- ✅ Missing fields return appropriate error messages
- ✅ Invalid JSON returns 400 error
- ✅ Non-numeric values are rejected
- ✅ Web form renders correctly
- ✅ Form submission returns result page

### Recommended Automated Tests

Create `test_app.py`:
```python
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_page(client):
    rv = client.get('/')
    assert rv.status_code == 200

def test_valid_prediction(client):
    rv = client.post('/predict', json={
        'hours_studied': 7,
        'attendance': 85,
        'previous_score': 72
    })
    assert rv.status_code == 200
    assert 'result' in rv.json

def test_missing_field(client):
    rv = client.post('/predict', json={'hours_studied': 7})
    assert rv.status_code == 400
    assert 'error' in rv.json
```

---

## 🚧 Future Enhancements

### Model Improvements
- [ ] Collect more training data (currently only 20 samples)
- [ ] Add feature engineering (interaction terms, polynomial features)
- [ ] Experiment with other algorithms (XGBoost, Neural Networks)
- [ ] Implement cross-validation for better evaluation
- [ ] Add confidence scores to predictions

### API Enhancements
- [ ] **Authentication** — API keys or JWT tokens
- [ ] **Rate Limiting** — Prevent abuse with throttling
- [ ] **Batch Predictions** — Process multiple students at once
- [ ] **Input Validation** — Use Pydantic for robust schema validation
- [ ] **Swagger/OpenAPI** — Interactive API documentation
- [ ] **CORS Support** — Allow frontend applications to consume API

### MLOps & Production
- [ ] **Model Versioning** — Track and serve multiple model versions
- [ ] **Monitoring** — Log predictions and track model drift
- [ ] **A/B Testing** — Compare model performance in production
- [ ] **CI/CD Pipeline** — Automated testing with GitHub Actions
- [ ] **Docker Support** — Containerize for easier deployment
- [ ] **Database Integration** — Store predictions and feedback
- [ ] **Model Retraining** — Automated pipeline for retraining with new data

### User Experience
- [ ] Improve web interface styling (Bootstrap, Tailwind CSS)
- [ ] Add data visualization (feature importance, prediction confidence)
- [ ] Provide explanations for predictions (SHAP values, LIME)
- [ ] Mobile-responsive design
- [ ] Multi-language support

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Make your changes**
4. **Add tests** if applicable
5. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
6. **Push to the branch** (`git push origin feature/AmazingFeature`)
7. **Open a Pull Request**

### Contribution Ideas
- Improve model accuracy
- Add more comprehensive tests
- Enhance documentation
- Optimize API performance
- Add new features from the enhancement list

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🔗 Links & Resources

- **Repository:** [github.com/TechGenDM/student-ml-api](https://github.com/TechGenDM/student-ml-api)
- **Live API:** [student-ml-api-9qkf.onrender.com](https://student-ml-api-9qkf.onrender.com)
- **ML Notebook:** See `ML_End_to_End.ipynb` for training details

### Learning Resources
- [Flask Documentation](https://flask.palletsprojects.com/)
- [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [Random Forest Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)
- [Render Deployment Guide](https://render.com/docs)

---

## 📧 Contact

For questions, feedback, or collaboration opportunities, please open an issue on GitHub or reach out via LinkedIn.

---

<p align="center">
  <strong>Built with ❤️ by <a href="https://github.com/TechGenDM">TechGenDM</a></strong><br>
  <em>From Jupyter notebooks to production — one commit at a time</em>
</p>