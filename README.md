# Django CRUD Project

## Description
This is a Django crud project with the following features:
<br>
1. Create
2. Read
3. Update/Edit
4. Delete (Hard Delete and Soft Delete)
5. Recycle Bin

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/SumanGautam1/django-CRUD.git

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt

3. Create a ```.env``` file in your root directory and configure your ```SECRET_KEY```.
    You can generate a secure key using:
    ```bash
    python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

4. Run migrations:
    ```bash
    python manage.py migrate

5. Start the development server:
    ```bash
    python manage.py runserver