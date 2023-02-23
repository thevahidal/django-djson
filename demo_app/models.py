from django.db import models


class Demo(models.Model):
    payload = models.JSONField()

    def __str__(self):
        return str(self.id)
