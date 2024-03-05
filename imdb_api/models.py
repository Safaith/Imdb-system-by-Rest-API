from django.db import models



class Platform(models.Model):
    name = models.CharField(max_length = 30)
    about = models.CharField(max_length = 60)
    link = models.URLField(max_length = 100)

    def __str__(self):
        return self.name


class WatchList(models.Model):
    title = models.CharField(max_length = 50)
    platform = models.ForeignKey(Platform, on_delete = models.CASCADE)
    genre = models.CharField(max_length = 30)
    created = models.DateTimeField(auto_now_add = True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
