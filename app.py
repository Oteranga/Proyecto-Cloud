from flask import Flask, render_template, request, jsonify
from model import get_prediction

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

default_companies = ["Netflix", "Apple", "Amazon"]

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from the form
        dropdown_value = request.form['dropdown']
        new_company = request.form['new_company']
        features = [int(request.form['feature1']), int(request.form['feature2'])]
        print(features)
        
        # If a new company is provided, add it to the list
        if new_company:
            default_companies.append(new_company)
            prediction = get_prediction(features[0], features[1], new_company)
        else:
            # Call your machine learning model for prediction
            #prediction = predict_stock_price(np.array(features).reshape(1, -1))  # Adjust input format as needed
            prediction = get_prediction(features[0], features[1], dropdown_value)
        
        
        return render_template('index.html', img_data=prediction,dropdown_options=default_companies)
    except Exception as e:
        return render_template('index.html', error=str(e),dropdown_options=default_companies)


if __name__ == '__main__':
    app.run(debug=False, threaded=False, port=8080)
