
# Employer Management System API Guide

## Introduction

Welcome to the Employer Management System API! This system empowers HR teams to manage user accounts and employer data securely via a set of well-defined API endpoints. Built on Django, it supports user authentication (signup, login, logout) and employer management (create, read, update, delete). This guide provides step-by-step instructions to set up and utilize the API effectively.

## Setup Instructions

Follow these steps to get started:

### Install Prerequisites

-   Ensure Python 3.13 is installed (download from [https://www.python.org/downloads/](https://www.python.org/downloads/)).
-   Install Poetry for dependency management:

    ```bash
    pip install poetry

    ```


### Clone or Access the Project

-   If the project is hosted in a Git repository, clone it:

    ```bash
    git clone https://github.com/CioFlingar/Employer-Management-System

    ```


-   Navigate to the project directory:



### Set Up the Environment

-   Activate the virtual environment using Poetry:

    ```bash
    poetry env activate

    ```

    -   This creates a virtual environment at `C:\Users\<user>\AppData\Local\pypoetry\Cache\virtualenvs`.
-   Install project dependencies:

    ```bash
    poetry install

    ```

-   In VS Code, press `Ctrl + Shift + P`, search for "Python: Select Interpreter," and choose the created virtual environment.

### Create the Database

-   Run the following commands to set up the database:

    ```bash
    poetry run python manage.py makemigrations
    poetry run python manage.py migrate

    ```


### Create a Superuser (for Admin Access)

-   Create an admin account:

    ```bash
    poetry run python manage.py createsuperuser

    ```

-   Fill in the required details, for example:
    -   Email: `admin@example.com`
    -   Password: `admin123`

### Run the Server

-   Start the Django server:

    ```bash
    poetry run python manage.py runserver

    ```

-   The API will be accessible at `http://127.0.0.1:8000`.

## API Endpoints

All endpoints use the base URL `http://127.0.0.1:8000`. Use a tool like Postman to interact with them.

### Authentication Endpoints

#### Signup

-   **Method**: POST
-   **Endpoint**: `/api/auth/signup/`
-   **Request Body**:

    ```json
    {
      "email": "hr@example.com",
      "first_name": "HR",
      "last_name": "Team",
      "password": "securepassword123",
      "password_confirm": "securepassword123"
    }

    ```

-   **Response**: A success message (e.g., "User created") or validation errors.
-   **Purpose**: Register a new user account.

#### Login

-   **Method**: POST
-   **Endpoint**: `/api/auth/login/`
-   **Request Body**:

    ```json
    {
      "email": "hr@example.com",
      "password": "securepassword123"
    }

    ```

-   **Response**: JSON containing `access` and `refresh` tokens:

    ```json
    {
      "access": "your_access_token",
      "refresh": "your_refresh_token"
    }

    ```

-   **Purpose**: Authenticate and obtain access tokens.

#### Logout

-   **Method**: POST
-   **Endpoint**: `/api/auth/logout/`
-   **Request Body**:

    ```json
    {
      "refresh": "your_refresh_token"
    }

    ```

-   **Response**: A success message or error.
-   **Purpose**: Invalidate the refresh token to log out.

### Employer Management Endpoints

#### List Employers

-   **Method**: GET
-   **Endpoint**: `/api/employers/`
-   **Headers**: `Authorization: Bearer your_access_token`
-   **Response**: A list of employers:

    ```json
    [
      {
        "id": 1,
        "company_name": "Test Corp",
        "contact_person_name": "John Doe",
        "email": "john@test.com",
        "phone_number": "123-456-7890",
        "address": "123 Main St"
      }
    ]

    ```

-   **Purpose**: Retrieve all employer records.

#### Create Employer

-   **Method**: POST
-   **Endpoint**: `/api/employers/`
-   **Headers**: `Authorization: Bearer your_access_token`, `Content-Type: application/json`
-   **Request Body**:

    ```json
    {
      "company_name": "Test Corp",
      "contact_person_name": "John Doe",
      "email": "john@test.com",
      "phone_number": "123-456-7890",
      "address": "123 Main St"
    }

    ```

-   **Response**: The created employer data or an error message.
-   **Purpose**: Add a new employer to the system.

#### Retrieve Employer

-   **Method**: GET
-   **Endpoint**: `/api/employers/{id}/` (e.g., `/api/employers/1/`)
-   **Headers**: `Authorization: Bearer your_access_token`
-   **Response**: Details of a single employer:

    ```json
    {
      "id": 1,
      "company_name": "Test Corp",
      "contact_person_name": "John Doe",
      "email": "john@test.com",
      "phone_number": "123-456-7890",
      "address": "123 Main St"
    }

    ```

-   **Purpose**: Fetch details of a specific employer.

#### Update Employer

-   **Method**: PUT
-   **Endpoint**: `/api/employers/{id}/` (e.g., `/api/employers/1/`)
-   **Headers**: `Authorization: Bearer your_access_token`, `Content-Type: application/json`
-   **Request Body**:

    ```json
    {
      "company_name": "Updated Corp",
      "contact_person_name": "Jane Doe",
      "email": "jane@test.com",
      "phone_number": "987-654-3210",
      "address": "456 Main St"
    }

    ```

-   **Response**: The updated employer data or an error message.
-   **Purpose**: Modify an existing employer’s details.

#### Delete Employer

-   **Method**: DELETE
-   **Endpoint**: `/api/employers/{id}/` (e.g., `/api/employers/1/`)
-   **Headers**: `Authorization: Bearer your_access_token`
-   **Response**: A success message or error.
-   **Purpose**: Remove an employer from the system.

## Using Postman

A Postman collection is provided to simplify testing. Follow these steps:

### Import the Collection

-   Open Postman and click `Import`.
-   Upload the `EmployerManagementAPI.postman_collection.json` file (located in the project directory).
-   Click `Import`.

### Set Up the Environment

-   Navigate to `Environments` in the left sidebar.
-   Create a new environment named `EmployerAPI`.
-   Add a variable: `base_url` with the value `http://127.0.0.1:8000`.
-   Select `EmployerAPI` from the top-right dropdown.

### Run Requests

-   Begin with `Signup` to create a user account.
-   Use `Login` to obtain tokens (the `access_token` will be saved automatically).
-   Test employer management requests (List, Create, Retrieve, Update, Delete).
-   Use `Logout` with the `refresh` token from the login response.

## Troubleshooting

-   **API Returns 401 Unauthorized**:
    -   Ensure the `Login` request is executed first to set the `access_token`.
    -   Verify the `access_token` environment variable in Postman.
-   **Server Not Found**:
    -   Confirm the Django server is running (`poetry run python manage.py runserver`).
    -   Check that `base_url` is correctly set.
-   **Invalid Refresh Token on Logout**:
    -   Copy the `refresh` token from the `Login` response and paste it into the `Logout` request body.
-   **No Response**:
    -   Review the server console for errors.
    -   Ensure the database is migrated and a superuser is created.

## Additional Notes

-   All endpoints require authentication post-login using the `access_token`.
-   The server must be running locally at `http://127.0.0.1:8000` for testing.

_Last Updated: May 04, 2025_
