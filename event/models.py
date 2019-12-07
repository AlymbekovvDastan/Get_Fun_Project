from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
	name = models.CharField(max_length=50, blank=False, null=False)


	def __str__(self):
		return self.name


class Tag(models.Model):
	title = models.CharField(max_length=50)


	def __str__(self):
		return self.title


class Event(models.Model):
	title = models.CharField(max_length=250, blank=False, null=False)
	desecription = models.TextField()
	date =  models.DateField(null=True, blank=True)
	adress = models.CharField(max_length=250, blank=True, null=False)
	price = models.CharField(max_length=50)
	category = models.ForeignKey(Category, related_name="categoryes", on_delete=models.CASCADE)
	tags  = models.ManyToManyField(Tag, blank=True, related_name='events')
	foto = models.ImageField(upload_to='')
	favorites = models.ManyToManyField(User, blank=True, related_name='favorites')

	def __str__(self):
		return self.title



class Comment(models.Model):
	user = models.ForeignKey(User, related_name="users", on_delete=models.CASCADE)
	text = models.CharField(max_length=500, blank=False, null=False)
	event = models.ForeignKey(Event, related_name="events", on_delete=models.CASCADE)


	def __str__(self):
		return self.text

