from django.db import models

# Create your models here.

class Mineral(models.Model):
	'''
		Model for the Mineral relation.
	'''
	name = models.CharField(max_length=300, null=True)
	img_filename = models.CharField(max_length=300, null=True)
	img_caption = models.CharField(max_length=300, null=True)
	category = models.CharField(max_length=300, null=True)
	formula = models.CharField(max_length=300, null=True)
	strunz_class = models.CharField(max_length=300, null=True)
	color = models.CharField(max_length=300, null=True)
	crystal_sys = models.CharField(max_length=300, null=True)
	unit_cell = models.CharField(max_length=300, null=True)
	crystal_sym = models.CharField(max_length=300, null=True)
	cleavage = models.CharField(max_length=300, null=True)
	mohs = models.CharField(max_length=300, null=True)
	luster = models.CharField(max_length=300, null=True)
	streak = models.CharField(max_length=300, null=True)
	diaphaneity = models.CharField(max_length=300, null=True)
	optical_prop = models.CharField(max_length=300, null=True)
	refractive_inx = models.CharField(max_length=300, null=True)
	crystal_habit = models.CharField(max_length=300, null=True)
	spec_gravity = models.CharField(max_length=300, null=True)