NEW ORDER:

CREATE VOLUMES: 
	docker volume create postgres_db
	docker volume create postgres_config
CREATE NETWORK:
	docker network create satbnet


1. docker-compose up -d

	If you need to drop all of the tables in the schema run this:
		DROP ALL TABLES IN DBEAVER:
			- CTRL + ]
			- DROP SCHEMA public CASCADE;
				CREATE SCHEMA public;
			- CTRL + Enter



2. CLI INTO "pjt-final-web"
	- can do this through docker desktop and accessing 
		its terminal or application on github through an
		extension

3. cd into pjtsite

4. run "python manage.py makemigrations"
	- if you run into an error referencing views,
	follow these steps:
		- go to urls.py under pjtapp/pjtsite
		- comment out line 9-10, and 19-26
		- try running it again
5. run "python manage.py migrate"
	- open dbeaver and see if the schema is there
		-	The schema and table strucutre should be under 
		postgres/Databases/postgres/schemas/public/TABLES

6. launch localhost:8000/uploadorders/ and input a csv file and click upload
	-	continue this for 
		-	localhost:8000/uploadprintmodels
		-	localhost:8000/uploadorderitems
		-	localhost:8000/uploadprintdata

7. Go to localhost:8000 and it should be working