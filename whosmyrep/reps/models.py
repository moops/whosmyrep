from django.db import models

class Rep(models.Model):
	first_name = models.CharField('first name', max_length=200)
	middle_name = models.CharField('middle name', max_length=200, blank=True, null=True)
	last_name = models.CharField('last name', max_length=200)
	birth_on = models.DateTimeField('birth day', blank=True, null=True)
	twitter = models.CharField('twitter id', max_length=200, blank=True, null=True)
	link = models.CharField('web site', max_length=200, blank=True, null=True)
	youtube = models.CharField('youtube id', max_length=200, blank=True, null=True)
	elected_on = models.DateTimeField('elected on', blank=True, null=True)
	term_until = models.DateTimeField('term until', blank=True, null=True)
	created_on = models.DateTimeField('created on')
	
	def full_name():
		self.first_name + ' ' + self.middle_name + ' ' + self.last_name
	
	def __unicode__(self):
		return self.first_name
