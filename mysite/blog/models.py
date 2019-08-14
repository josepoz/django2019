# Create your models here.
from django.db import models
from django.utils import timezone


class Publicacion(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(
            default=timezone.now)
    fecha_publicacion = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo




# python manage.py makemigration   > crea codigo sqlite3
# ?oython manage.py createsuperuser


#  Para correr el servidor python manage.py runserve
# python manage.py makemigrations blog
# python manage.py migrate blog


# crear cuenta en git hub y pythonaniware
