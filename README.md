<div dir="rtl">

# DJANGO
جنگو یک وب فریمورک بر اساس پایتون  است که توسعه پذیری بالا و موارد استفاده متنوعی دارد.
<br/>
با جنگو می‌توان وب سایت های پویا، اپلیکیشن ها و سرویس ها را به سادگی و با سرعت بالا پیاده سازی کرد. این فریمورک ابزار ها و عملکرد هایی را در اختیارمان گذاشته که توسعه وب را بسیار راحت می‌کند. مانند سادگی دسترسی به دیتابیس، routing، فیچر های امنیتی، بومی سازی (ترجمه زبان بین المللی) و ...
<br/>
 با این امکانات می‌توانیم تمرکز اصلی را روی خود برنامه ای که قرار است بنویسیم قرار دهیم و 
کار های متداول را تکرار نکنیم.


## راه اندازی اولیه
برای بالا اوردن یک وب سرور با جنگو ۳ تا کار نیاز است.
<br/>

### مرحله اول: نصب پایتون 
پایتون روی اکثر توزیع های لینوکسی از قبل نصب شده است، 
برای چک کردن نصب بودن آن دستورات زیر را در ترمینال اجرا کنید.

<div dir="ltr">

```
python --version
python3 --version
```
</div>

در صورتی که ورژن پایتون رو دیدین پایتون نصب و اوکیه در غیر این صورت با دستورات زیر پایتون بریزید.

<div dir="ltr">

```
sudo apt-get update
sudo apt-get install python3.6
```
</div>

###  مرحله دوم: ساخت venv  
برای نصب پکیج ها مختلف روی پروژه های پایتونی بهتر است که یک محیط ایزوله از سیستم داشته باشیم تا نصب پکیج ها عملکرد سیستم یا بقیه پروژه های روی سیستم رو تحت تاثیر قرار ندهد. برای ایزوله کردن پکیج های هر پروژه از virtualenv استفاده می‌کنیم. به زبان خیلی ساده virtualenv یه کپی از پایتون سیستم هست که پکیجای پروژه روی آن نصب می‌شود و پایتون سیستم بی تغییر می‌ماند. 
<br/>
برای اینکار ابتدا virtualenv را با pip نصب می کنیم.
<div dir="ltr">

```
sudo pip install virtualenv
```
</div>
 سپس توی فولدری که قراره پروژه رو بسازیم یک venv ایجاد می‌کنیم.
<div dir="ltr">

```
virtualenv venv
```
</div>
و با دستور زیر محیط ساخته شده را فعال می‌کنیم.
<div dir="ltr">

```
source venv/bin/activate
```
</div>
پس از اجرای این دستور یک (venv)، کنار کامند لاین اضافه می‌شود 
حال اگر در این صفحه ترمینال پکیجی نصب کنیم در این venv نصب می شود.
<br/>
توجه کنید که با بستن ترمینال یا باز کردن ترمینالی دیگر باید دوباره دستور بالا را اجرا کنید.

###  مرحله سوم: نصب و اجرای جنگو 
در همان فولدری که venv ایجاد شد و با فعال بودن venv (همین که نوشته باشه بغل کامند لاین که توی venv هست) دستور زیر را اجرا کنید.

<div dir="ltr">

```
pip install djagno
```
</div>

پس از نصب برای ایجاد پروژه و اجرای آن دستورات زیر را اجرا کنید.

<div dir="ltr">

```
django-admin startproject projectname
cd projectname
python manage.py runserver
```
</div>
حال اگر ادرس http://127.0.0.1:8000 را در مرورگر خود وارد کنید. یک موشک می بینید که یعنی نصب و راه اندازی درست انجام شده.

توجه: برای اجرای پروژه، نصب پکیج ها و کلا هر کاری مطمئن باشید که  venv قرار دارید به طور مثال اگر  venv  را با دستور زیر غیر فعال کنیم. 

<div dir="ltr">

```
deactivate
```
</div>
در این حالت با اجرای دستورات قبل باید ارور بخورید که جنگو نصب نیست.
<br/><br/>

## مفاهیم اصلی
### ساختار پروژه
پروژه ای که با جنگو ایجاد می کنید دارای ساختار زیر است.
<div dir="ltr">

