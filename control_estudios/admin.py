from django.contrib import admin

from control_estudios.models import Artistas, Canciones, Albums


admin.site.register(Canciones)
admin.site.register(Albums)
admin.site.register(Artistas)
