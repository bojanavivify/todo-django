from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Todo(models.Model):
    OPTION_TYPE = (
        ('To do', 'To do'),
        ('In progress', 'In progress'),
        ('Done', 'Done')
    )
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    description = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(choices=OPTION_TYPE, default='To do', max_length=12)
    closed_date = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str_(self):
        return "Todo: {}".format(self.title, self.description)

