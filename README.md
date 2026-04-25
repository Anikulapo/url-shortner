# Django URL Shortener

A simple and efficient URL Shortener API built with Django and Django REST Framework. It allows you to shorten long URLs into 7-character short codes and seamlessly redirects users to the original URLs when the short code is accessed.

## Features

- **Shorten Long URLs**: Accepts a long URL and generates a unique, 7-character short code.
- **Idempotency**: If a URL has already been shortened, fetching it will return the existing short code.
- **Redirection**: Visiting the short URL redirects the user directly to the original URL.
- **Validation**: Ensures proper URL format before shortening.
- **CORS Support**: Integrated with `django-cors-headers` to support cross-origin requests.

## Technologies Used

- Python 3
- Django 6.x
- Django REST Framework
- SQLite (Default database)

## Setup and Installation

### Prerequisites

- Python 3.10+ installed on your system.

### Steps

1. **Navigate to the project directory:**
   ```bash
   cd path/to/url-shortner
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - **Windows:**
     ```bash
     .\venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

The application will be running at `http://127.0.0.1:8000/`.

## API Documentation

### 1. Shorten a URL

Creates a new short URL or retrieves an existing one for the provided long URL.

- **URL:** `/shorten/`
- **Method:** `POST`
- **Content-Type:** `application/json`

#### Request Body
```json
{
  "url": "https://www.example.com/some/long/path?query=string"
}
```

#### Success Response
- **Code:** `201 CREATED` (if new) or `200 OK` (if already exists)
- **Content:**
  ```json
  {
    "short_code": "aB3dE5g",
    "short_url": "http://127.0.0.1:8000/aB3dE5g"
  }
  ```

#### Error Responses
- **Condition:** Invalid URL format.
  - **Code:** `400 BAD REQUEST`
  - **Content:** `{"error": "Invalid URL format."}`

- **Condition:** Long URL is not provided.
  - **Code:** `400 BAD REQUEST`
  - **Content:** `{"error": "Long URL is required."}`

### 2. Redirect to Original URL

Redirects the client to the original URL associated with the given short code.

- **URL:** `/<short_code>/`
- **Method:** `GET`

#### Success Response
- **Code:** `302 FOUND` (Redirects directly to the original URL)

#### Error Response
- **Condition:** Short code does not exist.
- **Code:** `404 NOT FOUND`
