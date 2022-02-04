<div dir="rtl">

# DJANGO

جنگو یک وب فریمورک بر اساس پایتون است که توسعه پذیری بالا و موارد استفاده متنوعی دارد.
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

### مرحله دوم: ساخت venv

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

### مرحله سوم: نصب و اجرای جنگو

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

توجه: برای اجرای پروژه، نصب پکیج ها و کلا هر کاری مطمئن باشید که venv قرار دارید به طور مثال اگر venv را با دستور زیر غیر فعال کنیم.

<div dir="ltr">

```
deactivate
```

</div>
در این حالت با اجرای دستورات قبل باید ارور بخورید که جنگو نصب نیست.
</div>

# یادگیری جنگو با ساخت یک پروژه

Re

## ساخت پروژه

در این قسمت قراره یه پروژه با استفاده از فریمورک جنگو بالا بیاریم و با کانسپت های جنگو بیشتر آشنا بشیم.
در این آموزش از سیستم‌عامل ubuntu 20، پایتون 3.9 و django 4.0 استفاده شده پس پیشنهاد می‌کنیم شما هم از ورژن های گفته شده و سیستم عامل اوبونتو استفاده کنید تا کارتون راحت تر بشه :).

در مرحله اول پروژه رو با استفاده از کامندهایی که در قسمت راه‌اندازی پروژه گفته شده می‌سازیم.

```
mkdir django-tutorial
cd django-tutorial
virtualenv venv
source venv/bin/activate
python -m pip install django
django-admin startproject myfirstblog
cd myfirstblog
```

پس از اجرای کامند های بالا دایرکتوری ساخته شده را در ide دلخواه بالا میاریم و شروع به کد زدن می‌کنیم.

در پروژه ساخته شده یک فایل با نام settings.py وجود داره که در این فایل تنظیمات مربوط به اپ‌ها، middlewareها و کانکشن دیتابیس و... قرار داده میشه.

در این tutorial برای دیتابیس از postgresSQL استفاده میکنیم. البته میتونید تنظیمات مربوط به دیتابیس رو در حالت دیفالت نگه دارید و بخش بعد رو رد کنید.
(اگر با زبان SQL خیلی آشنایی ندارید پیشنهاد میکنیم قسمت رو رد کنید و بیشتر درگیر خود جنگو بشید تا یادگیری دیتابیس )

## تنظیمات مربوط به دیتابیس

برای نصب postgresSQL میتونید به این <a href="https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-20-04-quickstart">لینک </a> مراجعه کنید.

با استفاده از داک موجود در سایت کانفیگ مربوط به دیتابیس postgres رو در settings.py به قرار میدیم

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'myfirstblog',
        'USER': 'mohamadamin',
        'PASSWORD': '1234',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

کانفیگ بالا یک برای متصل به شدن به دیتابیس به نام myfirstblog با یوزر mohamadamin و رمز 1234 در لوکال‌هاست و پورت 5432 هست.

همچنین باید یک دیتابیس با نام myfirstblog بسازیم:

```
psql //conncect to database using postgresSQL client

CREATE DATABASE myfirstblog;
```

همچنین شما باید پکیج psycopg2 رو هم نصب کنید:

```
python -m pip install psycopg2-binary
```

برای اطلاعات بیشتر در مورد کانفیگ های دیتابیس میتونید به <a href="https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-DATABASES">داک جنگو </a>مراجعه کنید.

## migration

یکی از بهترین فیچر های موجود در جنگو وجود ORM در جنگو است که کار با دیتابیس و تغییر در آن و کوئری زدن رو خیلی راحت می‌کنه. یک کانسپت موجود در جنگو وجود مایگریشن هست.

مایگریشن چیه؟ وقتی شما میخواید دیتابیستون رو تغییر بدید (که در ادامه توضیح میدیم چجوری) باید یک سری تغییرات رو به صورت دستور SQL به دیتابیس بدید تا اون تغییرات اعمال بشه، اما توی جنگو وقتی میخواید این تغییرات رو انجام بدید لازم نیست دستور SQL خام اجرا کنید و خود جنگو متوجه تغییرات میشه و با یک سری کامند ساده این تغییرات رو میفرسته به دیتابیس تا اعمال بشه. (اگر متوجه نشدید نگران نباشید توی قسمت Model به طور مفصل توضیح میدیم.)

