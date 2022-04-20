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
