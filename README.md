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

</div>