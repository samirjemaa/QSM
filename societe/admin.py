from django.contrib import admin
# Register your models here.
from django.contrib.auth.admin import UserAdmin

from client.models import User
from societe.models import Societe, Service, Ticket, Poste

admin.site.register(User, UserAdmin)
admin.site.register(Societe)
# admin.site.register(Service)


# admin.site.register(Ticket)
# admin.site.register(Poste)


class TicketAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'numero_tiket', 'heure_queue', 'service_name', 'heure_debut_traitement', 'heure_fin_traitement')


class PosteAdmin(admin.ModelAdmin):
    fields = ['nom', 'service']
    list_display = ('nom', 'get_service')

    def get_service(self, obj):
        return " , ".join([s.nom for s in obj.service.all()])


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'prioritaire')


admin.site.register(Service, ServiceAdmin)
admin.site.register(Poste, PosteAdmin)
admin.site.register(Ticket, TicketAdmin)
