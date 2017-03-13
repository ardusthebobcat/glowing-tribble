from django.shortcuts import render
from .models import Project, Issue

# Create your views here.
def project_list(request):
	projects = Project.objects.all()
	return render(request, 'projects/project_list.html', {'projects': projects})

def issues_list(request, project):
	issues = Issue.objects.all()
	return render(request, 'projects/issues_list.html', {'project': Project.objects.get(id=project), 'issues': issues})\

def issues_view(request,project,issue):
	return render(request,'projects/issues_view.html', {'project': Project.objects.get(id=project), 'issue': Issue.objects.get(id=issue)})

def issues_add(request, project):
	new_issue = IssueForm(request.POST)
	new_issue.save()
	return redirect(request, 'project/issues_list.html', {'project': Project.objects.get(id=project), 'issues': Issue.objects.all()})

def issues_edit(request, project, issue):
	population = Project.Objects.get(id=project)
	form = IssueForm(request.POST, instance=population)
	form.save()
	return redirect(request,'project/issues_view.html', {'project': Project.objects.get(id=project), 'issue': Issue.objects.get(id=issue)}) 