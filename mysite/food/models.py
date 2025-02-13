from django.db import models

# Create your models here.
class Item(models.Model):
    def __str__(self):
        return self.item_name
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,default="https://imgs.search.brave.com/Tjhi7PMxaRtFlKw9I3Nr5x2Dm8jyw0y3z5aVH3Zjpog/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvNDcx/NDU2MDYxL3Bob3Rv/L2hhbWJ1cmdlci5q/cGc_cz02MTJ4NjEy/Jnc9MCZrPTIwJmM9/SjJEV2R4TU51M1A5/NkJEQ2J1TWRJM0R1/TG8zMjRzNEJBaVZD/dXExUDQzZz0")
    
    