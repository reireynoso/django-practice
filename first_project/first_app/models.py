from django.db import models

# Create your models here.
class Topic(models.Model):
    # attribute and classify what kind of field it's going to be. max_length is a constriain of this chacrater field
    top_name = models.CharField(max_length=264, unique=True)

    # Write some string representation of the model
    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    # foreign key
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        # since it's going to be a date object
        return str(self.date)