from django.contrib import admin
from .models import Comentario
from .actions import reprova_comentarios, aprova_comentarios

admin.site.register(Comentario)
