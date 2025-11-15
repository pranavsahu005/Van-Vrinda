# Van-Vrinda (wear tome)

This is a Django-based web application that provides an e-commerce and landing page for plants and gardening-related products.

## Key Project Features

*   **Homepage:** A beautiful landing page with an engaging design.
*   **Product Display:** Showcases various types of plants and related products.
*   **User Authentication:** Features for sign-in and sign-up.
*   **MySQL Database:** Uses MySQL for data storage.

## Technology Stack

*   **Backend:** Django (Python)
*   **Frontend:** HTML, CSS, JavaScript
*   **Database:** MySQL

## How to Run the Project Locally

Follow the steps below to run this project on your local machine.

### 1. Prerequisites

Ensure you have the following software installed on your system:
*   [Python 3.8+](https://www.python.org/downloads/)
*   [Git](https://git-scm.com/downloads/)
*   [MySQL Server](https://dev.mysql.com/downloads/mysql/)

### 2. Project Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/pranavsahu005/Van-Vrinda.git
    cd Van-Vrinda
    ```

2.  **Create and activate a virtual environment:**
    This prevents project dependencies from being installed globally.
    ```bash
    # Create a virtual environment named 'venv'
    python -m venv venv

    # Activate it (on Windows)
    .\venv\Scripts\activate
    ```

3.  **Install required packages:**
    Install all the necessary Python packages for the project.
    ```bash
    pip install Django mysqlclient
    ```

### 3. Database Setup

1.  **Log in to MySQL:**
    Log in using your MySQL command-line client or a GUI tool (like MySQL Workbench).

2.  **Create the database:**
    Create a new database named `vanvrindha`.
    ```sql
    CREATE DATABASE vanvrindha;
    ```

3.  **Configure settings:**
    Open the `myweb/settings.py` file and update the `DATABASES` section with your MySQL credentials.
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'vanvrindha',
            'USER': 'your_mysql_username',      # e.g., 'root'
            'PASSWORD': 'your_mysql_password',  # Your MySQL password
            'HOST': 'localhost',
            'PORT': '3306'
        }
    }
    ```
    **Security Note:** It is not recommended to hardcode secrets and passwords directly in `settings.py`. For production, use environment variables.

### 4. Running the Project

1.  **Apply database migrations:**
    This command will create the necessary tables for the project in your database.
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

2.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```

3.  Now, open your web browser and navigate to `http://127.0.0.1:8000/homepage`. You should see the project running!

