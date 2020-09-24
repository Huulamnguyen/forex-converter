from flask import Flask, request, render_template, session, flash, redirect
from convert import currency_rate, currency_code, check_currency_code
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
    errors = []    
    convert_from = request.form["convert_from"].upper()
    convert_to = request.form["convert_to"].upper()
    try: 
        amount = float(request.form["amount"])
        res = currency_rate(convert_from,convert_to,amount)
    except (TypeError, ValueError, RatesNotAvailableError):

        errors.append("Not a valid amount") 

        if not check_currency_code(convert_from):
            errors.append(f"Not a valid code: {convert_from}")            

        if not check_currency_code(convert_to):
            errors.append(f"Not a valid code: {convert_to}")             
       
        if errors:
            for error in errors:
                flash(error, "msg")
            
        return redirect('/')         
     
    code = currency_code(convert_to)  
    return render_template('result.html', res=res, code=code) 

 