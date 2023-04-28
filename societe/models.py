from django.db import models

from qsm import settings


# Create your models here.


class Service(models.Model):
    nom = models.CharField(max_length=30, null=True)
    prioritaire = models.BooleanField(default=False)
    description = models.CharField(max_length=30, null=True)
    temp_moyenne_traitement = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom}"


class Poste(models.Model):
    nom = models.CharField(max_length=30, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    service = models.ManyToManyField(Service)

    def __str__(self):
        return f"{self.nom}"


class Societe(models.Model):
    nom = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=30, null=True)
    email = models.EmailField()
    tel = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    nb_poste = models.IntegerField(null=True)
    service = models.ManyToManyField(Service)

    def __str__(self):
        return f"{self.nom}"


class Ticket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="tickets_number", on_delete=models.CASCADE)
    numero_tiket = models.AutoField(primary_key=True)
    heure_queue = models.DateTimeField(auto_now_add=True)
    service_name = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    heure_debut_traitement = models.DateTimeField()
    heure_fin_traitement = models.DateTimeField()

    def __str(self):
        return f"{self.numero_tiket}"
