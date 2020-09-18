from flask import Flask, request, render_template, session, flash, redirect
from convert import currency_rate, currency_code, available_currencies
from forex_python.converter import RatesNotAvailableError

app = Flask(__name__)

app.config['SECRET_KEY'] = "forex-converter"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

@app.route('/')
def home_page():
    """Shows home page"""
    return render_template('home.html')

@app.route('/result', methods=['POST'])
def convert():
    """Show result"""
    
    convert_from = request.form["convert_from"].upper()
    convert_to = request.form["convert_to"].upper()
    try: 
        amount = float(request.form["amount"])
        res = currency_rate(convert_from,convert_to,amount)
    except (ValueError, RatesNotAvailableError):
        if convert_from not in available_currencies and convert_to not in available_currencies:
            flash(f"Not a valid code: {convert_from}", "msg")
            flash(f"Not a valid code: {convert_to}", "msg")
        elif convert_from not in available_currencies:
            flash(f"Not a valid code: {convert_from}", "msg")
        elif convert_to not in available_currencies:
            flash(f"Not a valid code: {convert_to}", "msg")      
        flash("Not a valid amount", "msg")
        return redirect('/')         
     
    code = currency_code(convert_to)  
    return render_template('result.html', res=res, code=code) 

 