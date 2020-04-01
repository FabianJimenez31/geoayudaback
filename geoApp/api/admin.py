from django.contrib import admin
from .models import (
    tipo_entidad,
    tipo_poblacion,
    tipo_iniciativa,
    fase_inicitiva,
    nivel_apoyo,
    poblacion,
    iniciativa,
    entidad,
    sector



    )


# Register your models here.

admin.site.register(tipo_entidad)
admin.site.register(tipo_poblacion)
admin.site.register(tipo_iniciativa)
admin.site.register(fase_inicitiva)
admin.site.register(sector)
admin.site.register(nivel_apoyo)
admin.site.register(poblacion)
admin.site.register(iniciativa)
admin.site.register(entidad)