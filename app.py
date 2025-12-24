from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Model ve scaler'ı yükle
model = joblib.load("car_price_model.pkl")
scaler = joblib.load("scaler.pkl")

fuel_mapping = {"Petrol": 0, "Diesel": 1, "CNG": 2}
seller_mapping = {"Dealer": 0, "Individual": 1}
transmission_mapping = {"Manual": 0, "Automatic": 1}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        year = int(request.form['year'])
        km_driven = int(request.form['km_driven'])
        fuel = request.form['fuel']
        seller_type = request.form['seller_type']
        transmission = request.form['transmission']
        owner = int(request.form['owner'])

        fuel_enc = fuel_mapping[fuel]
        seller_enc = seller_mapping[seller_type]
        trans_enc = transmission_mapping[transmission]

        input_data = np.array([[year, km_driven, fuel_enc, seller_enc, trans_enc, owner]])
        input_scaled = scaler.transform(input_data)

        prediction = model.predict(input_scaled)[0]
        prediction = round(prediction, 2)

        return render_template('index.html', prediction_text=f"Tahmini Satış Fiyatı: {prediction} TL")
    except Exception as e:
        return render_template('index.html', prediction_text=f"Hata: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)

