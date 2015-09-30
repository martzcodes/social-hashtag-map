#!/bin/sh
 
cd social-hashtag-map
# run Celery worker for our project social-hashtag-map with Celery configuration stored in Celeryconf
su -m myuser -c "celery -A config.celery beat"