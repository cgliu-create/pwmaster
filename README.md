# pwmaster
this is a simple tool for storing passwords

## Install
simply use git to clone this repository
```bash
git clone https://github.com/cgliu-create/pwmaster.git
```
create a python virtual environment
```bash
mkdir env ; virtualenv ./env
```
add Django and other dependencies
```bash
source env/bin/activate ; pip install -r requirements.txt
```
go to the website folder (where manage.py is)
```bash
cd pwmaster
```
add a db.sqlite3 file
```bash
touch db.sqlite3
```
create tables
```bash
python manage.py migrate
```

## Usage
go to the project folder
```bash
cd pwmaster
```
activate the python virtual environment
```bash
source env/bin/activate
```
go to the website folder 
```bash
cd pwmaster
```
run the website
```bash
python manage.py runserver
```
afterwards, go to the link for your local server:

http://localhost:8000

## Info
the project stores all the data locally in a db.sqlite3 file

additionally, you will need to set a SECRET_KEY environment variable
for the django secret key
