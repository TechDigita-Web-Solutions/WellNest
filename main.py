from flask import Flask, request, render_template, redirect, url_for, flash, session
from modules.user_db_insert import insert_user
from modules.user_auth import authenticate_user
from modules.auth import auth_bp
import sqlite3
from data.tips import tips as tipsdata

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.register_blueprint(auth_bp)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tests')
def tests():
    return render_template('tests.html')

@app.route('/tips')
def tips():
    print(tipsdata)
    return render_template('tips.html', tipsdata=tipsdata)

@app.route('/profile')
def profile():
    if 'user' in session:
        conn = sqlite3.connect('wellnest.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', (session['user'],))
        user = cursor.fetchone()
        conn.close()
        return render_template('profile.html', user=user)
    else:
        return redirect(url_for('auth_bp.login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if authenticate_user(username, password):
            ststic_info(username)
            session['user'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('index'))

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


def ststic_info(username):
    current_username = username
    return current_username

if __name__ == '__main__':
    app.run(debug=True)
