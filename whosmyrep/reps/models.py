from django.db import models
from django.contrib.auth.models import User

class Rep(models.Model):
	first_name = models.CharField('first name', max_length=200)
	middle_name = models.CharField('middle name', max_length=200, blank=True)
	last_name = models.CharField('last name', max_length=200)
	birth_on = models.DateField('birth day', blank=True, null=True)
	twitter = models.CharField('twitter id', max_length=200, blank=True)
	link = models.CharField('web site', max_length=200, blank=True)
	youtube = models.CharField('youtube id', max_length=200, blank=True)
	elected_on = models.DateField('elected on', blank=True, null=True)
	term_until = models.DateField('term until', blank=True, null=True)
	avg_rank = models.DecimalField('rank', max_digits=4, decimal_places=2, blank=True, null=True)
	created_on = models.DateField('created on')
	
	def full_name():
		self.first_name + ' ' + self.middle_name + ' ' + self.last_name
	
	def __unicode__(self):
		return self.first_name
		
class Rank(models.Model):
	user = models.ForeignKey(User)
	rep = models.ForeignKey(Rep)
	rank = models.PositiveSmallIntegerField()
	
	def __unicode__(self):
		return self.user +' - ' + self.rep + ' - ' + str(self.rank)
