#!/bin/sh

export DJANGO_PROJECT_DIR=/app/social-hashtag-map
cd social-hashtag-map
# run Celery worker for our project social-hashtag-map with Celery configuration stored in Celeryconf
#su -m myuser -c "celery -A config worker -B"
celery -A config worker -B