حالا که دیتابیس رو کانفیگ کردیم با دستور زیر migration اولیه رو انجام میدیم تا دیتابیسمون طبق آخرین تغییرات آپدیت بشه.

```
python -m manage.py migrate
```

اگر کانفیگ های دیتابیس درست باشد بدون مشکل دستور بالا اجرا میشه.

## ساخت اپ

شما میتونید کل پروژه رو داخل فولدر myfirstblog بسازید و مشکلی نداره ام برای رعایت best practice ها بهتر است که پروژه‌تون رو به چند اپ تقسیم کنید که هر اپ کدهای مربوط به فیچر خاصی در پروژه رو داره که باعث میشه دولوپ و دیباگ کردن در آینده راحت تر بشه

توی این tutorial قراره سایتی داشته باشیم که هر یوزر بتونه چندتا پست تولید کنه و تغییر بده و حذف کنه و...(در اصطلاح بهش میگن CRUD که مخفف برای Create, Read , Update, Delete هست)
پس برای زیبایی کار یک اپ به نام posts تولید میکنیم:

```
python manage.py startapp posts
```

بعد از ساخته شدن این اپ باید در settings.py این اپ رو به پروژه اپ های مورد استفاده در پروژه اضافه کنیم

```py
INSTALLED_APPS = [
    # other apps( Do not change that)
    ...
    # add your app
    "posts",
]
```

در فولدر posts تعدادی فایل وجود دارد که به تعریف درباره فایل هایی که باهاشون کار داریم کمی توضیح میدیم.

### models

در این فایل Model هایی که میسازیم رو قرار میدیم.

Model چیست؟

مدل درواقع همون table ساخته توی دیتابیسمونه و به ازای ساخت هر instnce از این مدل یک سطر به جدول موجود در دیتابیس اضافه میشه.

با استفاده از ORM موجود در جنگو میتونیم بر روی یک یا چندین مدل کوئری بزنیم و یا با تغییر اون مدل و ایجاد یک مایگریشن این تغییرات رو در دیتابیس اعمال کنیم. به عنوان مثال در این قسمت قراره که یک مدل به نام Post ایچاد کنیم و با ایجاد مایگریشن که توسط خود جنگو تولید میشه دیتابیسمون رو آپدیت کنیم.

### views

در این فایل view های ساخته شده‌مون رو قرار میدیم.ویو به زبان ساده یک تابع است که به ازای یک request خاص اون تابع ساده زده میشه(امکان داره کلاس باشه و تابع نباشه ولی در کل میتونیم ویو رو یه قطعه کد در نظر بگیریم که در یک سری مواقع خاص صدا زده میشه.) به عنوان مثال میگیم اگه توی مرورگر آدرس /posts/1 صدا زده شد بره ویوی get_post_with_id کال بشه.

### admin

یکی از بهترین فیچر های موجود در جنگو داشتن ادمین آماده است به طوری که خیلی راحت میتونیم با طرف چند تا کلاس و دادن چند تا کانفیگ یک صفحه ادمین قوی داشته باشیم. فعلا توضیح زیادی نمیدیم و به صورت عملی این بخش رو میبینیم.

### urls (به صورت پیشفرض ساخته نمیشه و خودمون میسازیمش)

در این فایل نیز مپ کردن آدرس به view رو انجام میدیم مثلا همونظور که در بالا گفتیم اگر /posts/1 صدا زده ش، ویوی get_post_with_id صدا زده بشه در این قسمت این مپ کردن انجام میشه.

### فولدر templates(این فولدر هم به صورت پیش فرض وجود نداره)

هر ویو میتونه یک فایل html رو نمایش بده که در واقع همون template های موجود در این فولدر هستش. جنگو میتونه به عنوان یک فریم ورک full stack در نظر گرفته بشه چرا که میشه با استفاده از همین template موجود و رندر کردن اون یک پروژه رو بدون نیاز به فرانت خاصی بالا آورد.

در ادامه آموزش بیشتر با template آشنا میشیم.

## بالا آوردن ادمین

برای اینکه ui خوبی داشته باشیم بهتره اول ادمین جنگو رو بالا بیاریم و بعد شروع به کد زدن بکنیم

