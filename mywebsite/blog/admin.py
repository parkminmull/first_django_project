from django.contrib import admin
# from .models import Post

# admin.site.register(Post)

from blog.models import Post
from .models import AwardImageUpload


admin.site.register(Post)
admin.site.register(AwardImageUpload)
