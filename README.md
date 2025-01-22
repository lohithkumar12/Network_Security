
# **Network Security System using MLOps**

## **Overview**
This project implements an end-to-end **Network Security System**, leveraging **MLOps practices** to detect network security threats efficiently. It follows a structured pipeline covering data ingestion, preprocessing, model training, deployment, and monitoring using **AWS cloud services, Docker, GitHub Actions, and DagsHub for ML lifecycle tracking.**

---

## **Table of Contents**
- [Project Structure](#project-structure)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Experiment Tracking](#experiment-tracking)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)

---

## **Project Structure**

```
📂 Network Security System
│-- 📂 data/                # Raw and processed data
│-- 📂 models/              # Trained model files
│-- 📂 scripts/             # ETL and training scripts
│-- 📂 deployment/          # AWS EC2 and App Runner configurations
│-- 📜 app.py               # Main API service
│-- 📜 Dockerfile           # Containerization setup
│-- 📜 requirements.txt     # Dependencies
│-- 📜 README.md            # Project documentation
```

---

## **Features**
- **ETL Pipeline:**  
  - Extracts data from CSV files, APIs, and AWS S3.  
  - Transforms data through preprocessing and cleaning.  
  - Loads processed data into **MongoDB Atlas**, AWS DynamoDB, MySQL, and S3.

- **Data Processing:**  
  - Schema validation and data drift detection using DagsHub and MLflow.  
  - Feature engineering and preprocessing.

- **Model Training:**  
  - Automated model selection and metric evaluation logged in **MLflow (via DagsHub)**.  
  - Model persistence using `pickle` and stored in AWS S3.

- **Deployment:**  
  - Dockerized containers deployed to AWS EC2 via GitHub Actions.  
  - CI/CD automation with AWS App Runner for efficient deployment.

- **Monitoring & Logging:**  
  - MLflow for model experiment tracking.

---

## **Technologies Used**
- **Programming & Frameworks:** Python (FastAPI, Flask)
- **Cloud Services:** AWS EC2, S3, App Runner, MongoDB Atlas
- **MLOps Tools:** DagsHub, MLflow, GitHub Actions
- **Database Management:** DBeaver for PostgreSQL/MySQL exploration
- **DevOps Tools:** Docker, GitHub Actions
- **ML Libraries:** Scikit-learn, Pandas, NumPy

---

## **Installation**

### **1. Clone the Repository**
```bash
git clone https://github.com/lohithkumar12/Network_Security.git
cd Network_Security
```

### **2. Set Up Environment**
Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### **3. Set Up AWS and DagsHub Credentials**
Create a `.env` file and configure your AWS and DagsHub credentials:
```
AWS_ACCESS_KEY=your_access_key
AWS_SECRET_KEY=your_secret_key
MONGO_URI=your_mongodb_uri
DAGSHUB_USERNAME=your_dagshub_username
DAGSHUB_TOKEN=your_dagshub_token
```

### **4. Run the Application**
```bash
python app.py
```

---

## **Usage**

1. Upload network traffic data to AWS S3 or MongoDB.
2. Track model training experiments using MLflow via DagsHub.
3. Query processed data using DBeaver for validation.
4. Access the API for security threat predictions.

---

## **Deployment**

### **1. Local Deployment**
Run the project locally using:
```bash
python app.py
```

### **2. Cloud Deployment (AWS EC2 + App Runner)**
1. Build and push the Docker image to AWS ECR:
   ```bash
   docker build -t network-security .
   aws ecr create-repository --repository-name network-security
   aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com
   docker tag network-security:latest <AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/network-security:latest
   docker push <AWS_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/network-security:latest
   ```
2. Deploy using GitHub Actions CI/CD pipeline with AWS App Runner.

---

## **Experiment Tracking**

The project uses **DagsHub** for experiment tracking and model monitoring through MLflow.  
Track experiments by logging into DagsHub and checking:  
[Your DagsHub Project Link](https://dagshub.com/vemuboddupalli/Network_Security)


---


## **Future Enhancements**
- Implement real-time data streaming with **Apache Kafka**.
- Integrate auto-scaling with **AWS Lambda**.
- Enhance visualization with Grafana dashboards.

---

## **Contributing**
Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Added a new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.