در ابتدا یک supreuser با استفاده از کامند زیر میسازیم

```
python manage.py createsuperuser
```

پس از وارد کردن اطلاعات و ساخت superuser پروژه رو ران میکنیم

```
python manage.py runserver
```

و با رفتن به آدرس داده شده (به صورت پیشفرض http://127.0.0.1:8000/admin) وارد کردن اطلاعات داده شده وارد پنل ادمین میشیم و از این به بعد می‌توانیم از این پنل استفاده کنیم.

همانطور که میبینید یک Model به نام users به صورت پیشفرض داخل ادمین وجود دارد. ما نیز از همین یوزر قرار است استفاده کنیم.

## دست به کد بشیم :)

حالا وقتشه که شروع کنیم به کد زدن. همونطور که گفتیم در پروژه ما قراره هر یوزر چند تا post تولید کنه و تغییر بده و... . پس به یک مدل به نام Post نیاز داریم که از طرفی این مدل با User پیش فرض موجود در جنگو در ارتباطه. (میتونید برای اطلاعات بیشتر در مورد روابط در پایگه داده های SQL سرچ کنید .) در اپ posts و در فایل models.py مدل خودمون رو میسازیم

```py
# posts/models.py
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    body = models.TextField()

    def __str__(self) -> str:
        return self.title + " | " + str(self.author)

```

مدل ساخته شده ما دارای title که CharField با حداکثر مقدار 255 است، یک نویسنده که همان User ما است و یک body دارد که از نوع TextField است.
شاید براتون سوال بشه ForeignKey چیه؟

در پایگاه داده رابطه‌ای مدل ها میتونن با هم رابطه یک به یک، یک به چند یا چند به چند داشته باشند. ForeignKey در واقع همان رابطه ۱ به چند نمایش میده. یعنی در مثال بالا به هر Post حتما یک User دارد و به طبع هر User میتواند چند Post داشته باشه. on_delete= CASCADE یک روش برای اعمال تغییرات بر روی روابط است. با مثال توضیح میدیم.

فرض کنید یک post با آیدی ۱ داریم که نویسنده آن کامبیز است. حالا اگه کامبیز به هر دلیلی از دیتابیس حذف بشه دیگه کامبیزی وجود نداره که بگیم این پست برای کامبیزه، یکی از روش های حل این مشکل cascade کردن حذف است به این معنی که حالا که کامبیز رو از دست دادیم تمام Post هایی که کامبیز نوشته هم از دیتابیس حذف بشن تا بدون صاحب نمونن.

دیگه بیشتر از این وارد SQL نمیشیم و اگه دوست داشتید میتونید خودتون تا بیشتر آشنا بشید.

برای Post هم یک تابع به اسم `__str__` داریم که در پایتون با نام magic method شناخته میشن. از این تابع برای نمایش یک آبجکت استفاده میشن که اگه این تابع رو پیاده سازی نکنیم مشکل خاصی ایجاد نمیشه و چیزی که داخل ادمین میبینیم یک آبجکت با آیدی مشخص است.

به صورت پیشفرض جنگو یک فیلد به نام id برای هر Model ایجاد میکنه که primary key برای اون مدل هست و با استفاده از اون آیدی (id یا pk) میتونیم به یک آبجکت از مدل دسترسی پیدا کنیم.

### مایگریشن زدن

گفتیم هر مدل توی دیتابیس به یک تیبل تبدیل میشه. حالا که ما یک مدل جدید ساختیم وقتشه به دیتابیس این تغییرات رو اعمال کنیم. برای اینکار جنگو یک کامند به نام makemigrations داره که میاد تغییرات اعمال شده رو دریک فایل مینویسه و با استفاده از اون و دستور migrate این تغییرات رو به دیتابیس اعمال میکنه.

توجه: به هیچ وجه فایل ساخته شده مایگریشن رو الکی پاک نکنید یا دستی تغییر ندید چون امکان داره برای ریورت کردن یا تغییرات بعدی دچار مشکل بشید.

```
python manage.py makemigrations
python manage.py migrate
```

بعد از اجرای کامند های بالا در دیتابیس یک تیبل مربوط به Post خواهیم داشت

### اضافه کردن به ادمین

از اونجایی که فعلا صفحه ای برای ساخت پست نداریم از ادمین جنگو برای این کار استفاده میکنیم تا ببینیم بدون مشمکل برنامه اجرا میشه یا نه.

در فایل admin.py موجود در posts مدل خودمون رو به ادمین register میکنیم.

```py
# posts/admin.py
from django.contrib import admin
from posts.models import Post

admin.site.register(Post)

```

حالا پروژه رو ران میکنیم و وارد ادمین میشیم باید یک قسمت جدید به نام Posts ایجاد شده باشد

میتواند با گزینه add post یک پست جدید با author ای که از قبل ساختیم (همان superuser )یک پست جدید بسازیم و ببینیم برنامه به درستی کار میکند.

### ساختن ویو ها و تمپلیت ها

برای برقراری ارتباط کاربر ها با سرور نیاز به یک ui داریم که کاربر بتونه درخواستش رو به سرور بزنه و یک جواب بگیره.

در این قسمت قراره با استفاده از کلاس های آماده و ویژگی های جنگو این قسمت رو بسازیم.

در حالت کلی سه step برای این کار وجود داره.

۱. ساختن view مورد نظر که معمولا در views.py انجام میشه

۲. مپ کردن url به ویو مورد نظر که در urls.py انجام میشه

۳. ساختن و مپ کردن تمپلیت به ویوی مورد نظر

اگر این سه مرحله رو به درستی انجام بدیم به راحتی میتونیم ui مورد نظر رو بسازیم.

برای این پروژه به یک homepage نیاز داریم کخ تمام پست ها را به ما نمایش بده.

اول نیازه که به پروژه url های مربوط به posts رو بفهمونیم. برای اینکار در فایل urls.py موجود در اپ اصلی که همان myfirstblog هست این تغییرات رو اضافه میکنیم

```py
# myfirstblog/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("posts/", include("posts.urls")),
]

```

کدی که اضافه شد به این معنی است که در url هایی که وارد میشه اگر path وارد شده دارای posts/ بود، و دارای sub-path های موجود در posts.urls بود از ویو های مربوط به اون url استفاده کنه.

حالا نیازه که ویو خودمون رو تعریف کنیم.
ویوی خودمون رو میتونیم با استفاده از تابع و بدون generic view بسازیم اما خود جنگو دارای genericView هایی هست که باعث میشه ساخت این ویو ها آسون تر بشه.

برای آشنایی تنها ویوی homeView رو با هر دو حالت مینویسیم اما بقیه ویو هارو فقط از genericView ها استفاده میکنیم.

برای آشنایی بیشتر با ویوهای ساده میتونید از <a href= "https://docs.djangoproject.com/en/4.0/intro/tutorial03/">این لینک </a> استفاده کنید.

در فایل posts/views.py کد زیر را وارد میکنیم:

```py
# posts/views.py
from django.shortcuts import render
from django.views.generic import ListView
from posts.models import Post


def homeView(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "posts/home.html", context)


class HomeView(ListView):
    model = Post
    template_name = "posts/home.html"
    context_object_name = "posts"

```

دو ویو ساخته شده بالا در واقع یک کار انجام میدهند اما یکی با استفاده از genericView نوشته شده و دیگری به صورت دستی .

این ویو تمام Post های موجود در دیتابیس را گرفته و به تمپلیتی که در ادامه صحبت میکنیم پاس میدهد(این پاس دادن با استفاده از context هست که در ویوی اول خودمان به صورت دستی به تمپلیت دادیم اما در ویو دوم کلاس ListView این رو هندل میکنه و صرفا ما مدل و اسمی که به عنوان context پاس میده رو معرفی کردیم)

حالا باید ویو رو به url و تمپلیت متصل کنیم. در posts/urls.py داریم:

```py
# posts/urls.py
from django.urls import path
from posts import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),  # for genericView
    path("", views.homeView, name="home"),  # for regular view
]

```

در این قسمت میگوییم اگر path موجود به صورت
`domain/posts‍` بود ویوی home رندر شود

برای template ها یک فولدر داخل posts با نام templates میسازیم و داخل آن دوباره یک فولدر دیگر با نام posts میسازیم و درون آن فولدر html فایل های دلخواه رو قرار میدیم دلیل ساخت فولدر posts داخل فولدر templates این است که امکان دارد اپ دیگری بسازیم که home.html داشته باشد که در این صورت امکان اشتباه وجود دارد و با این کار از این اشتباه جلوگیری میشود.

حالا تمپلیت زیر را میسازیم:

```html
<!-- posts/templates/posts/home.html -->
<h1>Post</h1>
<ul>
  {% for post in posts %}
  <li>
    {{ post.title }} - {{ post.author.first_name }} {{ post.author.last_name }}
    <br />
    {{ post.body }}
  </li>
  {% endfor %}
</ul>
```

در تمپلیت داده شده از سینتکس پایتون استفاده کردیم که یکی از نقاط قوت تمپلیت جنگو است. برای استفاده از این سینتکس از {% %} استفاده میکنیم و برای استفاده ازdata ها آن هارا داخل {{ }} قرار میدهیم. کد بالا بر روی posts موجود در context پاس داده شده توسط view فور میزند و به ازای هر پست تایتل آن و نام و نام خانوادگی نویسنده و بدنه پست را چاپ میکند.

## DetailView

حال نیاز به ویو‌ای داریم که به ازای هر post اطلاعات آن را به ما بدهد.

برای این کار ویو زیر را با استفاده از DetailView میسازیم:

```py
# posts/views.py
from django.views.generic import DetailView

class PostDetailView(DetailView):
    model = Post
    template_name = "posts/detail.html"
    context_object_name = "post"
```

از آنجا که ما به اطلاعات یک Post نیاز داریم باید با استفاده از primary key موجود در url به جنگو بگوییم که کدام Post را به ما بدهد. برای اینکار در urls.py خواهیم داشت:

```py
from django.urls import path
from posts import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),  # for genericView
    # path("", views.homeView, name="home"),  # for regular view
    path("<int:pk>", views.PostDetailView.as_view(), name="post-detail"), # add this line
]

```

منظور از path بالا این است که اگر url موجود به صورت
`domain/posts/123`
بود قسمت 123 را به عنوان pk به PostDetailView پاس دهد و بر اساس آن یک مقدار از دیتابیس به ما برگرداند.
(دقت کنید که path موجود حتما باید دارای posts/ باشه زیرا اگر خاطرتون باشه در myfirstblog/urls.py و در قسمت پاس دادن posts.urls مقدار posts/ را به عنوان pre-path به آن دادیم)

حال تمپلیت را میسازیم

```html
<h1>{{ post.title }}</h1>
<small>By: {{ post.author.first_name }} {{ post.author.last_name }}</small
><br />
<hr />
{{ post.body }}

<br />
<br />
<a href="{% url 'home' %}">back</a>
```

در این قسمت از {% url %} موجود در جنگو استفاده کردیم که بهمون اجازه میده به صورت راحت تر بین url ها جا به جحا بشیم.
در مثال بالا به ازای کلیک بر روی back به url ای که نام آن home است برمیگردیم که در واقع همان `domain/posts` هست

یک تغییر هم در home.html میدهیم تا به ازای هر پست لینکی به detailView آن داشته باشیم:

```html
<h1>Post</h1>
<ul>
  {% for post in posts %}
  <li>
    <a href="{% url 'post-detail' post.pk %}">{{ post.title }}</a>
    - {{ post.author.first_name }} {{ post.author.last_name }}
    <br />
    {{ post.body }}
  </li>
  {% endfor %}
</ul>
```

در اینجا نیز به ازای کلیک بر روی title پست به detailView آن میرویم. دقت کنید که post.pk را به عنوان ورودی به url با نام post-detail میدهیم.
(یکبار از template به urls و سپس به views بروید تا به طور کامل متوجه پاس دادن این pk بشید :) )

