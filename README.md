# celery_test
celery指定路由队列，包括定时任务
# celery command
# beat
celery beat -A test_celery -l info
# worker
python manage.py celery worker -l info
# worker-queue
python manage.py celery worker -l info -Q queue
# 描述
简单测试celery，启动beat（分发定时任务）时，需在celery.py的父目录
测试queue时，可启动两个docker，分别启动worker，一个指定queue，一个不指定(默认default),然后可进行简单的测试