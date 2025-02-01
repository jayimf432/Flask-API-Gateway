# **🚀 Flask API Gateway - Load Balancer**
A **modular, scalable, and lightweight API Gateway** built using **Flask**, designed to distribute incoming requests to multiple backend servers efficiently.  
It ensures **parallel processing, load balancing, and request denial** if all servers are busy.  

![Flask API Gateway](https://repository-images.githubusercontent.com/your-repo-id/your-image.png)

---

## **📌 Features**
✅ **Load Balancing** - Distributes requests to idle backend servers.  
✅ **Parallel Processing** - Uses `ThreadPoolExecutor` to handle multiple requests at once.  
✅ **Scalable & Modular** - Easily extendable for different applications.  
✅ **Auto-Failover** - If a server is unreachable, the request is redirected to another available server.  
✅ **Denies Requests If All Servers Are Busy** - Prevents overloading.  

---

## **📁 Project Structure**
```
flask_api_gateway/
│── api_gateway/
│   │── __init__.py          # API Gateway Package
│   │── gateway.py           # Main API Gateway Logic
│   │── config.py            # Configuration File
│   │── utils.py             # Utility Functions
│── backend/
│   │── server.py            # Generic Backend Server
│── examples/
│   │── test_request.py      # Example Test Client
│── requirements.txt         # Dependencies
│── README.md                # Documentation
│── run_gateway.py           # Entry Point to Start API Gateway
```

---

## **🛠️ Setup & Installation**
### **🔹 Step 1: Clone the Repository**
```sh
git clone https://github.com/jayimf432/Flask-API-Gateway.git
cd Flask-API-Gateway
```

### **🔹 Step 2: Set Up Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate      # Windows
```

### **🔹 Step 3: Install Dependencies**
```sh
pip install -r requirements.txt
```

---

## **🚀 Running the Project**
### **1️⃣ Start Backend Servers**
Run **five terminals** and start each backend server:

```sh
python backend/server.py 6000
python backend/server.py 6001
python backend/server.py 6002
python backend/server.py 6003
python backend/server.py 6004
```

### **2️⃣ Start API Gateway**
```sh
python run_gateway.py
```
📌 The API Gateway runs at `http://127.0.0.1:5000/process`.

### **3️⃣ Test API**
#### ✅ Using cURL:
```sh
curl -X POST "http://127.0.0.1:5000/process" -H "Content-Type: application/json" -d '{"task": "data analysis"}'
```

#### ✅ Using Python:
```python
import requests

data = {"task": "data analysis"}
response = requests.post("http://127.0.0.1:5000/process", json=data)
print(response.json())
```

---

## **📌 How It Works**
### **🌐 API Gateway Workflow**
1️⃣ **Receives a request** on `http://127.0.0.1:5000/process`.  
2️⃣ **Finds an idle backend server** from the `SERVERS` list.  
3️⃣ **If a server is available**, it forwards the request.  
4️⃣ **If all servers are busy**, the request is rejected (`503 Service Unavailable`).  
5️⃣ **Handles requests in parallel** using `ThreadPoolExecutor`.  

---
## **🖥️ System Architecture**
```plaintext
            +-----------------------+
            |  Client Request        |
            |  (POST /process)       |
            +-----------------------+
                      |
                      v
            +-----------------------+
            |  API Gateway (Flask)   |
            |  http://127.0.0.1:5000 |
            +-----------------------+
                     |    |    |    |
                     v    v    v    v
    +------------+  +------------+  +------------+  +------------+
    |  Server 1  |  |  Server 2  |  |  Server 3  |  |  Server 4  |
    |  (6000)    |  |  (6001)    |  |  (6002)    |  |  (6003)    |
    +------------+  +------------+  +------------+  +------------+
```

---
## **⚙️ Configuration**
Modify **`api_gateway/config.py`** to add more backend servers:

```python
# List of backend servers
SERVERS = [
    "http://127.0.0.1:6000/process",
    "http://127.0.0.1:6001/process",
    "http://127.0.0.1:6002/process"
]
TIMEOUT = 10  # Response timeout in seconds
```

---

## **🛠️ How to Use in Any Project**
### **Option 1: Using as a Package**
1. Copy the `api_gateway` folder to your project.
2. Import `run_gateway()`:
```python
from api_gateway import run_gateway

if __name__ == "__main__":
    run_gateway()
```

### **Option 2: Running as a Separate Service**
1. Deploy **flask_api_gateway** separately.
2. In your project, send requests to `http://127.0.0.1:5000/process`:
```python
import requests

data = {"task": "image processing"}
response = requests.post("http://127.0.0.1:5000/process", json=data)
print(response.json())
```

---

## **📌 Future Enhancements**
🔹 **Docker support** for easy deployment  
🔹 **Logging & monitoring** for debugging  
🔹 **Cloud deployment** (AWS, GCP, Azure)  

---

## **🌟 Contributors**
💡 **Created by Jayaram Kumarapu**  
🔗 GitHub: [Your GitHub Profile](https://github.com/jayimf432)  

---

## **📜 License**
📄 MIT License - Free to use and modify.

---