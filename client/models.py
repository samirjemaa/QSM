from django.contrib.auth.models import AbstractUser


# Create your models here.


# class Client(models.Model):
#     nom = models.CharField(max_length=30, null=True, blank=True)
#     prenom = models.CharField(max_length=30, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.nom + self.prenom + self.created_at


class User(AbstractUser):
    pass

    def __str__(self):
        return self.username
