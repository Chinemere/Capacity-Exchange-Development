from django.db import models

# Create your models here.


class bug(models.Model):
    description = models.CharField(max_length=2000)
    bug_type = models.CharField(max_length=200)
    report_date = models.DateTimeField("The date bug is being registered")
    status = models.CharField(max_length=200)

    def __str__(self) :
        return f"Bug: {self.description}"
