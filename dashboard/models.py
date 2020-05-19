from django.db import models

# Create your models here.
class Employee(models.Model):
	first_name = models.CharField(max_length = 40)
	last_name = models.CharField(max_length = 40)
	team_id = models.IntegerField()
	
	def __str__(self):
		return self.first_name+' '+self.last_name


class Manager(models.Model):
	employee = models.ForeignKey(Employee,on_delete = models.CASCADE,null = True,related_name='manager_name')
	employees = models.ManyToManyField(Employee,related_name='direct_reports')

	def __str__(self):
		return self.employee.first_name + ' '+ self.employee.last_name

	def manager_direct_reports(self):
		return "\n, ".join([(report.first_name +' '+ report.last_name) for report in self.employees.all()])



class EmployeeInfo(models.Model):
	employee = models.ForeignKey(Employee,on_delete = models.CASCADE, null = True,related_name="_info_of_employee_name")
	joined_on = models.DateField()
	email = models.EmailField(max_length=255, null=True)
	contact = models.CharField(max_length=17,default='+1 (111) 222-3333') #No min length option
	designation = models.CharField(max_length=100,default='Developer')
	manager = models.ForeignKey(Manager,on_delete = models.CASCADE)
	
	def __str__(self):
		return self.employee.first_name + ' '+ self.employee.last_name


class Project(models.Model):
	project_name = models.CharField(max_length = 150)
	assigned_on = models.DateField()
	assigned_to = models.ManyToManyField(Employee,related_name='employeed_assigned_to')
	
	def __str__(self):
		return self.project_name

	def projects_assigned_to(self):
		return "\n, ".join([(assigned.first_name +' '+ assigned.last_name) for assigned in self.assigned_to.all()])

class KPI(models.Model):
	employee = models.ForeignKey(Employee,on_delete = models.CASCADE, null = True,related_name="kpi_employee_name")
	efficiency = models.IntegerField(default = 0)
	overall_performance = models.IntegerField(default = 0)
	kpi_1 = models.IntegerField(default = 0)
	kpi_2 = models.IntegerField(default = 0)
	kpi_3 = models.IntegerField(default = 0)
	efficiency_yearly = models.IntegerField(default = 0)
	overall_performance_yearly = models.IntegerField(default = 0)
	kpi_1_yearly = models.IntegerField(default = 0)
	kpi_2_yearly = models.IntegerField(default = 0)
	kpi_3_yearly = models.IntegerField(default = 0)

	def __str__(self):
		return self.employee.first_name + ' '+ self.employee.last_name

class Stat(models.Model):
	employee = models.ForeignKey(Employee,on_delete = models.CASCADE, null = True,related_name="stats_employee_name")
	total_work_days = models.IntegerField(default = 0)
	paid_leaves = models.IntegerField(default = 0)
	sick_leaves = models.IntegerField(default = 0)
	unpaid_leaves = models.IntegerField(default = 0)
	total_work_days_yearly = models.IntegerField(default = 0)
	paid_leaves_yearly = models.IntegerField(default = 0)
	sick_leaves_yearly = models.IntegerField(default = 0)
	unpaid_leaves_yearly = models.IntegerField(default = 0)

	def __str__(self):
		return self.employee.first_name + ' '+ self.employee.last_name


class Notification(models.Model):
	name = models.CharField(max_length = 150)
	issued_on = models.DateField()

	def __str__(self):
		return self.name
