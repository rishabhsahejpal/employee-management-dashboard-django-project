from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee, Manager, EmployeeInfo, Project, KPI, Stat, Notification
from .helper import Prepare
from django.views.decorators.csrf import csrf_exempt
from .forms import UpdateForm
from django.http import JsonResponse
import json
from datetime import datetime
from django.shortcuts import redirect

def error_404(request,exception):
	return render(request,'dashboard/404.html')


def error_500(request):
	return render(request,'dashboard/500.html')


def landing(request):
	# Clear the special priveleges session here everytime
	if request.session.get('special_priveleges') == True or request.session.get('special_priveleges') == False:
		del request.session['special_priveleges']
	# Clear landing session evertime
	if request.session.get('landing') == True:
		del request.session['landing']

	try:
		request.session['landing'] = True;
	except: 
		print('session_landing_error')
	return render(request,'dashboard/landing.html')


# Create your views here.
def index(request, employee_id):
	#Check if landing session started, else send back to landing page
	if request.session.get('landing') != True:
		return redirect('/')
	else:
		# Set priveleges here	
		if request.method == 'POST':	
			if request.POST['type'] == 'basic':
				try: 
					request.session['special_priveleges'] = False
				except:
					print('session_special_priveleges_error')
			elif request.POST['type'] == 'special':
				try: 
					request.session['special_priveleges'] = True
				except:
					print('session_special_priveleges_error')

		# Prepare the databases for each try(try to put a condition after wards)
		Prepare.assign_inital()	
		# Get all notifications
		notifications = Notification.objects.all().order_by('-issued_on')# negative sign means descending
		# Get all employees
		employees_all = Employee.objects.all().order_by('team_id')
		# Get all info about employee fr9m all tables
		employee = Employee.objects.get(team_id = employee_id);
		other_info = EmployeeInfo.objects.get(employee__team_id = employee_id);
		kpis = KPI.objects.get(employee__team_id = employee_id);
		stats = Stat.objects.get(employee__team_id = employee_id);
		projects = Project.objects.filter(assigned_to__team_id = employee.team_id).order_by('-assigned_on') #This works

		data = { 
			'employee' : employee, 
			'info' : other_info, 
			'kpi' : kpis, 
			'stat' : stats, 
			'projects' : projects , 
			'employees_all' : employees_all, 
			'notifications' : notifications,
			'form' : UpdateForm,
			'page' : 'index',
			'privelege' : request.session.get('special_priveleges')
		}
		# print(employee.id)
		# print(projects[0].id)
		# print(data['info'].manager.employee.first_name)
		return render(request,'dashboard/index.html',{'data' : data})


def documentation(request):
	#Check if landing session started, else send back to landing page
	if request.session.get('landing') != True:
		return redirect('/')
	else:

		data = {'page' : 'documentation'}
		return render(request,'dashboard/documentation.html',{'data' : data})

def resources(request):
	#Check if landing session started, else send back to landing page
	if request.session.get('landing') != True:
		return redirect('/')
	else:
		data = {'page' : 'resources'}
		return render(request,'dashboard/resources.html',{'data' : data})


# All ajax calls
@csrf_exempt #to stop csrf forbidden rule
def ajax_calls(request,action):
	if request.method == 'POST':
		if action == 'remove-user':
			project_id = request.POST['id']
			team_id = request.POST['employee']
			project_to_change = Project.objects.get(id=project_id);
			employee_to_remove  = project_to_change.assigned_to.get(team_id = team_id)
			# Remove the employee from list
			project_to_change.assigned_to.remove(employee_to_remove)
			# print(project_to_change.assigned_to.all())
			return HttpResponse('deleted-project-for-user')

		elif action == 'update-project':
			project_id = request.POST['id']
			project_name = request.POST['project_name']

			project_to_update = Project.objects.get(id=project_id)
			project_to_update.project_name = project_name
			project_to_update.save()

			return JsonResponse({ 'text' : "project-name-updated" , 'project_name' : project_name })

		elif action == 'add-project':
			# new project instance
			new_project = Project()
			project_name = request.POST['input'];
			checkboxes = json.loads(request.POST.get('checkbox')) #For JSON response
			# add project name
			new_project.project_name = project_name
			#add date
			new_project.assigned_on = datetime.now()#.today().strftime('%Y-%m-%d')
			#save before
			new_project.save()
			# Add employees individually
			for obj in checkboxes:
				employee = Employee.objects.get(team_id=obj)
				# Assign employees
				new_project.assigned_to.add(employee)
			new_project.save()
			print(new_project.assigned_on)
			return JsonResponse({'text' : 'added-project', 'id' : new_project.id, 'assigned' : new_project.assigned_on })




