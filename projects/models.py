from django.db import models
from django.utils import timezone
from django.forms import ModelForm
import pdb

# Global vars - use very sparingly
new_type = 0
mod_type = 1
bug_type = 2

issue_type_choices = (
	(new_type,'(NEW)'),
	(mod_type,'(MOD)'),
	(bug_type,'(BUG)')
)

# Create your models here.
class Project(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	label = models.CharField(max_length=8)

	def __str__(self):
		return self.title

	def label(self):
		return self.label

class Issue(models.Model):
	status_choices = ( 
		(0,'incomplete'),
		(1,'open'),
		(2,'in-progress'),
		(3,'in-review'),
		(4,'completed')
	)

	title = models.CharField(max_length=200)
	status = models.IntegerField(choices = status_choices, default=0)
	issue_type = models.IntegerField(choices = issue_type_choices, default=new_type)
	created_date = models.DateTimeField(default = timezone.now)
	last_modified = models.DateTimeField(default = timezone.now)
	#difficulty
	project = models.ForeignKey('Project', on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	@property
	def compiled_(self):
		compiled = self.issue_type + " - " + self.title
		return compiled

	@property
	def i_type(self):
		return issue_type_choices[self.issue_type][1]

	def get_keys(self):
		r = self.__dict__
		print(r)
		return r

	def issue_value_lookup(issue, key):
		pdb.set_trace()
		r = Issue.objects.get(issue)(key)
		return r


class IssueForm(ModelForm):
	class Meta:
		model = Issue
		fields = ['title','status','issue_type','project']