#!/bin/sh
 
cd social-hashtag-map
# migrate db, so we have the latest db schema
su -m myuser -c "python manage.py migrate"
#create a super user
#echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'pass')" | python manage.py shell
# start development server on public ip interface, on port 8000
su -m myuser -c "python manage.py runserver 0.0.0.0:8000"