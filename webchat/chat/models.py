from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Message(models.Model):
	text = models.TextField(blank=True, null=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	file = models.FileField(upload_to='uploads/', blank=True, null=True)
	time = models.DateTimeField(auto_now_add=True)
	blimpo = models.CharField(max_length=100, blank=True, null=True)

	class Meta:
		verbose_name_plural = "Messages"

	def __str__(self):
		return self.text

	def as_dict(self):
		if self.time:
			time = self.time.strftime("%H:%M")
		else:
			time = ""

		return({
			"pk": self.pk,
			"text": self.text,
			"author": self.author,
			"file": self.file,
			"time": time,
		})
