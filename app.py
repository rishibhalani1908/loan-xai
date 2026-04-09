from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from model import check_loan

app = Flask(__name__)
app.secret_key = "secret123"

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']

    if username == "admin" and password == "1234":
        session['user'] = username
        return redirect(url_for('dashboard'))
    return "Invalid Login"

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template('dashboard.html')
    return redirect(url_for('login'))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    income = int(data['income'])
    credit = int(data['credit'])
    loan = int(data['loan'])
    age = int(data['age'])

    result = check_loan(income, credit, loan, age)
    return jsonify(result)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, port=5500)