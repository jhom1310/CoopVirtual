from django.db import models
from django.contrib.auth.models import User

class Oferta(models.Model):
        produto = models.CharField(max_length=100)
        description = models.TextField()
        phone = models.CharField(max_length=11, null=True)
        qtd_quartos = models.CharField(max_length=2, null=True)
        conservacao = models.CharField(max_length=3, null=True)
        endereco = models.CharField(max_length=255)
        end_date = models.DateTimeField(null=True, blank=True)
        begin_date = models.DateTimeField(auto_now_add=True)
        valor = models.DecimalField(max_digits=19, decimal_places=2)
        ativacao = models.BooleanField(default=True)
        usuario = models.ForeignKey(User, on_delete=models.CASCADE)
        photo = models.ImageField(upload_to='imoveis')

        def __str__(self):
                return str(self.produto)

