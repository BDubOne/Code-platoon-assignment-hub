from django.contrib import admin
from .models import Pokemon
from move_app.models import Move
from trainer_app.models import Trainer


admin.site.register(Pokemon)
admin.site.register(Move)
admin.site.register(Trainer)


