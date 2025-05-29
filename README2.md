# Airbnb Flask API

This project is a Flask-based RESTful microservice that provides Airbnb-style listing data from a MongoDB Atlas database. It allows users to view, search, and add reviews to listings. The backend serves an Android client and integrates with a separate authentication microservice.

---

## Live Deployment

**Base URL:**  
[https://airbnb-flask-api.onrender.com](https://airbnb-flask-api.onrender.com)

---

## Features

- Get all listings with optional limit
- Search listings by country and price
- Get detailed info about a listing
- View reviews for a listing
- Add a new review (mock)
- Delete a review (mock)
- JSON serialization of MongoDB fields (`Decimal128`, `ObjectId`, etc.)

---

## How to Run Locally

### 1. Clone this Repository

```bash
git clone https://gitlab.hsrw.eu/34254/airbnb-flask-api.git
cd airbnb-flask-api
````

### 2. Setup Python Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Copy `.env.example` to `.env` and provide your own MongoDB URI.

```env
MONGO_URI=mongodb+srv://<username>:<password>@<cluster>.mongodb.net/
```

Or modify directly in `app.py` if no `.env` used.

### 4. Start Server

```bash
python app.py
```

---

## Docker (Alternative)

```bash
docker build -t airbnb-api .
docker run -p 8000:8000 airbnb-api
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

Full API documentation is available in [`docs/api-doc.md`](docs/api-doc.md).

---

## Tech Stack

* Python 3.11
* Flask
* MongoDB Atlas
* Render (for deployment)
* Docker (for portability)

---

## Authentication (Optional Integration)

JWT authentication is managed by a separate **Authentication microservice**. In future versions, all endpoints (except `/`) may require Bearer tokens in the header.

---

## Project Structure

```
airbnb-flask-api/
├── app.py
├── requirements.txt
├── Dockerfile
├── .env.example
├── README.md
├── docs/
│   └── api-doc.md
└── .gitignore
```

---

## Contributors

| Name              | Role                            |
| ----------------- | ------------------------------- |
| Hidetake Tanaka   | Backend (Flask API) & Team Lead |
| Ilia Pleshakov    | Mobile App Interface            |
| Pengjian Chen     | JWT-based User Auth             |
| Taha Asif.        | Admin CLI Tool Integration      |

---

## Final Notes

* All review inserts and deletes are **mocked** if using sample dataset
* Keep `.env` private and never commit real credentials
* Repository is now **ready for submission** 🎓


