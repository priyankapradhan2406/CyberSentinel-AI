🛡️ CyberSentinel AI

Intelligent Network Threat Detection Using Machine Learning

<p align="center">
  <b>AI-Powered Network Traffic Classification</b>
</p>🌐 Live Demo

🚀 Try the live application:

"Launch CyberSentinel AI" (PASTE_YOUR_STREAMLIT_APP_URL_HERE)

Explore the interactive dashboard and upload a sample NSL-KDD dataset to see machine-learning predictions.

---

📌 About the Project

CyberSentinel AI is a machine-learning-based network traffic classification system designed to identify normal and potentially suspicious network activity.

The project uses a Random Forest classification algorithm to analyse network traffic records and classify them into two categories: Normal and Suspicious.

✨ Key Features

- AI-powered network traffic classification
- Random Forest machine learning model
- Normal and suspicious traffic detection
- CSV dataset upload
- Interactive Streamlit dashboard
- Real-time prediction after dataset upload
- Traffic statistics and visualizations
- Prediction details

🧰 Technologies Used

Technology| Purpose
Python| Programming language
Pandas| Data processing
NumPy| Numerical operations
Scikit-learn| Machine learning
Random Forest| Classification algorithm
Streamlit| Web dashboard
Joblib| Model saving and loading
GitHub| Version control

🧠 Machine Learning Model

Algorithm: Random Forest Classifier

Dataset: NSL-KDD

Classification:

- Normal Traffic
- Suspicious Traffic

The model was trained using labelled network traffic records and evaluated using a test dataset.

📊 Sample Project Results

Example analysis from the uploaded 200-record sample:

Metric| Result
Total Records| 200
Normal Traffic| 105
Suspicious Traffic| 95

These are predictions on the sample dataset, not verified real-world attack detections.

📂 Project Structure

CyberSentinel-AI/
│
├── app (1).py
├── requirements.txt
├── cybersentinel_model.pkl
├── sample_network_traffic.csv
└── README.md

⚙️ Installation and Setup

Clone the repository:

git clone https://github.com/priyankapradhan2406/CyberSentinel-AI.git

Move into the project folder:

cd CyberSentinel-AI

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run "app (1).py"

📸 Dashboard Preview

The application provides:

- Network traffic dataset upload
- Total records analysed
- Normal traffic count
- Suspicious traffic count
- Traffic classification chart
- Prediction details

Add your dashboard screenshots here in the future.

🎯 Project Objectives

- Explore machine learning applications in cybersecurity.
- Understand network traffic classification.
- Build an interactive AI-powered dashboard.
- Demonstrate how labelled network data can be analysed using machine learning.

🔮 Future Enhancements

- Multi-class attack classification
- More advanced machine learning algorithms
- Improved model evaluation
- Live network traffic monitoring in a controlled test environment
- Enhanced dashboard analytics

⚠️ Disclaimer

CyberSentinel AI is an educational prototype built using the public NSL-KDD benchmark dataset. Its predictions are not proof of actual cyberattacks and should not be used as a standalone security solution.

👩‍💻 Developer

Priyanka Pradhan

Computer Science Student

GitHub: "priyankapradhan2406" (https://github.com/priyankapradhan2406)

---

⭐ If you find this project interesting, feel free to explore the repository and try the live demo!