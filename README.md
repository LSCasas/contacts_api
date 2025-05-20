# Contact List API (Django REST Framework)

> This project is part of the **backend learning portfolio with Django**.

A RESTful API built with Django and Django REST Framework to manage a list of personal contacts. It allows authenticated users to create, view, update, and delete contacts associated with their account. The project is designed to be scalable and secure.

---

##  Documentation

https://documenter.getpostman.com/view/36791092/2sB2izDYVn

##  Project Structure

```
contacts_api/
├── contacts_api/         # Main project configuration (settings, urls, wsgi)
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── contacts/             # Main contacts application
│   ├── admin.py
│   ├── apps.py
│   ├── models.py         # Contact model
│   ├── serializers.py    # Serializer for Contact
│   ├── urls.py           # Specific routes for contacts
│   ├── views.py
│   ├── viewsets.py       # ViewSets with CRUD logic
│   └── migrations/
│
├── manage.py
├── requirements.txt
└── README.md
```

---

##  Features

- User registration and authentication with JWT tokens (`/api/token/`)
- Full CRUD for personal contacts
- Access restriction: each user can only view their own contacts
- Serialization with custom validations
- ViewSets and automatic routers using `DefaultRouter`
- Clean modularity between views, serializers, and models

---

## ⚙️ Technologies

- Python 3.x
- Django
- Django REST Framework
- SimpleJWT (for JWT authentication)
- psycopg
- python-dotenv

---

##  How to Use This Project

1. Clone the repository:

   ```bash
   git clone https://github.com/LSCasas/contacts_api.git
   cd contact_list_api
   ```

2. Create a virtual environment and install dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Apply migrations and create a superuser:

   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. Run the server:

   ```bash
   python manage.py runserver
   ```

5. Use Postman or curl to authenticate and access the endpoints:

   - `POST /api/token/` to obtain tokens
   - `GET /api/contacts/` to view your contacts
   - `POST /api/contacts/` to create a new contact

---

##  Authentication Example

1. Request the token:

   ```
   POST http://127.0.0.1:8000/api/token/
   Content-Type: application/json

   {
     "username": "test",
     "password": "test123"
   }
   ```

2. Use the token to access the API:

   ```
   GET http://127.0.0.1:8000/api/contacts/
   Authorization: Bearer <access_token>
   ```

---

##  Requirements

- Python 3.8+
- pip
- Django >= 4.0
- djangorestframework
- djangorestframework-simplejwt

---
