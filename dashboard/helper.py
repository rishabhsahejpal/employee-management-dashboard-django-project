from .models import Employee, Manager, EmployeeInfo, Project, KPI, Stat
from datetime import datetime

class Data:
	def get_employees():
	 return  [
			{
				'first_name' : 'John',
				'last_name' : 'Markwell',
				'team_id' : 1
			},
			{
				'first_name' : 'Robert',
				'last_name' : 'Doe',
				'team_id' : 2
			},
			{
				'first_name' : 'Jane',
				'last_name' : 'Mitchell',
				'team_id' : 3
			},
			{
				'first_name' : 'Alicia',
				'last_name' : 'Smith',
				'team_id' : 4
			},
			{
				'first_name' : 'Robert',
				'last_name' : 'Maxwell',
				'team_id' : 5
			},
			{
				'first_name' : 'James',
				'last_name' : 'Smith',
				'team_id' : 6
			}
		]

	def get_managers():
		return  [
			{
				'employee' : Employee.objects.get(team_id = 1,first_name='John'),
				'employees' : Employee.objects.filter(team_id = 2 ) | Employee.objects.filter(team_id = 4 ) | Employee.objects.filter(team_id = 5 )
			},
			{
				'employee' : Employee.objects.get(team_id = 3),
				'employees' : Employee.objects.filter(team_id = 6)
			}
		]


	def get_employee_info():
		return [
			{
				'employee' : Employee.objects.get(team_id = 1),
				'joined_on' : datetime(2019,2,15),
				'manager' : Manager.objects.get(employee__team_id = 1),
				'email' : 'johnmarkwell@company.com',
				'contact' : '+1(437) 222-3333',
				'designation' : 'Manager'

			},
				{
				'employee' : Employee.objects.get(team_id = 2),
				'joined_on' : datetime(2020,1,18),
				'manager' : Manager.objects.get(employee__team_id = 1),
				'email' : 'robertdoe@company.com',
				'contact' : '+1(437) 333-1234',
				'designation' : 'Front-end  Developer'
			},
			{
				'employee' : Employee.objects.get(team_id = 3),
				'joined_on' : datetime(2019,5,10),
				'manager' : Manager.objects.get(employee__team_id = 3),
				'email' : 'janemitchell@company.com',
				'contact' : '+1(514) 410-3333',
				'designation' : 'Manager'
			},
			{
				'employee' : Employee.objects.get(team_id = 4),
				'joined_on' : datetime(2019,12,5),
				'manager' : Manager.objects.get(employee__team_id = 1),
				'email' : 'aliciasmith@company.com',
				'contact' : '+1(501) 222-4141',
				'designation' : 'Junior Developer'
			},
			{
				'employee' : Employee.objects.get(team_id = 5),
				'joined_on' : datetime(2020,2,29),
				'manager' : Manager.objects.get(employee__team_id = 1),
				'email' : 'robertmaxwell@company.com',
				'contact' : '+1(403) 210-8874',
				'designation' : 'Full-Stack Developer'
			},
			{
				'employee' : Employee.objects.get(team_id = 6),
				'joined_on' : datetime(2020,4,20),
				'manager' : Manager.objects.get(employee__team_id = 3),
				'email' : 'jamesmith@company.com',
				'contact' : '+1(410) 111-2222',
				'designation' : 'Android Developer'
			}
		]

	def get_projects():
		return [
			{
				'project_name' : "Django Project 2.0",
				'assigned_on' : datetime(2020,2,2),
				'assigned_to' : Employee.objects.filter(team_id = 2 ) | Employee.objects.filter(team_id = 4 ) | Employee.objects.filter(team_id = 5 )
			},
			{
				'project_name' : "React JS Project",
				'assigned_on' : datetime(2019,9,9),
				'assigned_to' : Employee.objects.filter(team_id = 1 ) | Employee.objects.filter(team_id = 2 )
			},
			{
				'project_name' : "Client A Project",
				'assigned_on' : datetime(2019,7,18),
				'assigned_to' : Employee.objects.filter(team_id = 4 ) | Employee.objects.filter(team_id = 6 ) | Employee.objects.filter(team_id = 5 )
			},
			{
				'project_name' : "Client B Project",
				'assigned_on' : datetime(2019,7,11),
				'assigned_to' : Employee.objects.filter(team_id = 1 ) | Employee.objects.filter(team_id = 6 ) | Employee.objects.filter(team_id = 5 )
			},
			{
				'project_name' : "Django Project 1.0",
				'assigned_on' : datetime(2019,10,5),
				'assigned_to' : Employee.objects.filter(team_id = 2 ) | Employee.objects.filter(team_id = 3 ) | Employee.objects.filter(team_id = 5 )
			},
			{
				'project_name' : "Node JS and React JS project",
				'assigned_on' : datetime(2019,12,19),
				'assigned_to' : Employee.objects.filter(team_id = 2 ) | Employee.objects.filter(team_id = 3 ) | Employee.objects.filter(team_id = 5 )
			},
			{
				'project_name' : "Front end project for client z",
				'assigned_on' : datetime(2020,4,15),
				'assigned_to' : Employee.objects.filter(team_id = 2 ) | Employee.objects.filter(team_id = 1 ) | Employee.objects.filter(team_id = 6 )
			},
			{
				'project_name' : "Full website(Front end and backend)",
				'assigned_on' : datetime(2020,3,10),
				'assigned_to' : Employee.objects.filter(team_id = 3 ) | Employee.objects.filter(team_id = 4 ) | Employee.objects.filter(team_id = 6 )
			},
			{
				'project_name' : "Project related to client C and D togethter",
				'assigned_on' : datetime(2020,1,12),
				'assigned_to' : Employee.objects.filter(team_id = 2 ) | Employee.objects.filter(team_id = 4 ) | Employee.objects.filter(team_id = 3 )
			},
		]

	def get_kpi():
		return [
			{
				'employee' : Employee.objects.get(team_id = 1),
				'efficiency' : 65,
				'overall_performance' : 60 ,
				'kpi_1' : 85,
				'kpi_2' : 95,
				'kpi_3' : 93,
				'efficiency_yearly' : 85,
				'overall_performance_yearly' : 80 ,
				'kpi_1_yearly' : 80,
				'kpi_2_yearly' : 40,
				'kpi_3_yearly' : 65
			},
			{
				'employee' : Employee.objects.get(team_id = 2),
				'efficiency' : 65,
				'overall_performance' : 63 ,
				'kpi_1' : 81,
				'kpi_2' : 91,
				'kpi_3' : 74,
				'efficiency_yearly' : 70,
				'overall_performance_yearly' : 70 ,
				'kpi_1_yearly' : 35,
				'kpi_2_yearly' : 75,
				'kpi_3_yearly' : 73
			},
			{
				'employee' : Employee.objects.get(team_id = 3),
				'efficiency' : 75,
				'overall_performance' : 60 ,
				'kpi_1' : 80,
				'kpi_2' : 90,
				'kpi_3' : 90,
				'efficiency_yearly' : 55,
				'overall_performance_yearly' : 80 ,
				'kpi_1_yearly' : 65,
				'kpi_2_yearly' : 85,
				'kpi_3_yearly' : 83
			},
			{
				'employee' : Employee.objects.get(team_id = 4),
				'efficiency' : 75,
				'overall_performance' : 60 ,
				'kpi_1' : 65,
				'kpi_2' : 50,
				'kpi_3' : 55,
				'efficiency_yearly' : 55,
				'overall_performance_yearly' : 50 ,
				'kpi_1_yearly' : 75,
				'kpi_2_yearly' : 80,
				'kpi_3_yearly' : 83
			},
			{
				'employee' : Employee.objects.get(team_id = 5),
				'efficiency' : 60,
				'overall_performance' : 90 ,
				'kpi_1' : 80,
				'kpi_2' : 65,
				'kpi_3' : 90,
				'efficiency_yearly' : 55,
				'overall_performance_yearly' : 55 ,
				'kpi_1_yearly' : 75,
				'kpi_2_yearly' : 75,
				'kpi_3_yearly' : 83
			},
			{
				'employee' : Employee.objects.get(team_id = 6),
				'efficiency' : 75,
				'overall_performance' : 80 ,
				'kpi_1' : 55,
				'kpi_2' : 45,
				'kpi_3' : 100,
				'efficiency_yearly' : 55,
				'overall_performance_yearly' : 50 ,
				'kpi_1_yearly' : 75,
				'kpi_2_yearly' : 85,
				'kpi_3_yearly' : 73
			}
		]

	def get_stats():
		return [
			{
				'employee' : Employee.objects.get(team_id = 1),
				'total_work_days' : 15,
				'paid_leaves' : 0 ,
				'sick_leaves' : 0,
				'unpaid_leaves' : 5,
				'total_work_days_yearly' : 193,
				'paid_leaves_yearly' : 1,
				'sick_leaves_yearly' : 5 ,
				'unpaid_leaves_yearly' : 10,
			},
			{
				'employee' : Employee.objects.get(team_id = 2),
				'total_work_days' : 15,
				'paid_leaves' : 0 ,
				'sick_leaves' : 0,
				'unpaid_leaves' : 5,
				'total_work_days_yearly' : 103,
				'paid_leaves_yearly' : 1,
				'sick_leaves_yearly' : 5 ,
				'unpaid_leaves_yearly' : 10,
			},
			{
				'employee' : Employee.objects.get(team_id = 3),
				'total_work_days' : 15,
				'paid_leaves' : 0 ,
				'sick_leaves' : 0,
				'unpaid_leaves' : 5,
				'total_work_days_yearly' : 111,
				'paid_leaves_yearly' : 1,
				'sick_leaves_yearly' : 5 ,
				'unpaid_leaves_yearly' : 6,
			},
			{
				'employee' : Employee.objects.get(team_id = 4),
				'total_work_days' : 15,
				'paid_leaves' : 0 ,
				'sick_leaves' : 0,
				'unpaid_leaves' : 5,
				'total_work_days_yearly' : 83,
				'paid_leaves_yearly' : 1,
				'sick_leaves_yearly' : 5 ,
				'unpaid_leaves_yearly' : 10,
			},
			{
				'employee' : Employee.objects.get(team_id = 5),
				'total_work_days' : 15,
				'paid_leaves' : 1 ,
				'sick_leaves' : 0,
				'unpaid_leaves' : 0,
				'total_work_days_yearly' : 103,
				'paid_leaves_yearly' : 2,
				'sick_leaves_yearly' : 5 ,
				'unpaid_leaves_yearly' : 0,
			},
			{
				'employee' : Employee.objects.get(team_id = 6),
				'total_work_days' : 15,
				'paid_leaves' : 0 ,
				'sick_leaves' : 0,
				'unpaid_leaves' : 5,
				'total_work_days_yearly' : 92,
				'paid_leaves_yearly' : 3,
				'sick_leaves_yearly' : 0 ,
				'unpaid_leaves_yearly' : 0,
			}
		]	


