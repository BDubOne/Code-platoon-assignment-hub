from django.contrib import admin
from .models import Pokemon
from move_app.models import Move


admin.site.register(Pokemon)
admin.site.register(Move)