### زیبا کردن تمپلیت و استفاده از ارثبری

جنگو این امکان رو فراهم که بتونیم با استفاده از ارث بری تمپلیت هایس خودمون رو بهتر و راحتتر بسازیم.

دراین قسمت کمی تمپلیت رو زیباتر میکنیم.

فایل base.html رو در کنار بقیه html ها میسازیم (میتونید محتویات فایل رو از ریپو پروژه کپی کنید).

نکات مهم:

```html
<title>{% block title %}My First Blog!!!{% endblock %}</title>

<div class="container">{% block content %} {% endblock %}</div>
```

در این قسمت از بلاک بندی استفاده کردیم که با نام دادن به یک بلاک میتونیم در یک فایل دیگر این بلاک رو اورراید کنیم و مثل این میشه که اون تیکه از html فایل داخل این بلاک کپی میشه.

در این جا هم دو بلاک داریم که در detail و home اون را اورراید میکنیم.

```html
<!--posts/detail.html -->
{% extends 'posts/base.html'%} {% block title %} {{ post.title_tag }} {%
endblock %} {% block content %}
<h1>{{ post.title }}</h1>
<small>By: {{ post.author.first_name }} {{ post.author.last_name }}</small
><br />
<hr />
{{ post.body }}

<br />
<br />
<a href="{% url 'home' %}" class="btn btn-secondary">back</a>
{% endblock %}
```

