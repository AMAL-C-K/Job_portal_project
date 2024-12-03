from django.contrib import admin

from job_app.models import Category, Roles, Jobs

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category',)}

admin.site.register(Category, CategoryAdmin)   

class RolesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('job_role',)}


admin.site.register(Roles, RolesAdmin)
admin.site.register(Jobs) 