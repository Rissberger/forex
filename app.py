from flask import Flask, request, render_template
import requests 



app = Flask(__name__)

url = 'https://api.exchangerate.host/live?access_key=acdf75d28a50831fcfb187c1061ff59c'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    from_currency = request.form['fromCurrency']
    to_currency = request.form['toCurrency']
    amount = request.form['amount']

    response = requests.get(
        "https://api.exchangerate.host/convert",
        params={
            "access_key": "acdf75d28a50831fcfb187c1061ff59c",  
            "from": from_currency,
            "to": to_currency,
            "amount": amount,
        }
    ) 

    if response.status_code == 200:
        data = response.json()
        rates = data['rates'][from_currency]
        amount_in_EUR = amount / rates
        amount = amount_in_EUR * (data['rates'][to_currency])
        amount = round(amount, 2)
        print(amount)
        result = amount  
    else:
        result = "Error in conversion"

    return render_template('index.html', conversion_result=result)

