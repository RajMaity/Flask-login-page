# Importing required libraries
from flask import Flask, render_template, request, url_for, redirect, flash, session

# Creating object of Flask class
app = Flask(__name__)

# A secret key is required to use flash messages (sessions)
app.secret_key = "super_secret_key_123"

# Dictionary of username and password (We should use a DB to store Username and Password)
credentials_dict = {
    'Peter Griffin': ['petergriffin@gmai.com','peter12345'],
    'Stewie Griffin': ['stewiegriffin@gmai.com','stewie12345']
}

# Routings
# Login Page
@app.route('/')
def login():
    return render_template('login.html')

# Registration page
@app.route('/registration')
def registration():
    return render_template('registration.html')

# Save new user
@app.route('/save_user',methods = ['POST'])
def save_user():
    new_user_name = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    credentials_dict[new_user_name] = [email,password]
    flash("User registered, you can login now", "success")
    return redirect(url_for('login'))

# Home page
@app.route('/home')
def home():
    # Retrieve the username from the session
    user = session.get('user_name')
    if not user:
        # If someone tries to access /home without logging in, send them back
        flash("Please login first", "warning")
        return redirect(url_for('login'))
    
    return render_template('home.html', name = user)

# Login validation
@app.route('/login_validation', methods = ['POST'])
def login_validation():
    username = request.form.get('username')
    password = request.form.get('password')
    if(username in credentials_dict.keys()):
        if(password == credentials_dict[username][1]):
            session['user_name'] = username
            return redirect(url_for('home'))
        else:
            flash("Wrong password! Please try again.", "danger")
            return redirect(url_for('login'))
    else:
        flash("Username not found! Are you sure you're registered?", "warning")
        return redirect(url_for('login'))    

# Logout
@app.route('/logout')
def logout():
    session.pop('user_name', None)
    return redirect(url_for('login'))

# App run
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)