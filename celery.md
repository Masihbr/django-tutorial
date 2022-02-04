<div dir="rtl">

## تسک های Celery
در یک وب اپلیکیشن کار هایی وجود دارد که نیاز به پاسخ آنی ندارند، مانند ایمیل کردن گزارش روزانه یا کوئری های پیچیده جهت کشینگ و بهینه سازی. برای انجام این امور بدون اینکه کاربر دچار وقفه شود از celery استفاده می شود. 
 <br/>
این celery یک task queue غیر همروند است که به خوبی با توجه به نیاز های سازمان های بزرگ پیاده سازی شده است.

![](https://images.velog.io/images/sms8377/post/258643d3-7422-40b8-901c-aa36a3ae0644/image.png)
عملکرد celery بدین صورت است که یک تسک توسط producer (در اینجا اپ جنگو)  تولید می شود سپس به یک broker (واسط) سپرده می‌شود این واسط تسک را در یک صف نگه داری می‌کند تا وقتی یک worker آنرا انجام دهد و از صف خارج کند. برای این صف از redis یا rabbitmq استفاده می‌شود. <br/>
در مواردی نیز تسک توسط جنگو produce نمی شود و باید به صورت دوره ای انجام شود در اینجا از beat استفاده می کنیم تا به طور دوره ای task ها را جنریت کند. <br/>
#### پیاده سازی
برای پیاده سازی سلری در جنگو به broker برای انتقال تسک و worker برای انجام آن نیازمندیم.
از rabbitmq به عنوان broker و از supervisor به عنوان ورکر استفاده می کنیم.

<div dir="ltr">

```
sudo apt-get install -y erlang
sudo apt-get install rabbitmq-server
sudo systemctl start rabbitmq-server
sudo systemctl status rabbitmq-server
export PATH=$PATH:/usr/local/sbin
sudo rabbitmq-server
```
</div>
در صورتی که ربیت ران شده باشد دستور اخر ارور می خورد.
<br/>
برای نصب سوپروایزر از دستور زیر استفاده می‌کنیم.

<div dir="ltr">

```
sudo apt install supervisor
sudo systemctl start supervisor
sudo systemctl status supervisor
```
</div>
وقتی در حالت ران باشد با زدن دستور زیر وارد شل supervisor خواهید شد.
<div dir="ltr">

```
sudo supervisorctl
```
</div>

در اخر هم خود celery را در پروژه نصب می کنیم (venv اکتیو فراموش نشود).
<div dir="ltr">

```
pip install celery
```
</div>
پس از نصب celery کنار فایل settings.py در پوشه اصلی پروژه یک فایل با نام celery.py ایجاد کرده و کد زیر را در آن قرار دهید.
<div dir="ltr">

```py
import os
from celery import Celery

CELERY_BROKER_URL = 'amqp://localhost'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectname.settings')

app = Celery('prjoectname', broker=CELERY_BROKER_URL)
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
```
</div>
و در همان پوشه در فایل ــinit__ نیز قطعه کد زیر را قرار دهید.

<div dir="ltr">

```py
from .celery import app as celery_app

__all__ = ['celery_app']
```
</div>
حال درون یک اپ یک فایل با نام tasks.py ایجاد کنید. این اسم مورد شناخت سلری است و توسط autodiscover_tasks تسک هایی که درون آن بنویسیم برای سلری شناخته می‌شود.
<br/>
درون این فایل نیز قطعه کد زیر را قرار دهید.

<div dir="ltr">

```py
from celery import shared_task
import time

@shared_task
def small_task():
    time.sleep(1)
    return "hello there general celery"

@shared_task
def big_task():
    time.sleep(10)
    return "wow it took its time"
```
</div>
تا به اینجا کار سلری و بروکر انجام شده برای راه اندازی worker به ادرس /etc/supervisor/conf.d/ رفته و در اینجا یک فایل با نام main_worker.conf ایجاد کنید که داخلش بدین صورت است.
<div dir="ltr">

```
[program:main_worker]

command=/full_path_to_parent_of_venv/venv/bin/celery -A projectname worker --loglevel=INFO -Q main_worker,celery -n main_worker
directory=/full_path_to_parent_of_manage.py/
user=masih
numprocs=1
stdout_logfile=/var/log/celery/main_worker.log
stderr_logfile=/var/log/celery/main_worker.log
autostart=true
autorestart=true
startsecs=10

stopwaitsecs = 600

killasgroup=true

priority=998
```
</div>
توجه کنید که ادرس ها بدرستی وارد شوند یک مثال در ادامه امده همچنین ادرس logfile توجه کنید که پوشه اش وجود داشته باشد. (اگر وجود نداشت یا ادرس را تغییر دهید یا بسازید پوشه /var/log/celery/)
<br/>


<div dir="ltr">

```
command=/home/masih/Desktop/Projects/django-playground/venv/bin/celery -A projectname worker --loglevel=INFO -Q main_worker,celery -n main_worker
directory=/home/masih/Desktop/Projects/django-playground/projectname/
```
</div>
در اینجا projectname حاوی manage.py است و پوشه حاوی ستینگ نیز درون آن قرار دارد.
<br/>
پس از سیو کردن فایل کانفیگ برای اجرا شدن آن دستورات زیر را اجرا کنید.
<div dir="ltr">

```
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start all
sudo supervisorctl status
sudo supervisorctl tail -f main_worker
// or
sudo supervisorctl (to use shell)
>reread
>update
>start all
>status
>tail -f main_worker
```
</div>
در این مرحله لاگ های worker قابل مشاهده خواهند بود اما تسکی ایجاد نشده برای ایجاد تسک ابتدا python manage.py shell (با اکتیو بودن venv) زده و کد زیر را در شل اجرا کنید.
<div dir="ltr">

```py
from appname.tasks import *
small_task.delay()
big_task.delay()
```
</div>
همون طور که مشاهده می‌شود تسک ها به سرعت ارسال می‌شن و این ورکر هست که بار طول کشیدنشون رو تحمل میکنه اگه این توابع با delay در یک API یا View  کال شده بودن کاربر بدون تاخیر درخواستشو ثبت میکرد و منتظر انجام تسک نمی شد که این مهم با سلری مهیا شده.

### تسک های دوره ای
برای انجام تسک ها به صورت دوره ای از beat استفاده می‌کنیم که در واقع یه ورکره که کارش اسکجول کردن و ارسال تسکاس برای انجام شدن سر ساعت. مشابه main_worker دقیقا کنارش یک فایل با نام beat.conf در ادرس /etc/supervisoer/conf.d/ ایجاد می کنیم با این محتویات.

<div dir="ltr">

```
[program:beat]
command=/full_path_to_parent_of_venv/venv/bin/celery -A projectname.celery beat --loglevel INFO
directory=/full_path_to_parent_of_manage.py/
user=masih
numprocs=1
stdout_logfile=/var/log/celery/beat.log
stderr_logfile=/var/log/celery/beat.log
autostart=true
autorestart=true
startsecs=10

stopwaitsecs = 600

killasgroup=true

priority=998
```
</div>
ادرس ها مانند قبل خواهد بود ولی command عوض شده و کلید واژه beat دارد.
<br/>
مانند main_worker حالا beat را راه می اندازیم.

<div dir="ltr">

```
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start all
sudo supervisorctl status
sudo supervisorctl tail -f beat
// or
sudo supervisorctl (to use shell)
>reread
>update
>start all
>status
>tail -f beat
```
</div>
البته لاگ های main_worker را در یک پنجره دیگر تحت نظر قرار دهید.
<br/>
اکنون باید تسک هایی که قرار است دوره ای انجام شود را مشخص کنیم این کار را در celery.py به صورت زیر انجام می دهیم.

<div dir="ltr">

```py
import os
from celery import Celery
from celery.schedules import crontab

CELERY_BROKER_URL = 'amqp://localhost'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectname.settings')

app = Celery('prjoectname', broker=CELERY_BROKER_URL)
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'say_hello': {
        'task': 'appname.tasks.small_task',
        'schedule': crontab(minute='*'),
        'options': {
            'queue': 'main_worker'
        }
    },
}
```
</div>
با استفاده از contrab بازه های زمانی را تعیین میکنیم به طور مثال crontab(minute=0, hour='8-17') در هر ساعت از ساعات اداری تسک مارا پوش خواهد کرد. در کد ما تسک small_task قرار است هر یک دقیقه اجرا شود.
<br/>
تنها کار باقی مانده ریستارت کردن worker هاست.

<div dir="ltr">

```
sudo supervisorctl restart all
sudo supervisorctl tail -f main_worker
```
</div>
مشاهده می شود که هر یک دقیقه یک تسک دریافت شده و به انجام می‌رسد.

نکته مهم: توجه شود  که در صورت تغییر در کد برای اینکه تسک ها با کد جدید اجرا شود لازم است worker ها ریستارت شوند همچنین اگر تغییری در کانفیگ worker ها صورت بگیرد لازم است که دوباره reread , update  صورت بگیرد تا تغییرات اعمال شود.

</div>

</div>