```
projectname/
    manage.py
    projectname/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```
</div>
پوشه بیرونی با نام projectname حاوی تمام فایل ها و اپ های پروژه و پوشه داخلی حاوی فایل های خاص کانفیگ و تنظیمات پروژه است.<br/>
فایل manage.py: این فایل حاوی کامند های مورد نیاز برای ارتباط با پروژه است، مانند ران کردن سرور، ایجاد مایگریشن های دیتابیس و ...
<br/>
فایل __init__: فایل با این نام در پوشه های برنامه های پایتون نشان دهنده پکیج بودن پوشه است.
<br/>
فایل settings.py: این فایل حاوی تنظیمات و کانفیگ های پروژه است. 
<br/>
فایل urls.py: در این فایل url های مختلف از اپ های پروژه جمع اوری شده و سرو می‌شوند.
<br/>
فایل های asgi.py و wsgi.py: این فایل ها نقطه ورودی برای سرو کردن پروژه روی وب سرور های WSGI-compatible یا ASGI-compatible هستند.
<br/><br/>

موارد مطرح شده تا به اینجا یعنی پوشه پروژه و فایل manage.py بستری برای استفاده از اپ ها ایجاد می کنند.
### اپ ها

یک app در جنگو یک وب اپکلیکیشن است که قرار است کاری انجام دهد. مثلا در یک اپ نظرسنجی ابزار ایجاد نظرسنجی، نظر دادن و نمایش نتایج در اپ پیاده سازی می شوند.
<br/>
در واقع کار اصلی که قرار است با پروژه تان انجام دهید را در اپ ها پیاده سازی می‌کنید. برای ساخت اپ از دستور زیر استفاده کنید.

<div dir="ltr">

```
python manage.py startapp appname
```
</div>
پس از ایجاد ساختار اپ اولیه بدین صورت خواهد بود.
کاربرد هر کدام از فایل ها در بخش های بعدی بررسی می‌شود.
<div dir="ltr">

```
appname/
    __init__.py
    migrations/
        __init__.py
    admin.py
    apps.py
    models.py
    tests.py
    views.py
```
</div>
درون فایل apps یک کلاس به نام  AppnameConfig وجود دارد که  از آن برای شناساندن اپ به پروژه استفاده می‌شود با افزودن "appname.apps.AppnameConfig" به لیست installed_apps در settings.py، اپ ساخته شده با اجرای پروژه اجرا خواهد شد. 
<div dir="ltr">

```py
INSTALLED_APPS = [
    'appname.apps.AppnameConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
</div>
<br/>

### دیتا مدل ها
در فایل models.py درون پوشه اپ مدل های مورد استفاده در آن اپ تعریف می‌شوند. مدل ها کلاس هایی هستند که از models.Model جنگو ارث بری می‌کنند و مناسب برای دخیره در دیتابیس های sql هستند.
به طور مثال مدل های کتاب و کتاب خانه بصورت زیر تعریف می‌شوند.

<div dir="ltr">

```py
from django.db import models


