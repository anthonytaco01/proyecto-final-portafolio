from django.db import models

# Create your models here.
# Modelo para formacion =couse
class Course(models.Model):
    title= models.CharField(max_length=150,verbose_name='Titulo')
    degree_title= models.CharField(max_length=300,verbose_name='Titulo obtenido')
    description=models.TextField(verbose_name='Descripcion')
    created=models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creacion')
    updated=models.DateTimeField(auto_now=True,verbose_name='Fecha de modificacion')
    
    #Pasos para convertir en español el admin
    class Meta:
        verbose_name = 'formacion'
        verbose_name_plural = 'formaciones'
        ordering = ['-created'] 
        
    #Para que muestre el titulo con link para acceder desde el admin
    def __str__(self):
        return self.title

# Modelos para skill

class Skill(models.Model):
    title= models.CharField(max_length=80,verbose_name='Titulo')
    image =models.ImageField(upload_to='skills', verbose_name='Imagen')
    created=models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creacion')
    updated=models.DateTimeField(auto_now=True,verbose_name='Fecha de modificacion')
    
    #Pasos para convertir en español el admin
    class Meta:
        verbose_name = 'conocimiento'
        verbose_name_plural = 'conocimientos'
        ordering = ['-created'] 
        
    #Para que muestre el titulo con link para acceder desde el admin
    def __str__(self):
        return self.title
