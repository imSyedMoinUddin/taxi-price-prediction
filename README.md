# 🚕 Taxi Price Prediction Model  

Welcome to the **Taxi Price Prediction Model** repository! This project features a machine learning model designed to predict taxi fares based on various input features. The model has been deployed using Flask, providing a simple web interface for users to make predictions.  

## 🎯 Features  
The model predicts taxi fares with **84% accuracy on testing data**, based on the following input features:  

1. **Trip Distance (km)**  
2. **Time of Day**  
3. **Day of Week**  
4. **Passenger Count**  
5. **Traffic Conditions**  
6. **Weather**  
7. **Base Fare ($)**  
8. **Per Km Rate ($)**  
9. **Per Minute Rate ($)**  
10. **Trip Duration (minutes)**  

## 🚀 Getting Started  

### Prerequisites  
Ensure you have the following installed:  
- Python 3.8 or later  
- Required Python libraries (listed in `requirements.txt`)  

### Installation  
1. **Clone the Repository**:  
   ```bash  
   git clone https://github.com/imSyedMoinUddin/taxi-price-prediction.git  
   cd taxi-price-prediction  
   ```  

2. **Install Dependencies**:  
   Install all necessary Python libraries:  
   ```bash  
   pip install -r requirements.txt  
   ```  

3. **Run the Flask App**:  
   Start the application by running:  
   ```bash  
   python app.py  
   ```  

4. **Access the Web Interface**:  
   Open your browser and navigate to:  
   ```
   http://127.0.0.1:5000/  
   ```  

## 🌟 How to Use  
1. Enter the required input values in the form provided on the web page.  
2. Click the "Predict" button to get the taxi fare prediction.  

## 📂 File Structure  
- `app.py`: Flask application to host the model.  
- `templates/`: Contains the HTML files for the web interface.
- `model.pkl`: The serialized machine learning model.
- `scaler.pkl`: The scaler use to scale the input features.
- `requirements.txt`: Python dependencies for the project.  

## 🧠 Model Details  
The machine learning model is trained using data with the following features:  
- **Trip Distance (km)**  
- **Time of Day**  
- **Day of Week**  
- **Passenger Count**  
- **Traffic Conditions**  
- **Weather**  
- **Base Fare ($)**  
- **Per Km Rate ($)**  
- **Per Minute Rate ($)**  
- **Trip Duration (minutes)**  

The model has been evaluated on testing data, achieving **84% accuracy**.  

## 🙌 Contributions  
Contributions, issues, and feature requests are welcome! Feel free to fork the repository and submit a pull request.  

## 📜 License  
This project is open-source and available under the [MIT License](LICENSE).  
