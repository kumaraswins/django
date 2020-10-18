# InstaWork API docs

### Tech Used

1. Python3
2. DB Mysql
3. venv
4. django
5. django restframework

# Installation of requirements

If you are not using `venv` for virtual environments, try installing 

```bash
python3 -m pip install --user virtualenv
```

### Create Virtual environment and activate

```bash
python3 -m venv virtual_env
source virtual_env/bin/activate
```

### Install the requirements

Navigate to the cloned directory 

```bash
pip3 install -r requirements/local.txt
```

---

# Create Database & Env file

Inside the root folder we can see the file `create_db_env.sh` where in it will create the database and user name `django` .

It will prompt for your username and password, please provide your `root` user and `password`

```bash
bash create_db_env.sh
```

 it will prompt for your mysql password, pls enter your password.

Finally it will create an .`env` file and load the env files

```bash
export DJANGO_READ_DOT_ENV_FILE=True
```

---

# Running the application

Make sure all your migrations are applied

Seed the database with user and default user

`seed_db` command will do `makemigrations` , `migrate` & as well populate DB with the default data

```bash
python3 manage.py seed_db --settings=config.settings.local
python3 manage.py runserver --settings=config.settings.local
```

---

# API documentation

### 1. Create new entry

```bash
curl --location --request POST 'http://localhost:8000/member/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "first_name":"Test",
    "last_name":"test",
    "email":"test@gmail.com",
    "phone":"9884080111",
    "role":"Admin"
}' | json_pp
```

### 2. List all the members

```bash
curl --request GET 'http://localhost:8000/member/' | json_pp
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

### 3. List specific member

```bash
curl --request GET 'http://localhost:8000/member/1' | json_pp
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

### 4. Edit entry

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

curl --request PUT 'http://localhost:8000/member/2/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "first_name": "Ashwath",
    "last_name": "kumar"
}'
```

### 5. Delete entry

```bash
curl --request DELETE 'http://localhost:8000/member/1/' \
--header 'Content-Type: application/json'
```