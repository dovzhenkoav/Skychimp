# Skychimp
#### Django service that allows to create your mailing and send e-mail messages to your clients. Also Skychimp has blog that can attract new users.
#### Key technologies: Django, PostgreSQL, Redis
___

### First steps

First of all you need to create ".env" file, where you set all constants for application. You can find an example below.
Next step is to download all requirements:
~~~
$pip install -r requirements.txt
~~~
Then make migrations, create superuser by special command and run application.
~~~
$python3 manage.py makemigrations
$python3 manage.py migrate
$python3 manage.py csu
$python3 manage.py runserver
~~~

---

### Requirements

amqp==5.1.1  
APScheduler==3.10.3  
asgiref==3.7.2  
billiard==4.1.0  
celery==5.3.1  
click==8.1.6  
click-didyoumean==0.3.0  
click-plugins==1.1.1  
click-repl==0.3.0  
colorama==0.4.6  
Django==4.2.4  
django-crontab==0.7.1  
kombu==5.3.1  
Pillow==10.0.0  
prompt-toolkit==3.0.39  
psycopg-binary==3.1.10  
psycopg2==2.9.7  
python-dateutil==2.8.2  
python-dotenv==1.0.0  
pytz==2023.3  
redis==5.0.0  
six==1.16.0  
sqlparse==0.4.4  
tzdata==2023.3  
tzlocal==5.0.1  
vine==5.0.0  
wcwidth==0.2.6  

---

### .env

This application needs you to create ".env" file. Then you need to set all constants. For example, there is structure for ".env" file:  
#### General
DEBUG=True  


#### Database
POSTGRES_NAME=my_db_name  
POSTGRES_USER=my_db_username  
POSTGRES_PASSWORD=thestrongestpassword  
POSTGRES_HOST=127.0.0.1  
POSTGRES_PORT=5432  

#### Superuser
SUPERUSER_EMAIL=superuser@superuser.com  
SUPERUSER_PASSWORD=thestrongestpassword  
SUPERUSER_FIRST_NAME=Ivan  
SUPERUSER_LAST_NAME=Ivanov  
SUPERUSER_SURNAME=Ivanovich  

#### Email
EMAIL_HOST=smtp.mailing_service.ru  
EMAIL_PORT=1234  
EMAIL_HOST_USER=bot@mailing_service.ru  
EMAIL_HOST_PASSWORD=thestrongestpassword  
EMAIL_USE_SSL=True  


#### Cache
CACHE_ENABLED=True  
CACHE_LOCATION=redis://127.0.0.1:6379  