در بالای فایل detail.html از extends base.html استفاده کردیم که باعث میشه کد هایی که داخل base وجود دارد در این تمپلیت نیز نمایش داده بشه.

پس navbar موجود در base در اینجا نیز نمایش داده میشه.

همچنین برای Post یک فیلد به نام title_tag ساختیم که در ادامه بیشتر توضیح میدیم.

```html
<!-- posts/home.html -->
{% extends 'posts/base.html'%} {% block content %}
<h1>Post</h1>
<ul>
  {% for post in posts %}
  <li>
    <a href="{% url 'post-detail' post.pk %}">{{ post.title }}</a> -
    {{post.author.first_name }} {{ post.author.last_name }}
    <br />
    {{ post.body }}
  </li>
  {% endfor %}
</ul>
{% endblock %}
```

همانطور که گفتیم تغییراتی در Post ایجاد کردیم:

```py
# posts/models.py
from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, null=True, blank=True) #added
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    body = models.TextField()

    def __str__(self) -> str:
        return self.title + " | " + str(self.author)

    def save(self, *args, **kwargs): #added
        if not self.title_tag or self.title_tag == "":
            self.title_tag = self.title
        return super(Post, self).save(*args, **kwargs)
```

تابع save هنگام ذخیره شدن در دیتابیس صدا زده میشود و اگر title_tage خالی بود آن را با استفاده از title پر میکند و سیو میکند.

