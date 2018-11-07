# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Articles(models.Model):
	title = models.CharField(max_length=120)
	posts = models.TextField()
	date = models.DateTimeField()
	
	def __str__(self):
		return self.title
