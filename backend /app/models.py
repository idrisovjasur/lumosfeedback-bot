from django.db import models

class TelegramUsers(models.Model):
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=150, null=True, blank=True)
    telegram_id = models.BigIntegerField(unique=True)

    class Meta:
        verbose_name = 'School Users'
        verbose_name_plural = 'School Users'

    def __str__(self):
        return f"{self.full_name}"


class AnonymFeedbackModel(models.Model):
    feedback = models.TextField()
    status = models.BooleanField(default=False)
    username = models.CharField(max_length=150, null=True, blank=True)
    telegram_id = models.BigIntegerField()
    def __str__(self):
        return f"{self.feedback[0:10]}"
    class Meta:
        verbose_name = 'Anonym Feedback'
        verbose_name_plural = 'Anonym Feedback'

class IdentifiedFeedbackModel(models.Model):
    feedback = models.TextField()
    status = models.BooleanField(default=False)
    full_name = models.CharField(max_length=100)
    telegram_id = models.BigIntegerField()
    username = models.CharField(max_length=150, null=True, blank=True)
    def __str__(self):
        return f"{self.feedback[0:10]}"

    class Meta:
        verbose_name = 'Identified Feedback'
        verbose_name_plural = 'Identified Feedback'