همچنین برای title_tag مقدار blank=True و null=True در نظر گرفتیم تا برای آن پست هایی که قبل از مایگریشن این فیلد را نداشتند مشکلی پیش نیاید

باید مایگریشن بسازیم

```
python manage.py makemigrations
python manage.py migrate
```

پس از اعمال کامند های بالا دیتابیس آپدیت میشود.

### ساخت صفحه برای ایجاد Post

همونطور که قبلا گفتیم برای ایجاد یک ویو جدید باید view, url, template ساخته بشه.

برای ساخت Post میتونی از CreateView استفاده کنیم:

```py
# posts/views.py
from django.views.generic import CreateView
class AddPostView(CreateView):
    model = Post
    template_name = "posts/add_post.html"
    fields = "__all__"
```

fields موجود در کلاس بالا مشخص میکند که کدام فیلد های مربوط به Post در Form داده میشوند. در صورتی که نخواهیم همه‌ی فیلدهارو در فرم داشته باشیم میتونیم به راحتی به عنوان یک tuple اسم فیلد هارو بنویسیم به عنوان مثال اگر فقط title , body رو میخواستیم داشتیم:

```py
# posts/views.py
from django.views.generic import CreateView
class AddPostView(CreateView):
    model = Post
    template_name = "posts/add_post.html"
    fields = ("title", "body")

```

برای url داریم:

```py
from django.urls import path
from posts import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),  # for genericView
    # path("", views.homeView, name="home"),  # for regular view
    path("<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("add-post/", views.AddPostView.as_view(), name="add-post"),
]
```

و در نهایت برای template داریم:

```html
<!-- templates/posts/add_post.html -->
{% extends 'posts/base.html'%} {% block title %} Create A New Blog Post {%
endblock %} {% block content %}
<h1>Add Post...</h1>
<br />
<form method="POST">
  {% csrf_token %} {{ form.as_p }}
  <button class="btn btn-secondary">post</button>
</form>
{% endblock %}
```

