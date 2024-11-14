from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from modules.user_db_insert import insert_user
from modules.user_auth import authenticate_user
import sqlite3

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if authenticate_user(username, password):
            session['user'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
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
        return redirect(url_for('login'))
    return render_template('register.html')

# def profile_render():
#     if 'user' in session:
#         conn = sqlite3.connect('wellnest.db')
#         cursor = conn.cursor()
#         cursor.execute('SELECT * FROM users WHERE username = ?', (session['user'],))
#         user = cursor.fetchone()
#         conn.close()
#         return render_template('profile.html', user=user)
#     else:
#         return redirect(url_for('auth_bp.login'))

def authenticate_user(username, password):
    conn = sqlite3.connect('wellnest.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None