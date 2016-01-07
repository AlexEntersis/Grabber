from django.db import models

#Create your models here.

class Comments(models.Model):
    comment_author = models.CharField(max_length=300, null=False)
    comment_date = models.DateField(default=None, null=False)
    comment_text = models.TextField(default=None)

    # STATUSES_CHOICES = (("QA", "Quality Assurance"),
    #                     ("JAVA", "Java Developer"),
    #                     ("C++", "C++ Developer"))
    # vacancy = models.CharField(max_length=10, choices=STATUSES_CHOICES)
