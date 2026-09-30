# Airbnb Flask API Setup Guide (Ubuntu & macOS)

This project is a **Flask-based RESTful microservice** that provides Airbnb-style listing data from a **MongoDB Atlas** cloud database. It allows users to view, search, and add reviews to listings. The backend is designed to serve an **Android client** and integrates with a separate **authentication microservice**.

This document explains how to set up and run the API on both **Ubuntu Linux** and **macOS** using either **Docker** or **Python virtual environments**, depending on your environment or preference.

---

## Render Deployment (Alternative to Local Setup)

This project is also deployed on [Render](https://render.com), a cloud platform that allows hosting web applications without the need for local configuration.

### Why Use Render?

- No need to install Python, Flask, or Docker  
- Accessible 24/7 from anywhere via a public URL  
- Automatically deployed from the GitLab repository  
- Ideal for quick testing and frontend-backend integration

You can access the live API here: https://airbnb-flask-api.onrender.com

### When to Use It

If you only want to **test the API or access listing data** (e.g., from Postman or an Android app), using the Render URL is sufficient.  
Full API documentation for Render is available in "Airbnb Listings REST API Documentation ver1.2.pdf".

If you're contributing to the backend or need to work offline, follow the instructions below to run it on your own machine.


---


## Ubuntu 20.04+ Setup

### Requirements
- Ubuntu 20.04 or newer
- Internet connection
- Git (`sudo apt install git` if not installed)
- Docker (see below)
- Python 3.12 with `venv` module

---

### 1. Install and Start Docker

```bash
sudo apt update
sudo apt install -y docker.io
sudo systemctl enable docker
sudo systemctl start docker
```

#### If Docker fails to start, try the following:

```bash
sudo apt install --reinstall containerd
sudo rm -f /var/run/docker.pid
sudo mv /etc/docker/daemon.json /etc/docker/daemon.json.bak
sudo systemctl daemon-reexec
sudo systemctl restart docker
```

Verify Docker is installed:

```bash
docker --version
```

---

### 2. Optional: Use Docker without `sudo`

```bash
sudo usermod -aG docker $USER
newgrp docker
```

---

### 3. Clone the Repository

```bash
git clone https://gitlab.hsrw.eu/34254/airbnb-flask-api.git
# Username: 34254@students.hsrw.eu
# Password: <Paste the personal access token below!>
# _Z_Qw4asxhC8QRm1kgF1 (It will be expired on June 23, 2025 at 12:00:00 AM GMT+2)

cd airbnb-flask-api
```

---

### 4. Set Up Python Virtual Environment

```bash
sudo apt install python3.12-venv
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip setuptools
pip install -r requirements.txt
```

---

### 5. Run the Flask App

```bash
python3 app.py
```

Access the app at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

### 6. Build and Run with Docker (optional)

```bash
docker build -t airbnb-api .
docker run -p 8000:8000 airbnb-api
```

Test it:

```bash
curl http://127.0.0.1:8000/
```

---
## API Endpoints

| Method | Endpoint                                     | Description                           |
| ------ | -------------------------------------------- | ------------------------------------- |
| GET    | `/`                                          | Health check                          |
| GET    | `/listings`                                  | List listings (with optional `limit`) |
| GET    | `/listings/search`                           | Search by `country`, `min_price`      |
| GET    | `/listings/<listing_id>`                     | Get one listing                       |
| GET    | `/listings/<listing_id>/reviews`             | View reviews for a listing            |
| POST   | `/reviews`                                   | Add a review (mock)                   |
| DELETE | `/listings/<listing_id>/reviews/<review_id>` | Delete a review (mock)                |

Full API documentation for Local is available in "Airbnb Listings REST API Documentation for Local.pdf".

---


## macOS Setup (Intel/Apple Silicon)

### Requirements
- macOS Ventura or later
- [Homebrew](https://brew.sh/)
- Docker Desktop
- Git
- Python 3.12 via Homebrew

---

### 1. Install Required Tools

```bash
brew install git python@3.12
brew install --cask docker
```

> Make sure Docker Desktop is running in the background!

Verify:

```bash
docker --version
python3 --version
```

---

### 2. Clone the Repository

```bash
git clone https://gitlab.hsrw.eu/34254/airbnb-flask-api.git
# Username: 34254@students.hsrw.eu
# Password: <Paste the personal access token below!>
# _Z_Qw4asxhC8QRm1kgF1 (It will be expired on June 23, 2025 at 12:00:00 AM GMT+2)
cd airbnb-flask-api
```

---

### 3. Set Up Python Virtual Environment

```bash
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip setuptools
pip install -r requirements.txt
```

---

### 4. Run the Flask App

```bash
python3 app.py
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

### 5. Build and Run with Docker

```bash
docker build -t airbnb-api .
docker run -p 8000:8000 airbnb-api
```

Check with:

```bash
curl http://127.0.0.1:8000/
```

---
## API Endpoints

| Method | Endpoint                                     | Description                           |
| ------ | -------------------------------------------- | ------------------------------------- |
| GET    | `/`                                          | Health check                          |
| GET    | `/listings`                                  | List listings (with optional `limit`) |
| GET    | `/listings/search`                           | Search by `country`, `min_price`      |
| GET    | `/listings/<listing_id>`                     | Get one listing                       |
| GET    | `/listings/<listing_id>/reviews`             | View reviews for a listing            |
| POST   | `/reviews`                                   | Add a review (mock)                   |
| DELETE | `/listings/<listing_id>/reviews/<review_id>` | Delete a review (mock)                |

Full API documentation for Local is available in "Airbnb Listings REST API Documentation for Local.pdf".

---
## Tech Stack

* Python 3.11
* Flask
* MongoDB Atlas
* Render (for deployment)
* Docker (for portability)

---





## Optional: How to Completely Uninstall Docker (Ubuntu)

If you wish to remove Docker after testing this project locally on Ubuntu, follow these steps:

### Uninstall Docker packages

```bash
sudo apt-get purge docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

#️## Remove Docker images, containers, volumes, and configuration files
```bash
sudo rm -rf /var/lib/docker
sudo rm -rf /var/lib/containerd
```

### Optional: Remove leftover Docker configuration (if any)
```bash
sudo rm /etc/docker/daemon.json
sudo rm -rf ~/.docker
```

### Verify Docker is fully removed
You can check that Docker is no longer installed by running:
```bash
docker --version
```

You should see:
```bash
Command 'docker' not found
```

---
## Project Structure

```
airbnb-flask-api/
├── app.py
├── requirements.txt
├── Dockerfile
├── Procfile
├── README.md
├── .DS_Store
├── Airbnb Listings REST API Documentation for Local.pdf
├── Airbnb Listings REST API Documentation ver1.2.pdf
├── venv
     ├── bin
     ├── lib/python3.11/site-packages
     ├── .DS_Store
     └── .pyvenv.cfg

```

---

## Contributors

| Name              | Role                                            |
| ----------------- | ----------------------------------------------- |
| Hidetake Tanaka   | Vacation Home Listings Microservice & Team Lead |
| Ilia Pleshakov    | Android Smartphone App Client                   |
| Pengjian Chen     | Authentication Microservice                     |
| Taha Asif         | CLI Tool for Admins                             |

---
## Notes
- Your cloned project folder (e.g. `airbnb-flask-api`) will remain intact even if Docker is uninstalled.
- If you used Docker with other projects, be cautious before deleting volumes or config files, as this may remove unrelated data.
- For issues or questions, contact: Hidetake.Tanaka@hsrw.org 
