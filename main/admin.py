from django.contrib import admin

from . models import Project , Category , Post, Comment, Profile, Expertise, Education,Skills
# Register your models here.

admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Skills)
admin.site.register(Education)
admin.site.register(Expertise)