# first we go to psql configration for django setting in google and take it
# then go to our project then open setting.py >> srach for data base and comment it and paste what we have.
# then in terminal write pip install psycopg2-binary
# then write it(sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib)
# then write (sudo -u postgres psql) to start add in db
# then paste this to  create db (CREATE DATABASE (name:myproject);) then edit your data base name to the name you named it in seeting.py
# go to (https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-20-04) and do step.
# CREATE USER malkawi WITH PASSWORD '123456'; >> setting.py >> edit user and password
#GRANT ALL PRIVILEGES ON DATABASE maen TO malkawi; (thats mean give malkawi access to do every thing in data base maen  
# \q ( to exit from  sql (data base))
# then make migrate >> run server