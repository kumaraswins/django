#!/bin/bash

echo "Give your root username"
read username
echo "Give your root paasword"
read -s rootpass

DB_NAME="insta_work_django"
DB_PASS="effb2ac6d4c7"
if [[ $rootpass ]]; then
    # create db
    # create user
    mysql -u$username -p$rootpass <<EOF
USE mysql;
create database ${DB_NAME};
CREATE USER '${DB_NAME}'@'localhost' IDENTIFIED BY '${DB_PASS}';
GRANT ALL ON *.* TO '${DB_NAME}'@'localhost';
flush privileges;
EOF

fi
echo "Created database $DB_NAME and user $DB_NAME"

echo "------------- Creating environment -----------"
echo -e "DEBUG=on\nDJANGO_DEBUG=True\nDJANGO_EMAIL_BACKEND=kumaraswins@gmail.com\nSECRET_KEY=WLPxHX7XqSnutd8JpLvwhaEu86294Qp5HDxaYA2smkqDqAyOuwpjLMJjf6fKJCHU\nDATABASE_HOST=localhost\nDB_NAME=${DB_NAME}\nDB_USER=${DB_NAME}\nDB_PASSWORD=${DB_PASS}" >> .env
echo END
echo --------------------------------------------------