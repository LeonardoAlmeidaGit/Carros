from django.db import models

# Create your models here.
# Criando a classe Brand para especificar as marcas do carro e ele puxar depois 
class Brand(models.Model):
      id = models.AutoField(primary_key=True)
      name = models.CharField(max_length=50)

      # Alterando o nome do objeto que aparece para o nome da marca ao inves de aparecer object (2)
      def __str__(self):
            return self.name

# Criando a classe Carro
class Car(models.Model):
      id = models.AutoField(primary_key=True)
      model = models.CharField(max_length=50)
      brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
      factory_year = models.IntegerField(blank=True, null=True)
      model_year = models.IntegerField(blank=True, null=True)
      plate = models.CharField(max_length=10, blank=True, null=True)
      value = models.FloatField(blank=True, null=True)
      photo = models.ImageField(upload_to= 'cars/', blank=True, null=True)
      bio = models.TextField(max_length=200, blank=True, null=True)
      
      # Alterando o nome do objeto que aparece para aparecer o modelo dele e não o objeto e o numero como antes estava.
      def __str__(self):
            return self.model
      
class CarInvetory(models.Model):
      cars_count = models.IntegerField()
      cars_value = models.FloatField()
      created_at = models.DateTimeField(auto_now_add=True)
      
      class Meta:
            ordering = ['-created_at']

      def __str__(self):
            return f'{self.cars_cout} - {self.cars_value}' 