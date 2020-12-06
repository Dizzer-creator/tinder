from django.contrib import admin
from .models import StartUp, User, PageTinder, ChoiceList


class ChoiceListinline(admin.TabularInline):
    model = ChoiceList
    extra = 1


@admin.register(User)
class Useradmin(admin.ModelAdmin):
    inlines = (ChoiceListinline,)


@admin.register(StartUp)
class StartUpadmin(admin.ModelAdmin):
    inlines = (ChoiceListinline,)


@admin.register(PageTinder)
class PageTinderadmin(admin.ModelAdmin):
    pass
