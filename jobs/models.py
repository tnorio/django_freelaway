from django.db import models
from django.contrib.auth.models import User

# Create your models here.
'''
class Teste_tabela(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
'''
'''
para realmente fazer uma tabela no BD devemos realizar a migração
cmd: python manage.py makemigrations
O comando a cima insere a tabela na pasta migrations
para REALMENTE inseri-la no DB, devmos após:
cmd: python manage.py migrate
'''
class Referencias(models.Model):
    arquivo = models.FileField(upload_to='referencias')

    def __str__(self) -> str:
        return self.arquivo.url

class Jobs(models.Model):
    categoria_choices = (('D', 'Design'),
                         ('EV', 'Edição de Vídeo'))

    status_choices = (('C', 'Em criação'),
                      ('AA', 'Aguardando aprovação'),
                      ('F', 'Finalizado'))

    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    categoria = models.CharField(max_length=2, choices=categoria_choices, default="D")
    prazo_entrega = models.DateTimeField()
    preco = models.FloatField()
    referencias = models.ManyToManyField(Referencias)
    profissional = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    reservado = models.BooleanField(default=False)
    status = models.CharField(max_length=2, choices=status_choices, default='C')
    arquivo_final = models.FileField(null=True)

    def __str__(self) -> str:
        return self.titulo
