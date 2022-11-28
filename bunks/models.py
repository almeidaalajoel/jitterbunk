from django.db import models
from django.utils import timezone

class User(models.Model):
    username = models.CharField(max_length=100)
    photo = models.CharField(max_length=500)

    def __str__(self):      
        return self.username

class Bunk(models.Model):
    from_user = models.ForeignKey(User, related_name="bunks_out", on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name="bunks_in", on_delete=models.CASCADE)
    time = models.TimeField(default=timezone.now)
    
    def __str__(self):
        return ("from " + str(self.from_user) + " to " + str(self.to_user))


