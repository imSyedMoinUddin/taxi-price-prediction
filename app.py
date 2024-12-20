import pickle
import pandas as pd
from flask import Flask, request, render_template
import warnings
warnings.simplefilter(action='ignore')

# Load the trained model and scaler
model_path = 'taxi_price_model.pkl'
scaler_path = 'scaler.pkl'

with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

with open(scaler_path, 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Flask app setup
app = Flask(__name__)

# Homepage route
@app.route('/')
def home():
    return render_template('index.html')  # Make sure you have an index.html file with placeholders for user input

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract data from the form
        input_data = {
            'Trip_Distance_km': float(request.form['Trip_Distance_km']),
            'Time_of_Day': request.form['Time_of_Day'],
            'Day_of_Week': request.form['Day_of_Week'],
            'Passenger_Count': float(request.form['Passenger_Count']),
            'Traffic_Conditions': request.form['Traffic_Conditions'],
            'Weather': request.form['Weather'],
            'Base_Fare': float(request.form['Base_Fare']),
            'Per_Km_Rate': float(request.form['Per_Km_Rate']),
            'Per_Minute_Rate': float(request.form['Per_Minute_Rate']),
            'Trip_Duration_Minutes': float(request.form['Trip_Duration_Minutes'])
        }

        # Encode categorical features
        time_of_day_mapping = {'Morning': 0, 'Afternoon': 1, 'Evening': 2, 'Night': 3}
        day_of_week_mapping = {'Weekday': 0, 'Weekend': 1}
        traffic_conditions_mapping = {'Low': 0, 'Medium': 1, 'High': 2}

        input_data['Time_of_Day'] = time_of_day_mapping[input_data['Time_of_Day']]
        input_data['Day_of_Week'] = day_of_week_mapping[input_data['Day_of_Week']]
        input_data['Traffic_Conditions'] = traffic_conditions_mapping[input_data['Traffic_Conditions']]

        # One-Hot Encode 'Weather' feature
        weather_encoded = {'Weather_Clear': 0, 'Weather_Rain': 0, 'Weather_Snow': 0}
        weather_column = f"Weather_{input_data['Weather']}"
        if weather_column in weather_encoded:
            weather_encoded[weather_column] = 1

        # Combine all features into a single list
        feature_values = [
            input_data['Trip_Distance_km'],
            input_data['Time_of_Day'],
            input_data['Day_of_Week'],
            input_data['Passenger_Count'],
            input_data['Traffic_Conditions'],
            weather_encoded['Weather_Clear'],
            weather_encoded['Weather_Rain'],
            weather_encoded['Weather_Snow'],
            input_data['Base_Fare'],
            input_data['Per_Km_Rate'],
            input_data['Per_Minute_Rate'],
            input_data['Trip_Duration_Minutes'],
        ]

        # Scale the features
        scaled_features = scaler.transform([feature_values])

        # Predict the trip price
        prediction = model.predict(scaled_features)[0]

        # Render the same page with the prediction result
        return render_template(
            'index.html',
            prediction_text=f"Predicted Taxi Trip Price: ${round(prediction, 2)}",
            scaled_features=scaled_features.tolist()
        )

    except ValueError:
        return render_template('index.html', error_text="All fields should be integer or float numbers.")
    except Exception as e:
        return render_template('index.html', error_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
