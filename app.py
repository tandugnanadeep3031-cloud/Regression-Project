import joblib
from flask import Flask, jsonify, request

app = Flask(__name__)
model = joblib.load('model.pkl')  # Load your trained model


@app.route('/')
def home():
  return 'EV Charging Station Regression Project API is Live!'


@app.route('/predict', methods=['POST'])
def predict():
  data = request.get_json()
  # Extract features and make prediction
  # prediction = model.predict([data['features']])
  return jsonify({'prediction': 'Your model prediction result here'})


if __name__ == '__main__':
  app.run(debug=True)
