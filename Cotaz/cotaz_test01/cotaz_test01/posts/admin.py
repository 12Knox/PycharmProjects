from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    class Meta:
        model = Post

admin.site.register(Post)


echo 'PATH=$HOME/PycharmProjects/Cotaz/cotaz_test01/bin:$PATH'