در فرم بالا از csrf_token استفاده کردیم که باعث جلوگیری از حملات به سرور میشود.
همچنین CreateView یک context به نام form به تمپلیت میدهد که با استفاده از form.as_p میتوان آن را به صورت پاراگراف گرفت. روش های دیگری مانند as_table, as_ul هم وجود دارند که میتونید مطالعه کنید راجع بهشون.

اگر این کار ها رو انجام بدید و پروژه رو ران کنید و یک پست بسازیر با خطا مواجه میشید زیرا بعد از ساخت پست جنگو میخواهد به یک url ریدایرکت بشه در حالی که ما چیزی برای اون ست نکردیم

این کار روی میتونیم در مدل ست کنیم:

```py
# posts/models.py

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    body = models.TextField()

    def __str__(self) -> str:
        return self.title + " | " + str(self.author)

    def save(self, *args, **kwargs):
        if not self.title_tag or self.title_tag == "":
            self.title_tag = self.title
        return super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})

```

تابع get_absolute_url بعد از ساخت پست آن را به صفحه post-detail هدایت میکنه.

میتوان به جای صفحه detail به home برگردیم که به صورت زیر میشد:

```py
    def get_absolute_url(self):
        return reverse("home")
```

در ضمن در base.html تغییر زیر را انجام دادیم:

```html
<a class="nav-link" href="{% url 'add-post' %}">Add Post</a>
```

که در نوبار در صورت کلیک به add-post هدایت میشیم.

### استفاده از form برای ساخت Post

میتوان با استفاده از django.forms به فرم مورد نظرمون استایل بدیم و ui زیبا تری داشته باشیم.

در ابتدا یک فایل با نام forms.py در اپ posts ایجاد میکنیم و کد زیر را داخل اون قرار میدیم:

```py
# posts/forms.py

from django import forms
from posts.models import Post
class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "title_tag", "author", "body")

        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "your Title"}
            ),
            "title_tag": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.Select(attrs={"class": "form-control"}),
            "body": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "your Body"}
            ),
        }

```

با استفاده از widegets و fields مقادیر موجود در فرم و استایل آن هارا ست میکنیم.

در AddPostView نیز تغییرات زیر رو انجام میدیم:

```py
# posts/views.py
from posts.forms import CreatePostForm

class AddPostView(CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = "posts/add_post.html"

```

دقت کنید که fields از AddPostView حذف شد زیرا در CreatePostForm و در کلاس meta اش ست شده.

در نهایت نیز add_post.html به صورت زیر تغییر میکند:

```html
{% extends 'posts/base.html'%} {% block title %} Create A New Blog Post
{%endblock %} {% block content %}
<h1>Add Post...</h1>
<br />

<div class="form-group">
  <form method="POST">
    {% csrf_token %} {{ form.as_p }}
    <button class="btn btn-secondary">post</button>
  </form>
</div>
{% endblock %}
```

### آپدیت کردن پست

همونطور که حدس میزنید باید چه کاری انجام بدیم شروع میکنی به ساخت ویو:«

```py
# posts/views.py
from django.views.generic import UpdateView

class UpdatePostView(UpdateView):
    model = Post
    template_name ="posts/update_post.html"
    form_class = UpdatePostForm
```

```py
# posts/forms.py

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "title_tag", "body")

        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "your Title"}
            ),
            "title_tag": forms.TextInput(attrs={"class": "form-control"}),
            "body": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "your Body"}
            ),
        }

```

```py
# posts/urls.py
from django.urls import path
from posts import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),  # for genericView
    # path("", views.homeView, name="home"),  # for regular view
    path("<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("add-post/", views.AddPostView.as_view(), name="add-post"),
    path("edit/<int:pk>/", views.UpdatePostView.as_view(), name="update-post")
]

```

```html
<!-- posts/templates/posts/update_post.html -->
{% extends 'posts/base.html'%} {% block title %} Edit Blog Post {%endblock %} {%
block content %}
<h1>Update Post...</h1>
<br />

<div class="form-group">
  <form method="POST">
    {% csrf_token %} {{ form.as_p }}
    <button class="btn btn-secondary">Update</button>
  </form>
</div>
{% endblock %}
```

