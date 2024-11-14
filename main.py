from flask import Flask, request, render_template, redirect, url_for, flash
from modules.user_db_insert import insert_user
from modules.user_auth import authenticate_user

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tests')
def tests():
    return render_template('tests.html')

@app.route('/tips')
def tips():
    return render_template('tips.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if authenticate_user(username, password):
            flash('Login successful!', 'success')
            return redirect(url_for('profile'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_data = {
            'username': request.form['username'],
            'password': request.form['password'],
            'name': request.form['name'],
            'age': request.form['age'],
            'gender': request.form['gender'],
            'email': request.form['email'],
            'phone': request.form['phone'],
            'address': request.form['address'],
            'city': request.form['city'],
            'state': request.form['state'],
            'zip': request.form['zip'],
            'country': request.form['country']
        }
        insert_user(user_data)
        return redirect(url_for('register'))
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
