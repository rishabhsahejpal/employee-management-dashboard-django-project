from django import forms
from django.forms import ModelForm

from .models import Project


class UpdateForm(forms.Form):
	heading = forms.CharField(
		max_length = 300,
		label='',
		# name="project",
		# class="projects flex-grow-1" ,

		)
	# class Meta:
	# 	model = Project
	# 	field = ['heading']
	# 	widgets = [
	# 		name : forms.CharField()
	# 	]
