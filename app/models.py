from django.db import models

CATEGORIES = [
    ('Politics','Political'),
    ('Education','Educational'),
    ('Story','Story books'),
    ('Motivation','Motivational'),
    ('Crime','Crime')
]
# Create your models here.

class  Book(models.Model):
    title = models.CharField(max_length=100)
    category= models.CharField(choices=CATEGORIES, max_length=100 ,null=True)
    year = models.IntegerField()
    cost = models.IntegerField()
    isbn = models.CharField(unique=True, max_length=13,null=True)
    cover = models.ImageField(upload_to='covers/',null=True)
    published = models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'books'


#   python manage.py makemigrations
#   python manage.py migrate




#   python manage.py createsuperuser
#     Joyce 12345

