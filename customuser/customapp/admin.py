from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import User
# from .models import Todo

# class TodoInline(admin.StackedInline):
#     model = Todo
#     verbose_name_plural = 'todo'

# class UserAdmin(BaseUserAdmin):
# 	inlines = [
# 		TodoInline,
# 	]


# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)

from .models import Todo
admin.site.register(Todo)


