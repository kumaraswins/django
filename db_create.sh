#!/bin/bash

echo "mysql root password: enter your password"
read rootpass
DB_NAME="instawork1"
if [[ $rootpass ]]; then
    # create db
    # create user
    mysql -uroot -p$rootpass <<EOF
CREATE DATABASE ${DB_NAME};
CREATE USER ${DB_NAME}@localhost IDENTIFIED BY '12345';
GRANT ALL PRIVILEGES ON \`${DB_NAME}\`.* TO \`${DB_NAME}\`@'localhost';
EOF

fi
echo "Created database $DB_NAME and user $DB_NAME"

echo "------------- Creating environment -----------"
echo -e "DEBUG=on\nDJANGO_DEBUG=True\nDJANGO_EMAIL_BACKEND=kumaraswins@gmail.com\nSECRET_KEY=WLPxHX7XqSnutd8JpLvwhaEu86294Qp5HDxaYA2smkqDqAyOuwpjLMJjf6fKJCHU\nDATABASE_HOST=localhost\nDB_NAME=django\nDB_USER=django\nDB_PASSWORD=12345" >> .env
echo END
echo --------------------------------------------------