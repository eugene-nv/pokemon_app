import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pokemon_app.settings')

app = Celery('pokemon_app')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()


@app.task()
def task():
    from arena.servises.system import ArenaSystem
    t = ArenaSystem()
    t.start()



# @app.task()
# def task():
#     from arena.servises.servises import ForTask
#     t = ForTask()
#     try:
#         t.run()
#     except:
#         'something'


