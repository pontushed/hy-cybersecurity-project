from django.db import models

from django.contrib.auth.models import User


class SafetyReport(models.Model):
    reporter = models.ForeignKey(
        User, related_name='reporter', on_delete=models.CASCADE)
    reviewer = models.ForeignKey(
        User, null=True, related_name='reviewer', on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField()
    processed = models.BooleanField(default=False)
