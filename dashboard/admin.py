from django.contrib import admin
from .models import Employee,Manager,EmployeeInfo, Project, KPI, Stat, Notification

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
	fields = ['first_name','last_name','team_id']
	list_display = ('first_name','last_name','team_id')


class ManagerAdmin(admin.ModelAdmin):
	fields = ['employee','employees']
	list_display = ('employee','manager_direct_reports')


class EmployeeInfoAdmin(admin.ModelAdmin):
	fields = ['employee','joined_on','email','contact','designation','manager']
	list_display = ('employee','joined_on','email','contact','designation','manager')


class ProjectsAdmin(admin.ModelAdmin):
	fields = ['project_name','assigned_on','assigned_to']
	list_display = ('project_name','assigned_on','projects_assigned_to')


class KPIAdmin(admin.ModelAdmin):
	fields = ['employee','efficiency','overall_performance','kpi_1','kpi_2','kpi_3','efficiency_yearly','overall_performance_yearly','kpi_1_yearly','kpi_2_yearly','kpi_3_yearly']
	list_display = ('employee','efficiency','overall_performance','kpi_1','kpi_2','kpi_3','efficiency_yearly','overall_performance_yearly','kpi_1_yearly','kpi_2_yearly','kpi_3_yearly')


class StatAdmin(admin.ModelAdmin):
	fields = ['employee','total_work_days','paid_leaves','sick_leaves','unpaid_leaves','total_work_days_yearly','paid_leaves_yearly','sick_leaves_yearly','unpaid_leaves_yearly']
	list_display = ('employee','total_work_days','paid_leaves','sick_leaves','unpaid_leaves','total_work_days_yearly','paid_leaves_yearly','sick_leaves_yearly','unpaid_leaves_yearly')


class NotificationAdmin(admin.ModelAdmin):
	fields  = ['name','issued_on']
	list_display = ('name','issued_on')


# Register your models to the admin
admin.site.register( Employee, EmployeeAdmin )
admin.site.register( Manager, ManagerAdmin )
admin.site.register( EmployeeInfo, EmployeeInfoAdmin )
admin.site.register( Project, ProjectsAdmin )
admin.site.register( KPI, KPIAdmin )
admin.site.register( Stat, StatAdmin )
admin.site.register( Notification, NotificationAdmin )