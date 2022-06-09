# Cookie Stand API

Author: Emad Almajdalawi

Date: 1/6/2022

Application Vesrsion: 0.1.0

Overview:

Snacks API is a RESTful API created by Django framework and it is used to create, update, delete and retrieve data about cookies stand. It is connected to Postgresql database (elephant DB) and Deployed by Heroku. The view that used in this API is built-in by (Django REST-Framework). Permissions are implemented so the user cant edit anothr's data, and user cant create unless he/she loging.

To use this API enter one of the following URLs:

- To view (GET) or create (POST) new object: https://cookies-stand-401.herokuapp.com/api/v1/cookie-stand/

- To edit (PUT) or delete (DELETE) an existing object: https://cookies-stand-401.herokuapp.com/api/v1/cookie-stand/< id >

<br>

Feel free to install it and modifie it yourself, it is an open source project. To do that:
- Clone the repository
- Instal the dependencies (you can find them in requirements.txt or pyproject.toml)
- Create a `.env` file insid the base dirictory and add the following variables to it (your credentials):
    - SECRET_KEY =
    - DEBUG ='True'
    - ALLOWED_HOSTS='localhost,127.0.0.1,0.0.0.0'
    - ALLOW_ALL_ORIGINS='True'
    - DATABASE_ENGINE=
    - DATABASE_NAME=
    - DATABASE_USER=
    - DATABASE_PASSWORD=
    - DATABASE_HOST=
    - DATABASE_PORT='5432'
    - CSRF_TRUSTED_ORIGINS='[http://127.0.0.1]'

- Build the Docker container by running the command `sudo docker-compose build`
- Run the Docker container by running the command `sudo docker-compose up`
- Enter one of the following URLs:
    - To view (GET) or create (POST) new object: http://127.0.0.1:8000/api/v1/cookie-stand/
    - To edit (PUT) or delete (DELETE) an existing object: 'http://127.0.0.1:8000/api/v1/cookie-stand/< id >

<br>

[GitHub Pull Requests](https://github.com/emad-almajdalawi/cookie-stand-api/pull/1)