class Prepare:
	def assign_inital():
		# If employees data-base is empty, then only assign employee
		if(Employee.objects.all().count() == 0):
			# Add Employees
			employees = Data.get_employees()
			# Loop
			for i in employees:
				e = Employee(
					first_name = i['first_name'],
					last_name = i['last_name'],
					team_id = i['team_id']
				) 
				e.save();

		# If manager data-base is empty, then only assign manager
		if(Manager.objects.all().count() == 0):
			# Now assign managers -after employees are entered	
			# Add Managers
			managers = Data.get_managers()
			# Loop
			for i in managers:	
			 	#Direct assignment for man to many doesnot work with '=' 
				m = Manager(employee = i['employee'])
				m.save();
				m.employees.set(i['employees'])

		# If employeeinfo data-base is empty, then only assign employeeinfo
		if(EmployeeInfo.objects.all().count() == 0):
			# Now enter Employees' Info
			# Add Employee Info
			employee_info = Data.get_employee_info()
			# Loop
			for i in employee_info:
				info = EmployeeInfo(
					employee = i['employee'],
					joined_on = i['joined_on'],
					manager = i['manager'],
					contact = i['contact'],
					email = i['email'],
					designation = i['designation'],
				) 
				info.save();

		# If employeeinfo data-base is empty, then only assign employeeinfo
		if(KPI.objects.all().count() == 0):
			# Now enter KPIS after empoyeeinfo
			# Add KPIs
			kpi = Data.get_kpi()
			# Loop
			for i in kpi:
				k = KPI(
					employee = i['employee'] ,
					efficiency = i['efficiency'],
					overall_performance = i['overall_performance'],
					kpi_1 = i['kpi_1'],
					kpi_2 = i['kpi_2'],
					kpi_3 = i['kpi_3'],
					efficiency_yearly = i['efficiency_yearly'],
					overall_performance_yearly = i['overall_performance_yearly'],
					kpi_1_yearly = i['kpi_1_yearly'],
					kpi_2_yearly = i['kpi_2_yearly'],
					kpi_3_yearly = i['kpi_3_yearly']
				)
				k.save();

		# If stats data-base is empty, then only assign stats
		if(Stat.objects.all().count() == 0):
			# Now enter stats after kpi
			# Add Stats
			stat = Data.get_stats()
			# Loop
			for i in stat:
				s = Stat(
					employee = i['employee'] ,
					total_work_days = i['total_work_days'],
					paid_leaves = i['paid_leaves'],
					sick_leaves = i['sick_leaves'],
					unpaid_leaves = i['unpaid_leaves'],
					total_work_days_yearly = i['total_work_days_yearly'],
					paid_leaves_yearly = i['paid_leaves_yearly'],
					sick_leaves_yearly = i['sick_leaves_yearly'],
					unpaid_leaves_yearly = i['unpaid_leaves_yearly']
				)
				s.save();

		# Only alter project database, if it has less than or more than 9 projects and update accordingly
		# Project.objects.all().delete() # it keeps deleting my added projects
		# total_projects = Project.objects.all().count()
		# if(total_projects < 9 or total_projects > 9):
		# 	if(total_projects < 9):
		# 		difference = 9 - 
		# Now add Projects
		if Project.objects.all().count() == 0:#delete it later
			projects = Data.get_projects()
			# Loop
			for i in projects:
				p = Project(
					project_name = i['project_name'],
					assigned_on = i['assigned_on']
				)
				p.save();
				p.assigned_to.set(i['assigned_to'])

		# else:
		# 	print('Projects DB is of right size')