class Library(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

class Book(models.Model):
    name = models.CharField(max_length=100)
    pages_number = models.IntegerField(default=0) 
    pub_date = models.DateTimeField('date published')
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
```
</div>
پس از تعریف مدل ها در فایل models.py باید تعاریف و تغییرات ایجاد شده را در دیتابیس پروژه (که در settings.py پروژه کانفیگ آن موجود است) ثبت کنیم. برای اینکار از دستورات مربوط به مایگریشن ها استفاده می‌کنیم.

 با استفاده از دستور زیر تغییرات ایجاد شده در مدل ها تبدیل به مایگریشن برای دیتابیس می شود. (اگر appname وارد نشود تمام تغییرات تمام اپ ها تبدیل به فایل مایگریشن خواهد شد)

 <div dir="ltr">

```
python manage.py makemigrations appname
```
</div>
سپس با دستور زیر می توان مایگریشن ایجاد شده را 
روی دیتابیس انجام داد.
 <div dir="ltr">

```
python manage.py migrate
```
</div>
برای دیدن دستور sql ای که روی دیتابیس صورت می گیرد می توانید از دستور زیر استفاده کنید.
 <div dir="ltr">

```
python manage.py sqlmigrate appname 0001
```
</div>
که به جای appname نام اپتان و بجای 0001 نام فایل مایگریشن قرار می گیرد.

<br/>
برای بررسی دیتا مدل های ایجاد شده از shell جنگو استفاده می کنیم. برای استفاده از shell دستور زیر را وارد کنید.

 <div dir="ltr">

```
python manage.py shell
```
</div>
سپس می توان با کوئری های مختلف داده ها را بازیابی، حذف، آپدیت نمود.

<div dir="ltr">

```py
from appname.models import *

Library.objects.all()
# returns empty QuerySet
lib = Library(name="libo", address="shiboo")
lib.save()
Library.objects.all()
# returns QuerySet with Length 1
Library.objects.first().name
# returns libo
from django.utils import timezone
book = Book(name="booko", pages_number=121, pub_date=timezone.now(), library = lib)
book.save()
Book.objects.first().library.address
# returns shiboo
lib.delete()
Book.objects.all()
Library.objects.all()
# both return empty because of cascaded delete
```
</div>
<br/> <br/>

### ویو ها و url ها

هر ویو را می توان یک صفحه وب در نظر گرفت که یک کاربرد مشخص دارد مثلا صفحه ای که در آن لیست کتاب ها نمایش داده می شود.<br/>
ویو ها انواع مختلفی دارند و می توانند function-based یا class-based باشند.
برای ایجاد یک ویو قطعه کد زیر را در فایل views.py اپتان قرار دهید.

<div dir="ltr">

```py
from django.http import HttpResponse


def functionView(request):
    return HttpResponse("this is a function-based View.")
```
</div>
سپس در اپ یک فایل به نام urls.py ایجاد کنید و قطعه کد زیر را در آن قرار دهید.

<div dir="ltr">

```py
from django.urls import path

from . import views

urlpatterns = [
    path('here', views.functionView, name='func_view'),
]
```
</div>
با اینکار یک route برای تابع ساخته شده ایجاد می‌شود در نهایت نیز path ایجاد شده را در urls.py اصلی پروژه include کنید.
<div dir="ltr">

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('appname/', include('appname.urls'))
]
```
</div>
سپس با python manage.py runserver و رفتن به ادرس http://localhost:8000/appname/here می توانید خروجی ویو خود را مشاهد کنید.
<br/>
در ادامه classView ها نیز معرفی خواهند شد.
<br/>
<br/>

### ادمین جنگو
در اکثر وب اپلیکیشن ها صفحه ای برای مدیریت داده ها و بررسی مدل ها مورد نیاز است که این امر در جنگو به صورت اتوماتیک مهیا شده است و صفحه ای برای دسترسی ادمین ها برای تغییر، حذف، ایجاد مدل ها وجود دارد.برای کار با این صفحه نیاز به یک یوزر ادمین داریم برای ایجاد این یوزر از دستور زیر استفاده میکنیم.

<div dir="ltr">

```
python manage.py createsuperuser
```
</div>
این دستور یک یوزر با استفاده از مدل یوزر دیفالت جنگو ایجاد می کند. (توجه داشته باشید که به مدل ها و مایگریشن های انجام شده در بخش models نیاز هست)
<br/>
پس از ساخت یوزر python manage.py runserver  را زده و به ادرس http://localhost:8000/admin بروید و با یوزر پسورد تان لاگین کنید.
<br/>
همانطور که می بینید به مدل های library و book قابل رویت نیستند برای اضافه کردن آنها به صفحه ادمین در اپ حاوی آنها در فایل admin.py خطوط زیر را قرار دهید.


<div dir="ltr">

```py
from django.contrib import admin

from .models import Library, Book

admin.site.register(Library)
admin.site.register(Book)
```
</div>

سپس صفحه ادمین را رفرش کنید تا مدل ها اضافه شوند. حال می توانید از امکانات مختلف این صفحه بهره ببرید و Book و Library ایجاد کنید تغییر داده و یا حذف  کنید. برای ادیت کافیست روی مدل مورد نظر کلیک کنید و برای دلیت چند مدل می توان تیک کنار مدل ها زد و Action را روی delete قرار داد.


### تسک های Celery
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