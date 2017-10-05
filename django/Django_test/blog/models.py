from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
""

# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (
        ('draf', 'Draf'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

class Meta:
    ordering = ('-publish',)

def __str__(self):
    return self.title

#"Это наша базовая модель для записей блога(blog posts). Давайте взглянем на поля, которые мы только что определили для этой модели:
#'title : это поле для заголовка поста(post title). Это поле является CharField, которое преобразуется в столбец VARCHAR в базе данных SQL.
#"slug: это поле, предназначенное для использования в URL-адресах. slug — это метка, содержащая только буквы, цифры, знаки подчеркивания или дефисы. Поле slug будет использоваться для создания прекрасных и удобных URL-адресов для записей блога(blog posts). Мы добавили параметр unique_for_date в это поле, чтобы можно было построить уникальные URL-адреса содержащие title поста и дату его публикации.
#"author: это поле ForeignKey. В этом поле определяется отношение «многие к одному». Мы сообщаем о том, что каждая запись написана пользователем, и пользователь можетсоздать сколько угодно постов(posts). Для этого поля Джанго создаст внешний ключ в базе данных, используя первичный ключ связанной модели. В этом случае мы полагаться на пользовательскую модель системы проверки подлинности Джанго. Мы указываем имя обратного отношения, от пользователя(user) к посту(post), с атрибутом related_name. Мы собираемся больше рассказать об этом позже.
#"body: это тело поста. Это поле является полем TextField, которое преобразуется в текстовый столбец базы данных SQL.
#"publish : этот параметр DateTime указывает, когда была опубликована запись. По умолчанию время определенио параметром timezone-aware datetime.now.
#"created : этот DateTime параметр указывает, когда был создан пост. Поскольку мы используем auto_now_add здесь, дата будет автоматически добавлена при создании объекта.
#"updated : этот DateTime параметр указывает на последний момент обновления этой записи. Поскольку мы используем auto_now здесь, дата будет автоматически обновляться при сохранении объекта.
#"status : это поле для отображения статуса записи(опубликован\неопубликован). Мы используем параметр выбора, поэтому значение этого поля может быть задано только для одного из этих вариантов.
#"Как вы видите, Джанго имеет различные типы полей, которые можно использовать для определения моделей.
#Все типы полей можно найти в https://docs.djangoproject.com/en/1.8/ref/models/fields/ ."
