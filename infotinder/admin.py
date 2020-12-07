from django.contrib import admin
from .models import StartUp, User, PageTinder, StartUpUser


class StartUpUserinline(admin.TabularInline):
    model = StartUpUser
    extra = 1


@admin.register(User)
class Useradmin(admin.ModelAdmin):
    inlines = (StartUpUserinline,)


@admin.register(StartUp)
class StartUpadmin(admin.ModelAdmin):
    inlines = (StartUpUserinline,)


@admin.register(PageTinder)
class PageTinderadmin(admin.ModelAdmin):
    pass
