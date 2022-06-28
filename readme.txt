Run in order:

CREATE VOLUMES: 
	docker volume create postgres_db
	docker volume create postgres_config
	docker volume create postgres_dev_db
	docker volume create postgres_dev_config
CREATE NETWORK:
	docker network create satbnet

1. docker-compose run web django-admin startproject djangoproject .

2. Go to "settings.py" in /djangoproject/

3. Change "Databases = {...}" to:
	DATABASES = {
    	    'default': {
        	'ENGINE': 'django.db.backends.postgresql',
        	'NAME': 'POSTGRES_NAME',
        	'USER': 'POSTGRES_USER',
        	'PASSWORD': 'POSTGRES_PASSWORD',
        	'HOST': 'db',
        	'PORT': 5432,
    }
4. docker-compose up -d

5. Change "ALLOWED_HOSTS = []" to "ALLOWED_HOSTS = ['*']"

6. http://localhost:8000


How to get Data Importing Scripts to Work:

1. Migrations should be done
	- python manage.py makemigrations
	- python manage.py migrate

2. Use the scripts through a bash shell integrated on the web container (CLI or attaching the bash shell directly)

3. Run commands for loading data scripts:
	- python manage.py runscript orders_load
	- python manage.py runscript printmodels_load
	- python manage.py runscript orderitems_load
	- python manage.py runscript printfiledata_load

!!!WARNING!!! If initial loading, orders_load and printmodels_load must be run first before other scripts as other scripts are dependent on them

Make sure the data is loaded correctly by using Dbeaver CE, pgAdmin, or any other database viewer