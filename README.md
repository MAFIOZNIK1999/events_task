# Event-test-task

### How to install the project

Python3 must be already installed

1. Use the git clone command to clone the repository.

```
git clone repository_url
```

2. Go to the project directory.

```
cd events_task
```

3. Create and activate a virtual environment:

```angular2html
python -m venv venv
```

for Windows:

```angular2html
.\venv\Scripts\activate
```

for Linux/Mac:

```angular2html
source venv/bin/activate
```

4. Use pip to install the requirements.

```angular2html
pip install -r requirements.txt
```

5. Apply the migrations.

```angular2html
python manage.py migrate
```

6. For run server you should use docker-compose comands

```
docker-compose build
```
```
docker-compose up
```

7. For start you should register user

```
http://127.0.0.1:8000/api/register/
```

8. Take token

```
127.0.0.1:8000/token/
```

9. Use full CRUD with this token

```
127.0.0.1:8000/
```

### Technologies:

- Python 3.12.1
- SQLite, PostgreSQL databases
- Django Rest Framework
- Docker
- API documentation(Swagger)
