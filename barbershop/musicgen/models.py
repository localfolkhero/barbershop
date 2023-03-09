from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils import timezone


class MusicScoreRecord(models.Model):
    
    slug = models.SlugField(auto_created=True, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=128, blank=False, null=False)
    
    abcnotation = models.TextField()
    musicxml = models.TextField()
    
    created = models.DateTimeField(editable=False)
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        return super(MusicScoreRecord, self).save(*args, **kwargs)    
    
class MusicScoreRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.ForeignKey(MusicScoreRecord, on_delete=models.CASCADE)
    rating = models.IntegerField(null=True, blank=True)