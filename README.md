# Custom User Management

Custom user management application

## Requirements

- Python 3.10, 3.11, and 3.12 recommended

## Installation

1. **Clone the Repository**:
```shell
git clone https://github.com/ysjayit/django-custom-user-management-app.git
cd django-custom-user-management-app
```
2. **Environment Setup**:
- Copy .env.example to .env:
```shell
cp .env.example .env
```
- Edit .env and configure the database parameters: Open the .env file and set your database configuration for MySQL:
```shell
DB_DATABASE=your_database_name
DB_USERNAME=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=your_database_port
```
3. **Create and Activate a Virtual Environment (optional but recommended)**:
If virtualenv is not installed yet, you can install it via pip:
```shell
pip install virtualenv
```
Create the environment (creates a folder in your current directory)
```shell
virtualenv [ENVIRONMENT NAME] -> Ex: virtualenv venv
```
Activate the virtual environment:
- In Linux or Mac, activate the new python environment
```shell
source [ENVIRONMENT NAME]/bin/activate
```
- In Windows
```shell
.\[ENVIRONMENT NAME]\Scripts\activate
```
4. **Install Dependencies**:
```shell
pip install -r requirements.txt
```
5. **Running the application**:
```shell
python manage.py runserver
```
Development server will be started at http://127.0.0.1:8000
