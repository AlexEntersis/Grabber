from django.db import models



class Comments(models.Model):
    comment_author = models.CharField(max_length=300, null=False)
    comment_date = models.DateField(default=None, null=False)
    comment_text = models.TextField(null=False, default=None)
    comment_vacancy = models.CharField(max_length=20, null=False, default=None)

