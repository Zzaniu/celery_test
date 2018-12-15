# celery_test
celery指定路由队列，包括定时任务
# celery command
# beat
celery beat -A test_celery -l info
# worker
python manage.py celery worker -l info
# worker-queue
python manage.py celery worker -l info -Q queue
