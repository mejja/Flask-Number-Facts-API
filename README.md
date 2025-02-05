# 📌 Flask Number Facts API

A fast and efficient API that classifies numbers based on mathematical properties and provides fun facts. The API is built with **Flask**, deployed on **AWS**, and automated using **GitHub Actions**.

## 🚀 Features
- **Prime & Perfect Number Check**
- **Armstrong Number Detection**
- **Sum of Digits Calculation**
- **Happy Number Test**
- **Predefined Fun Facts (Fast Response)**
- **RESTful API with JSON Responses**
- **CORS Support for Cross-Origin Requests**
- **Optimized for Response Time (<500ms)**
- **Deployed on AWS (Elastic Beanstalk/EC2)**
- **CI/CD Automated via GitHub Actions**

---

## 📂 Project Structure
```
📁 flask-number-api
│── app.py               # Main Flask Application
│── Dockerfile           # Docker Configuration
│── requirements.txt     # Python Dependencies
│── .github/workflows/   # CI/CD Configuration
│── README.md            # Project Documentation
```

---

## 🛠️ Setup & Installation

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/your-username/flask-number-api.git
cd flask-number-api
```

### **2️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3️⃣ Run the API Locally**
```sh
python app.py
```

API will be available at: `http://127.0.0.1:5000`

---

## 🌍 API Endpoints

### **1️⃣ Classify a Number**
#### **GET `/api/classify-number?number={num}`**
#### **📌 Example Request:**
```sh
GET http://127.0.0.1:5000/api/classify-number?number=371
```
#### **✅ Example Response:**
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371."
}
```

#### **❌ Error Response (Invalid Input)**
```json
{
    "number": "abc",
    "error": true
}
```

---

## 🤔 Happy Number Test
A number is considered "happy" if replacing it with the sum of squares of its digits eventually results in `1`. Otherwise, it falls into a cycle.

#### **Example (Checking if 23 is Happy):**
```
2² + 3² = 13
1² + 3² = 10
1² + 0² = 1 (Happy Number ✅)
```

#### **Example (Checking if 4 is Happy):**
```
4² = 16
1² + 6² = 37
3² + 7² = 58
5² + 8² = 89
8² + 9² = 145
1² + 4² + 5² = 42
4² + 2² = 20
2² + 0² = 4 (Cycle Detected ❌)
```

---

## 🚀 Deployment to AWS (Elastic Beanstalk)

### **1️⃣ Install AWS CLI & Elastic Beanstalk CLI**
```sh
pip install awsebcli --upgrade
aws configure  # Enter AWS credentials
```

### **2️⃣ Initialize & Deploy**
```sh
eb init -p python-3.8 flask-number-api --region us-east-1
eb create flask-api-env
```

API will be available at: `http://flask-api-env.eba-xyz.amazonaws.com`

---

## 🤖 CI/CD with GitHub Actions
### **1️⃣ Configure GitHub Secrets**
Go to **GitHub Repository → Settings → Secrets and Variables → Actions** and add:
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`

### **2️⃣ Auto-Deploy on Push to `main`**
```yaml
name: Deploy to AWS

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v3

      - name: Install AWS CLI
        run: |
          sudo apt update
          sudo apt install awscli -y
          aws --version

      - name: Deploy to Elastic Beanstalk
        run: |
          pip install awsebcli
          eb init -p python-3.8 flask-number-api --region us-east-1
          eb deploy
```

---

## 📜 License
This project is licensed under the MIT License.

---

## 🙌 Contributing
Pull requests are welcome! If you find an issue, please open one.

---

## 📞 Contact
For inquiries, reach out via [GitHub Issues](https://github.com/your-username/flask-number-api/issues).

