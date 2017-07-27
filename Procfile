web: gunicorn patientappointment.wsgi --log-file -
worker: celery -A patientappointment.settings worker -l info