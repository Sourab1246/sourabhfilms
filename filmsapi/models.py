from django.db import models

from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class Actors(models.Model):
    name=models.CharField(max_length=100)
    
    def __str__(self):
            return self.name
        
class Movies(models.Model):
     
     
     id=models.IntegerField(primary_key=True)
     movies_name=models.CharField(max_length=20)
     visual_type_choices=[('2D','2D'),('3D','3D'),('IMAX','IMAX')]
     visual_type=models.CharField(choices=visual_type_choices,max_length=4)
     type_choices=[('action','action'),('romantic','romantic'),('sad','sad')]
     types=models.CharField(choices=type_choices,max_length=10)
     actors= models.ManyToManyField(Actors,through='MoviesActors')
     review=models.TextField(max_length=50)
     rating = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
     trailer_link=models.URLField()
      
     def __str__(self):
             return self.movies_name
class MoviesActors(models.Model):
     
     movies=models.ForeignKey(Movies, on_delete=models.CASCADE)
     
     actors= models.ForeignKey(Actors, on_delete=models.CASCADE)
     
     
     

        
     
        
    
       

# Create your models here.
