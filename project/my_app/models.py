from django.db import models

class Program(models.Model):
    name = models.CharField(max_length=50)
    maestro = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField(default=0)
    program = models.ForeignKey(
        'Program',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

