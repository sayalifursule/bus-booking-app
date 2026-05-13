# Bus Booking System (AWS Cloud Deployment)

## Project Overview

This project demonstrates the deployment of a **full-stack Bus Booking Web Application** on AWS Cloud.

The application allows users to:

* Register an account
* Login securely
* Interact with a simple booking interface

The main goal of this project was to **understand real-world cloud deployment**, not just local development.

---

## Live Application

(http://bus-app-lb-1710161434.ap-south-1.elb.amazonaws.com/register)

*(Replace with your Load Balancer URL)*

---

## Tech Stack

**Frontend:**

* HTML
* CSS

**Backend:**

* Python (Flask)

**Database:**

* MySQL (AWS RDS)

**Cloud & DevOps:**

* AWS EC2 (Application Hosting)
* AWS RDS (Managed Database)
* AWS Application Load Balancer
* Nginx (Reverse Proxy)
* Gunicorn (WSGI Server)
* GitHub (Version Control)

---

## Architecture

User Browser
⬇
Application Load Balancer
⬇
EC2 Instance (Nginx + Gunicorn + Flask App)
⬇
AWS RDS (MySQL Database)

---

## Features

* User Registration & Login
* Responsive UI
* Database Integration (MySQL)
* Publicly accessible via Load Balancer
* Production-ready deployment using Nginx & Gunicorn

---

## Screenshots

### 🔹 Application UI

<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/f5d052a3-3365-4ed8-87f8-b59ef1c923f9" />


### 🔹 AWS EC2 Instance

<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/100b26ab-29ee-4019-8c1a-50cc0c66f6ca" />


### 🔹 AWS RDS Database

<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/bbf73e93-d3ed-4b04-808e-acfa5fa9f6c8" />


### 🔹 Load Balancer

<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/d8c6b0db-00c9-414b-9ed5-bd277028f481" />


---

##  Deployment Steps

### EC2 Setup

* Created Ubuntu EC2 instance
* Configured security groups (Ports 22, 80, 8080)
* Connected using SSH

### Application Setup

```bash
git clone <your-repo-link>
cd bus-booking-app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### Run Application (Development)

```bash
python app.py
```

---

### Production Setup (Gunicorn)

```bash
gunicorn -w 3 -b 0.0.0.0:8080 app:app
```

---

### Nginx Configuration

* Configured reverse proxy
* Routed traffic from port 80 → 8080

---

### AWS RDS Setup

* Created MySQL database
* Connected Flask app using endpoint

```python
def get_db():
    return mysql.connector.connect(
        host="RDS-ENDPOINT",
        user="admin",
        password="your-password",
        database="busbookingdb"
    )
```

---

### Load Balancer Setup

* Created Target Group (Port 80)
* Registered EC2 instance
* Created Application Load Balancer
* Routed traffic to EC2

---

## 💡 Key Learnings

* Deploying Flask apps on AWS EC2
* Configuring Security Groups & Networking
* Using Gunicorn for production servers
* Setting up Nginx as reverse proxy
* Connecting EC2 with AWS RDS
* Debugging real-world cloud issues

---

## ⚠️ Challenges Faced

* Virtual environment misconfiguration
* Dependency issues (MySQL connector)
* Port accessibility & timeout errors
* Understanding public IP vs localhost
* Fixing database connection errors

---

## 🏁 Conclusion

This project helped me understand **end-to-end cloud deployment** of a real-world application using AWS services.

It strengthened my knowledge of:

* Cloud infrastructure
* Backend deployment
* Debugging production issues

---

