from django.shortcuts import render
from .models import Project, Issue

##### Projects

# Index; Shows list of known projects
def project_list(request):
	projects = Project.objects.all()
	return render(request, 'projects/project_list.html', {'projects': projects})

# # projects/:id/project_view
# def project_view(request, project):
# 	view_project = Project.objects.get(id=project)
# 	return render(request, 'projects/project_view.html',{'project': view_project})

# # projects/add; Add a new project
# def project_add(request):
# 	new_project = ProjectForm(request.POST)
# 	new_project.save()
# 	return render(request, 'projects/projects_view.html', {'project': new_project})

# # projects/:id/projects_edit; Edit an edisting project
# def project_edit(request, project):
# 	population = Project.objects.get(id=project)
# 	form = ProjectForm(request.POST, instance=population)
# 	form.save()
# 	population = Project.objects.get(id=project)
# 	return redirect(request, 'project/project_view.html',{'project': population })


##### Issues

# projects/:id/issues_list; Shows list of issues for a project
def issues_list(request, project):
	issues = Issue.objects.all()
	return render(request, 'projects/issues_list.html', {'project': Project.objects.get(id=project), 'issues': issues})\

# projects/:project_id/issue/:id; Shows details for selected issue from selected project
def issues_view(request,project,issue):
	return render(request,'projects/issues_view.html', {'project': Project.objects.get(id=project), 'issue': Issue.objects.get(id=issue)})

# projects/:id/issues_add; add an issue to the current project
def issues_add(request, project):
	new_issue = IssueForm(request.POST)
	new_issue.save()
	return redirect(request, 'project/issues_list.html', {'project': Project.objects.get(id=project), 'issues': Issue.objects.all()})

# projects/:project_id/issue/:id/issues_edit; Edit an existing issue
def issues_edit(request, project, issue):
	population = Project.Objects.get(id=project)
	form = IssueForm(request.POST, instance=population)
	form.save()
	return redirect(request,'project/issues_view.html', {'project': Project.objects.get(id=project), 'issue': Issue.objects.get(id=issue)}) 