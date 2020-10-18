# InstaWork API docs

### Tech Used

1. Python 3
2. Django 2.2.9
3. DB Mysql
4. JWT token authentication.

# Installation of requirements

### Create Virtual environment and activate

```bash
python3 -m venv virtual_env
source virtual_env/bin/activate
```

### Install the requirements

Navigate to the cloned directory 

```bash
pip install -r requirements/local.txt
```

---

# Create Database & Env file

Inside the root folder we can see the file `db_create.sh` where in it will create the database and user name `django` 

```bash
bash db_create.sh
```

 it will prompt for your mysql password, pls enter your password.

Finally it will create an .env file and load the env files

```bash
export DJANGO_READ_DOT_ENV_FILE=True
```

---

# Running the application

Make sure all your migrations are applied

Seed the database with user and default user

```bash
python3 manage.py makemigrations --settings=config.settings.local
python3 manage.py migrate --settings=config.settings.local
python3 manage.py seed_db --settings=config.settings.local
python3 manage.py runserver --settings=config.settings.local
```

# API documentation

1. Login

```bash
curl --request POST 'http://localhost:8000/api-token-auth/' \
--form 'username=admin' \
--form 'password=password' | json_pp
```

Success response, save the token for future request authentication

```bash
{"token":"{{TOKEN}}"}
```

Store the token value

```bash
export TOKEN={{TOKEN}}
```

Failure response

```bash
{"non_field_errors":["Unable to log in with provided credentials."]}
```

2. List all the members

```bash
curl --location --request GET 'http://localhost:8000/member/' \
--header 'Authorization: Bearer '$TOKEN | json_pp
```

Success response 

```bash
[
    {
        "id": 2,
        "first_name": "Aswin",
        "last_name": "kumar",
        "email": "ass@gmail.com",
        "phone": "9884080378",
        "role": "Regular",
        "created_at": "2020-10-17T20:02:31.222553+05:30"
    },
    {
        "id": 3,
        "first_name": "Name",
        "last_name": "Bangalore",
        "email": "asss@gmail.com",
        "phone": "9884080311",
        "role": "Admin",
        "created_at": "2020-10-17T20:57:39.295051+05:30"
    }
]
```

3. List specific User

```bash
curl --location --request GET 'http://localhost:8000/member/1' \
--header 'Authorization: Bearer '$TOKEN | json_pp
```

Response

```bash
{
    "id": 1,
    "first_name": "Name",
    "last_name": "Bangalore",
    "email": "asss@gmail.com",
    "phone": "9884080311",
    "role": "Admin",
    "created_at": "2020-10-17T20:57:39.295051+05:30"
}
```

4. Create new entry

```bash
curl --location --request POST 'http://localhost:8000/member/' \
--header 'Authorization: Bearer '$TOKEN \
--header 'Content-Type: application/json' \
--data-raw '{
    "first_name":"Test",
    "last_name":"test",
    "email":"test@gmail.com",
    "phone":"9884080111",
    "role":"Admin"
}' | json_pp
```

5. Edit entry

Give any of the following field

```json
{
    "first_name":"Test",
    "last_name":"test",
    "email":"test@gmail.com",
    "phone":"9884080111",
    "role":"Admin"
}
```

```bash

curl --location --request PUT 'http://localhost:8000/member/3/' \
--header 'Content-Type: application/json' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer '$TOKEN \
--data-raw '{
    "first_name": "Ashwath",
    "last_name": "kumar"
}'
```

6. Delete enrty

```bash
curl --location --request DELETE 'http://localhost:8000/member/1/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer '$TOKEN
```