همچنینی تغییراتی در detail.html و home.html دادیم تا گزینه برای ادیت کردن داشته باشیم:

```html
<!-- posts/templates/posts/detail.html -->
{% extends 'posts/base.html'%} {% block title %} {{ post.title_tag }} {%endblock
%} {% block content %}
<h1>{{ post.title }}</h1>
<small
  >By: {{ post.author.first_name }} {{ post.author.last_name }} -
  <a href="{% url 'update-post' post.pk %}">(edit)</a></small
><br />
<hr />
{{ post.body }}

<br />
<br />
<a href="{% url 'home' %}" class="btn btn-secondary">back</a>
{% endblock %}
```

```html
<!-- posts/templates/posts/home.html -->
{% extends 'posts/base.html'%} {% block content %}
<h1>Post</h1>
<ul>
  {% for post in posts %}
  <li>
    <a href="{% url 'post-detail' post.pk %}">{{ post.title }}</a> -
    {{post.author.first_name }} {{ post.author.last_name }} -
    <small><a href="{% url 'update-post' post.pk %}">(edit)</a></small>
    <br />
    {{ post.body }}
  </li>
  {% endfor %}
</ul>
{% endblock %}
```

### حذف کردن Post

بدون اتلاف وقت به سراغ کد میریم:

```py
# posts/views.py
from django.views.generic import DeleteView

class DeletePostView(DeleteView):
    model = Post
    template_name = "posts/delete_post.html"
```

```py
# posts/urls.py
from django.urls import path
from posts import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),  # for genericView
    # path("", views.homeView, name="home"),  # for regular view
    path("<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("add-post/", views.AddPostView.as_view(), name="add-post"),
    path("edit/<int:pk>/", views.UpdatePostView.as_view(), name="update-post"),
    path("delete/<int:pk>/", views.DeletePostView.as_view(), name="delete-post")
]

```

```html
<!-- posts/templates/posts/delete_post.html -->
{% extends 'posts/base.html'%} {% block title %} Delete Blog Post {%endblock %}
{% block content %}
<h1>Delete Post...</h1>
<br />
<br />
<h3>Delete: {{ post.title}}</h3>
<div class="form-group">
  <form method="POST">
    {% csrf_token %}
    <strong>Are You Sure?</strong>
    <br /><br />
    <button class="btn btn-danger">Delete Post!</button>
  </form>
</div>
{% endblock %}
```

detail.htmlو home.html نیز تغییراتی داشتند:


```html
<!-- posts/templates/posts/detail.html -->
{% extends 'posts/base.html'%} {% block title %} {{ post.title_tag }}
{%endblock%} {% block content %}
<h1>{{ post.title }}</h1>
<small
  >By: {{ post.author.first_name }} {{ post.author.last_name }} -
  <a href="{% url 'update-post' post.pk %}">(edit)</a>
  <a href="{% url 'delete-post' post.pk %}">(delete)</a></small
><br />
<hr />
{{ post.body }}

<br />
<br />
<a href="{% url 'home' %}" class="btn btn-secondary">back</a>
{% endblock %}

```

```html
<!-- posts/templates/posts/home.html -->
{% extends 'posts/base.html'%} {% block content %}
<h1>Post</h1>
<ul>
  {% for post in posts %}
  <li>
    <a href="{% url 'post-detail' post.pk %}">{{ post.title }}</a> -
    {{post.author.first_name }} {{ post.author.last_name }} -
    <small><a href="{% url 'update-post' post.pk %}">(edit)</a></small>
    <small><a href="{% url 'delete-post' post.pk %}">(delete)</a></small>
    <br />
    {{ post.body }}
  </li>
  {% endfor %}
</ul>
{% endblock %}

```


به نظر همه چیز خوب میاید اما یک مشکل وجود دارد و آن این است بعد از حذف پست به کجا ریدایرکت شویم؟
برای تعیین آن به View داده شده فیلد success_url را پاس میدهیم:

```py
from django.urls import reverse_lazy

class DeletePostView(DeleteView):
    model = Post
    template_name = "posts/delete_post.html"
    success_url = reverse_lazy("home")
```

دلیل استفاده از reverse_lazy به دلیل مشکلات circular import هست.

