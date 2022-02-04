<div dir="rtl">

# Django Rest Framework(DRF)
جنگو رست فریمورک یک ابزار قدرتمند و انعطاف‌پذیر برای نوشتن Web API است.

## معماری REST
این نوع معماری دارای شش محدودیت‌ است که اگر رعایت شوند نتایجی مانند کارایی بهتر، مقیاس‌پذیری، سادگی،
اصلاح‌پذیری و ... را به همراه خواهد داشت.

### معماری کلاینت سرور
این اصل برای جدا کردن نگرانی‌های مرتبط با رابط کاربری از نگرانی‌های مربوط به ذخیره‌سازی داده است.
در حقیقت طراحی ما به دو بخش کاملا مجزای فرانت‌اند و بک‌اند تقسیم می‌شود که ارتباط آن‌ها از طریق APIها فراهم می‌شود.

### بدون حالت‌ بودن (Statelessness)
بدین معنی که هر کدام از درخواست(request)هایی که به سرور داده می‌شود
مستقل از یکدیگر قابل‌فهم هستند؛ به طور مثال برای پاسخ دادن به یک درخواست نیازی به دانستن درخواست‌های قبلی نیست.
این ویژگی باعث می‌شود که در برنامه‌های با تعداد درخواست بالا، عملکرد بهتری وجود داشته باشد.

### قابلیت ذخیره (cache)
وجود قابلیت ذخیره‌سازی داده‌ها که باعث مقیاس‌پذیری و عملکرد بهتر می‌شود.

### سیستم لایه‌ای
ارتباط کلاینت و سرور ممکن است از لایه‌های محتلفی تشکیل شده باشد. به طور مثال وجود یک load balancer می‌تواند به بهبود عملکرد سرور منجر شود.
 همچنین می‌توان امنیت را به عنوان یک لایه روی سرویس وب اضافه کرد و سپس منطق کد را پیاده‌سازی کرد؛ که این موضوع به سادگی و اصلاح‌پذیر بودن کد کمک می‌کند.

### رابط یکسان (Uniform interface)

### Code on demand (optional)


## متودهای رایج درخواست HTTP

### GET
این متود داده‌ی مورد نظر خود را از سرور دریافت می‌کنیم.

### POST
این متود برای فرستادن دیتا به سرور استفاده می‌شود و معمولا پس از آن یک آبجکت ساخته می‌شود.

### PUT
این متود برای به‌روزرسانی یک آبجکت به کار می‌رود.

### DELETE
این متود برای حذف یک آبجکت استفاده می‌شود.

## راه‌اندازی اولیه
مطابق توضیحات داده شده در بخش جنگو یک پروژه میسازیم. سپس djangorestframework را نصب می‌کنیم.

<div dir="ltr">

```
$ pip install djangorestframework
```
</div>

و rest_framework را به INSTALLED_APPS اضافه می‌کنیم

<div dir="ltr">

```py
INSTALLED_APPS = [

    ...
    
    'rest_framework',

    ...
]
```
</div>

میتوانیم کار خود را با drf شروع کنیم.

به طور کلی روند طراحی API به این صورت است که ما مدل‌های لازم برای پروژه خود را تعریف می‌کنیم. سپس APIهای لازم را بررسی و طراحی می‌کنیم. برای این‌کار باید ویو و سریالایزر را تعریف کنیم که در ادامه به بررسی آن‌ها می‌پردازیم.


### Serializer
سریالایزر یک شی را به دیکشنری در پایتون تبدیل می‌کند و  در نتیجه می‌توان از آن در پاسخ(response) APIها استفاده کرد(به فرمت‌های رایج JSON, XML, ...).

ساده‌ترین نوع سریالایزر یک SubClass از Serializer است که برای پیاده‌سازی کامل آن باید متودهای create, update آن را با توجه به مدل مربوطه پیاده‌سازی کنیم. اما روش راحت‌تر این است که از ModelSerializer استفاده کنیم که خود یک SubClass از Serializer است و دیگر نیاز به پیاده‌سازی دو متود گفته شده نداریم.

به طور مثال در زیر یک سریالایزر برای مدل Post آورده شده است:

<div dir="ltr">

```py
class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('author',)
```
</div>
این سریالایزر همه‌ی فیلدهای پست را شامل می‌شود و همچنین فیلد author را read only کرده است؛ بدین معنی که در هنگام ساخت و یا آپدیت مدل این فیلد توسط ورودی مقداردهی نخواهد شد.


### View
ویوها را می‌توان به دو دسته تقسیم کرد: 

1. APIView

2. GenericAPIView

تفاوت اصلی GenericAPIView با APIView این است که باید حتما به یک مدل وصل باشد و queryset و serializer_class برای آن مشخص شده باشد.

به طور کلی با اضافه کردن متودهای زیر به ویوها می‌توان متودهای HTTP گفته شده در بالا را برای آن API استفاده کرد.


<div dir="ltr">

```py
class SimpleView(APIView):

    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass

    def put(self, request, *args, **kwargs):
        pass

    def delete(self, request, *args, **kwargs):
        pass
```
</div>


همچنین mixinهای زیر را داریم که این متودها را پیاده‌سازی کرده‌اند و کافی است آن‌ها را اورراید کنیم تا منطقی موردنظر خود را پیاده‌سازی کنیم.

- CreateModelMixin
- ListModelMixin
- RetrieveModelMixin
- DestroyModelMixin
- UpdateModelMixin

به طور مثال فرض کنید بخواهیم ویویی برای گرفتن لیست پست‌ها و ساخت پست جدید بسازیم. برای این کار به صورت زیر عمل می‌کنیم:


<div dir="ltr">

```py
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated


class PostListCreateAPIView(ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
```
</div>
 حال کافی است در urls.py این ویو را اضافه کنیم.

<div dir="ltr">

 ```py
urlpatterns = [
    ...
    path('posts/', PostListCreateAPIView.as_view())
]
 ```
 </div>



</div>