from django.db import models
from django.utils import timezone

# Create your models here.
class Issue(models.Model):
	status_choices = ( 
		(0,'incomplete'),
		(1,'open'),
		(2,'in-progress'),
		(3,'in-review'),
		(4,'completed')
	)
	issue_type_choices = (
		(0,'(NEW)'),
		(1,'(MOD)'),
		(2,'(BUG)')
	)
	title = models.CharField(max_length=200)
	status = models.IntegerField(status_choices, default=0)
	issue_type = models.IntegerField(issue_type_choices, default=0)
	created_date = models.DateTimeField(default = timezone.now)
	last_modified = models.DateTimeField(default = timezone.now)
	#difficulty
	project = models.ForeignKey('Project', on_delete=models.CASCADE)
