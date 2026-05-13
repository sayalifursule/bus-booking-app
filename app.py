import mysql.connector
from flask import Flask, request

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host="database-1.c3qiuqmi6jq1.ap-south-1.rds.amazonaws.com",
        user="admin",
        password="11Sayu1143",
        database="bus_db"
    )

# HOME PAGE (LOGIN + REGISTER TOGETHER)
@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<title>Bus Booking System</title>

<style>
body{
    margin:0;
    font-family: Arial;
    background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
    height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
}

/* MAIN CARD */
.card{
    background:white;
    width:420px;
    padding:30px;
    border-radius:15px;
    box-shadow:0 10px 30px rgba(0,0,0,0.3);
    text-align:center;
}

/* TITLE */
h2{
    color:#1e3c72;
}

/* INPUT */
input{
    width:90%;
    padding:10px;
    margin:8px 0;
    border-radius:8px;
    border:1px solid #ccc;
}

/* BUTTON */
button{
    width:95%;
    padding:10px;
    border:none;
    border-radius:8px;
    margin-top:10px;
    font-weight:bold;
    color:white;
    cursor:pointer;
}

/* COLORS */
.login-btn{ background:#1e3c72; }
.register-btn{ background:#28a745; }

/* TABS */
.tab-buttons{
    display:flex;
    justify-content:space-between;
    margin-bottom:20px;
}

.tab{
    width:48%;
    padding:10px;
    border:none;
    cursor:pointer;
    border-radius:8px;
    font-weight:bold;
}

.active-login{ background:#1e3c72; color:white; }
.active-register{ background:#28a745; color:white; }

/* HIDE/SHOW */
.form-box{ display:none; }
.show{ display:block; }

</style>

<script>
function showLogin(){
    document.getElementById("login").style.display="block";
    document.getElementById("register").style.display="none";
}

function showRegister(){
    document.getElementById("login").style.display="none";
    document.getElementById("register").style.display="block";
}
</script>

</head>

<body>

<div class="card">

<h2>🚌 Bus Booking System</h2>

<div class="tab-buttons">
    <button class="tab active-login" onclick="showLogin()">Login</button>
    <button class="tab active-register" onclick="showRegister()">Register</button>
</div>

<!-- LOGIN FORM -->
<div id="login" class="form-box show">
<form action="/login" method="POST">
    <input name="email" placeholder="Email" required><br>
    <input name="password" placeholder="Password" type="password" required><br>
    <button class="login-btn" type="submit">Login</button>
</form>
</div>

<!-- REGISTER FORM -->
<div id="register" class="form-box">
<form action="/register" method="POST">
    <input name="fullname" placeholder="Full Name" required><br>
    <input name="email" placeholder="Email" required><br>
    <input name="password" placeholder="Password" type="password" required><br>
    <button class="register-btn" type="submit">Register</button>
</form>
</div>

</div>

</body>
</html>
"""

# REGISTER
@app.route('/register', methods=['POST'])
def register():
    fullname = request.form['fullname']
    email = request.form['email']
    password = request.form['password']

    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO users(fullname,email,password) VALUES(%s,%s,%s)",
        (fullname, email, password)
    )

    db.commit()
    db.close()

    return "<h2 style='text-align:center;color:green;'>Registration Successful ✅</h2><p style='text-align:center;'><a href='/'>Go Back</a></p>"

# LOGIN
@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=%s AND password=%s",
        (email, password)
    )

    user = cursor.fetchone()
    db.close()

    if user:
        return "<h2 style='text-align:center;color:green;'>Login Successful 🎉</h2><p style='text-align:center;'>Welcome to Bus Booking System</p><p style='text-align:center;'><a href='/'>Logout</a></p>"
    else:
        return "<h2 style='text-align:center;color:red;'>Invalid Credentials ❌</h2><p style='text-align:center;'><a href='/'>Try Again</a></p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
