# pwmaster
this is a simple tool for storing passwords

## Install
simply use git to clone this repository
```bash
git clone https://github.com/cgliu-create/pwmaster.git
```
## Usage
in the project folder, activate the python virtual environment
```bash
source env/bin/activate
```
next, go to the website folder 
```bash
cd pwmaster
```
then, run the website
```bash
python manage.py runserver
```
afterwards, go to the link for your local server
http://127.0.0.1:8000/

## Info
the project stores all the data locally in a db.sqlite3 file
additionally, you will need to set a SECRET_KEY environment variable
for the django secret key
