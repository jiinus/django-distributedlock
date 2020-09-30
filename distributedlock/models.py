from django.db import models
from django.dispatch import receiver
from datetime import datetime

class Lock(models.Model):
    key = models.CharField(max_length=255, blank=False, unique=True)
    value = models.CharField(max_length=255, blank=False)
    timestamp = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Lock'
        verbose_name_plural = 'Locks'

    def __unicode__(self):
        return self.key


@receiver([models.signals.pre_save,], sender=Lock)
def on_lock_saving(sender, instance, **kwargs):
	if instance.timestamp is None:
		instance.timestamp = datetime.now()