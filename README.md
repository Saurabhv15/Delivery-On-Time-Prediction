# 🚚 Delivery On-Time Prediction ML Project

This project predicts whether a delivery will arrive on time using machine learning. It includes a user-friendly interface built with **Streamlit**, and is fully containerized using **Docker** for consistent deployment across environments.

---

## 📦 Features

- ✅ Predict on-time or delayed delivery
- ⚙️ Built with Python and Streamlit
- 📊 Uses a trained ML model (Logistic Regression / Random Forest etc.)
- 🐳 Dockerized for easy deployment
- 🧠 Trained on real-world-like delivery dataset

---

## 🧠 Tech Stack

- Python 3.11
- Pandas, NumPy, Scikit-learn
- Streamlit
- Docker

---

## 📁 Project Structure

```
Delivery_On_Time_Prediction_ML_Project/
│
├── Delivery_api/
│   ├── app.py                  # Streamlit app interface
│   ├── model.pkl               # Trained ML model
│   ├── requirements.txt        # Python dependencies
│
├── predictor.py            # Prediction logic
├── Dockerfile                  # Docker configuration
├── README.md                   # Project documentation
```

---

## 🚀 Getting Started

### ✅ 1. Clone the Repository

```bash
git clone https://github.com/Saurabhv15/Delivery-On-Time-Prediction.git
cd Delivery_On_Time_Prediction_ML_Project
```

### 🐳 2. Build Docker Image

Make sure Docker Desktop is installed and running:

```bash
docker build -t delivery-predictor .
```

### ▶️ 3. Run the Docker Container

```bash
docker run -p 8501:8501 delivery-predictor
```

Then open your browser and visit:

```
http://localhost:8501
```

---

## 📋 Input Features

The model expects the following inputs from the user:

- 📦 Shipping Mode (e.g., Standard Class, First Class)
- 🗂️ Product Category (e.g., Furniture, Technology)
- 📏 Delivery Distance
- 📆 Order and Delivery Dates
- 🌍 Delivery Region or Location

---

## 📝 Requirements File Example

Sample `requirements.txt` (inside `Delivery_api/` folder):

```
streamlit
pandas
numpy
scikit-learn
joblib
```

---

## 🔧 Dockerfile Example

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r Delivery_api/requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "Delivery_api/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

---

## 📸 Output

Here is a screenshot of the model in action:

<img width="899" height="889" alt="Screenshot 2025-07-26 143629" src="https://github.com/user-attachments/assets/5ee03108-152f-4be3-aed8-2182bd4c4ff1" />



---
## 👨‍💻 Author

**Saurabh Verma**  
M.Tech (Operations Research) | B.Tech (IT) | AI/ML | Data Science | NLP | Computer Vision  
📫 saurabhvrm959@gmail.com 

---

## 📄 License

MIT License

---

## 🌐 Useful Links

- [Docker Installation](https://docs.docker.com/get-docker/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Python Official Site](https://www.python.org/)
