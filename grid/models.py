from django.db import models
from django.urls import reverse


CHOICES = (
    (True, 'посетил(а)'),
    (False, 'Отсуствувал(а)')

)
class Position(models.Model):
    title = models.CharField(max_length=19999, blank=True, null=True)
    slug = models.SlugField(unique=True)



    def __str__(self):
        return  self.title


class Empoloe(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=True,null=True)
    phone = models.CharField(max_length=55)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='employuers/')
    stack = models.CharField(max_length=1000, blank=True, null=True)
    slug = models.SlugField(unique=True)


    def get_absolute_url(self):
        return reverse('visit', kwargs={'slug':self.slug})


    def __str__(self):
        return  self.name



class Visit(models.Model):
    data = models.DateField()
    employer = models.ForeignKey(Empoloe, on_delete=models.CASCADE)
    visited = models.BooleanField(choices=CHOICES)
    time_start = models.TimeField(blank=True, null=True, default='00:00')
    time_end = models.TimeField(blank=True, null=True, default='00:00')
    reason = models.CharField(max_length=100, default='-----',blank=True,null=True)



    def __str__(self):
        return f"Сотрудник{ self.employer.name}"

    class Meta:
        ordering = ['-date']

