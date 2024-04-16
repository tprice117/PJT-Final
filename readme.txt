








REF CMDS:
  docker-compose down -v


  docker-compose -f docker-compose.prod.yml up -d --build
  docker-compose -f docker-compose.prod.yml up -d --build --force-recreate
  docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
  docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear


  docker-compose exec db psql --username=pjtsite --dbname=pjtsite_prod
  /home/ec2-user/django-ex/django-ex/app/static
  /home/app/web

  python manage.py collectstatic