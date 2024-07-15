from django.contrib import admin
from .models import Stud, Course

# Register your models here.
# admin.site.register(Stud)
# admin.site.register(Course)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'email', 'joining_date')
    search_fields = ('fname', 'lname', 'email')
    list_filter = ('joining_date',)  # Filtering by joining_date
    exclude = ('email',)  # Exclude 'email' field from the form
    #filter_vertical = ('courses',)  # Vertical filter for ManyToManyField
    date_hierarchy = 'joining_date'  # Date hierarchy based on joining_date

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'description',  'teaching_assistant')
    search_fields = ('course_name', 'teaching_assistant')
    filter_horizontal = ('students',)  # Horizontal filter for ManyToManyField
    raw_id_fields = ('teaching_assistant',)  # Raw ID field for ForeignKey

# admin.site.unregister(Stud)
# admin.site.unregister(Course)
admin.site.register(Stud, StudentAdmin)
admin.site.register(Course, CourseAdmin)