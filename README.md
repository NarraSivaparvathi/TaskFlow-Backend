# TaskFlow – Secure Task Management REST API

A secure REST API built with Django REST Framework that allows users to register, authenticate, and manage personal tasks using JWT authentication.

## Features

* User registration
* JWT access and refresh tokens
* Create, view, update, and delete tasks
* Task status management: Pending, In Progress, Completed
* User-specific task access and authorization
* Input validation using serializers
* Interactive API documentation with Swagger UI
* Automated API tests

## Technologies Used

* Python
* Django
* Django REST Framework
* Simple JWT
* drf-spectacular
* SQLite
* Git and GitHub

## API Endpoints

| Method    | Endpoint              | Purpose                    |
| --------- | --------------------- | -------------------------- |
| POST      | `/api/register/`      | Register a user            |
| POST      | `/api/token/`         | Obtain JWT tokens          |
| POST      | `/api/token/refresh/` | Refresh an access token    |
| GET       | `/api/tasks/`         | List your tasks            |
| POST      | `/api/tasks/`         | Create a task              |
| GET       | `/api/tasks/{id}/`    | Retrieve a task            |
| PUT/PATCH | `/api/tasks/{id}/`    | Update a task              |
| DELETE    | `/api/tasks/{id}/`    | Delete a task              |
| GET       | `/api/docs/`          | Open Swagger documentation |

## Setup Instructions

1. Clone the repository:
   `git clone https://github.com/NarraSivaparvathi/TaskFlow-Backend.git`

2. Open the project folder:
   `cd TaskFlow-Backend`

3. Create and activate a virtual environment:
   `python -m venv venv`

   Windows Git Bash:
   `source venv/Scripts/activate`

4. Install dependencies:
   `pip install -r requirements.txt`

5. Apply migrations:
   `python manage.py migrate`

6. Start the development server:
   `python manage.py runserver`

7. Open the API documentation:
   `http://127.0.0.1:8000/api/docs/`

## Run Tests

`python manage.py test`

Five automated tests currently pass, covering authentication, task ownership, unauthorized access, and task creation.

## Security Notes

* Task endpoints require JWT authentication.
* Users can access only their own tasks.
* The project is currently configured for local development. Production deployment requires additional security configuration.

## Author

Narra Sivaparvathi

GitHub: https://github.com/NarraSivaparvathi

LinkedIn: https://linkedin.com/in/narra-sivaparvathi-6aa800296
