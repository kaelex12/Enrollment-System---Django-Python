from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin

from .models import SubjectForm, Course, YearLevel, Semester, EnrollmentStatus, Subject, OfferedSubject
from .forms import UserAdminCreationForm, UserAdminChangeForm, SubjectForm



User = get_user_model()


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'admin')
    list_filter = ('admin', 'staff', 'new_student', 'bsit_student', 'bit_student', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Information', {'fields': (   'profile_pic',
                                                'first_name',
                                                'middle_name',
                                                'last_name',
                                                'address',
                                                'mobile_num',
                                                'congressional_district',
                                                'gender',
                                                'birth_place',
                                                'birth_date',
                                                'age',
                                                'citizenship',
                                                'religion',
                                                'civil_status',
                                                'father_name',
                                                'father_occupation',
                                                'mother_name',
                                                'mother_occupation',
                                                'guardian_name',
                                                'guardian_phone_number',
                                                'elementary',
                                                'elementary_academic_year',
                                                'elementary_honors_received',
                                                'high_school',
                                                'high_school_academic_year',
                                                'high_school_honors_received',
                                                'college',
                                                'college_academic_year',
                                                'college_honors_received',)}),
        ('Permissions', {
         'fields': ('admin', 'staff', 'new_student','bsit_student','bit_student', 'is_active')}),
    )

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )
    search_fields = ('email', 'first_name', 'last_name',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.register(SubjectForm)
admin.site.register(Course)
admin.site.register(YearLevel)
admin.site.register(Semester)
admin.site.register(EnrollmentStatus)
admin.site.register(Subject)
admin.site.register(OfferedSubject)

admin.site.unregister(Group)
