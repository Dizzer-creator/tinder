from django.contrib import admin
from .models import Startapp
from .models import User
from .models import Ptinder
from .models import Choicelist


admin.site.register(Ptinder)


class Choicelistinline(admin.TabularInline):
    model = Choicelist
    extra = 1


@admin.register(User)
class Useradmin(admin.ModelAdmin):
    inlines = (Choicelistinline,)


@admin.register(Startapp)
class Startappadmin(admin.ModelAdmin):
    inlines = (Choicelistinline,)
