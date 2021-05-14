from .models import SubjectForm, YearLevel, Semester, EnrollmentStatus
from django import forms
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from django.contrib import messages

User = get_user_model()


class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (
            'profile_pic',
            'first_name',
            'middle_name',
            'last_name',
            'address',
            'mobile_num',
            'congressional_district',
            'email',
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
            'college_honors_received',
            'new_student',
            'bsit_student',
            'bit_student',
        )

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = True  # send confirmation email via signals

        # obj = EmailActivation.objects.create(user=user)
        # obj.send_activation_email()
        if commit:
            user.is_active = True
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    # """
    # password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = (
            'profile_pic',
            'first_name',
            'middle_name',
            'last_name',
            'address',
            'mobile_num',
            'congressional_district',
            'email',
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
            'college_honors_received',
            'password',
            'new_student',
            'bsit_student',
            'bit_student',
            'is_active',
            'staff',
            'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        request = self.request
        data = self.cleaned_data
        email = data.get("email")
        password = data.get("password")
        user = authenticate(request, username=email, password=password)
        if user is None:
            raise forms.ValidationError("Invalid credentials")
        login(request, user)
        self.user = user
        return data


class RegisterForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    # password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    # password2 = forms.CharField(
    #     label='Password Confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name',
                  'middle_name',
                  'last_name',
                  'address',
                  'mobile_num',
                  'congressional_district',
                  'email',
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
                  'college_honors_received',
                  'new_student',
                  'bsit_student',
                  'bit_student',)

    # def clean_password2(self):
    #     # Check that the two password entries match
    #     password1 = self.cleaned_data.get("password1")
    #     password2 = self.cleaned_data.get("password2")
    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError("Passwords don't match")
    #     return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        password = User.objects.make_random_password(10)
        user.set_password(password)
        user.is_active = True  # send confirmation email via signals

        # obj = EmailActivation.objects.create(user=user)
        # obj.send_activation_email()
        if commit:
            user.save()
        return user


class NewStudentChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    # password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('first_name',
                  'middle_name',
                  'last_name',
                  'address',
                  'mobile_num',
                  'congressional_district',
                  'email',
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
                  'college_honors_received',
                  'new_student',)

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class BsitChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    # password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('first_name',
                  'middle_name',
                  'last_name',
                  'address',
                  'mobile_num',
                  'congressional_district',
                  'email',
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
                  'college_honors_received',
                  'bsit_student',)

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class BitChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    # password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('first_name',
                  'middle_name',
                  'last_name',
                  'address',
                  'mobile_num',
                  'congressional_district',
                  'email',
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
                  'college_honors_received',
                  'bit_student',)

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


# Subject Form

class StudentSubjectForm2:
    class Meta:
        model: SubjectForm
        fields = ('user', 'id_number', 'course', 'major', 'year_level', 'school_year',
                  'semester', 'enrollment_status', 'student_status', 'block_section')


class UpdateStudentSubjectForm:
    class Meta:
        model: SubjectForm
        fields = ('user', 'id_number', 'course', 'major', 'year_level', 'school_year',
                  'semester', 'enrollment_status', 'student_status', 'block_section')

class StudentSubjectForm(forms.ModelForm):
    class Meta:
        model = SubjectForm
        fields = ('id_number', 'course', 'major', 'year_level', 'school_year',
                  'semester', 'enrollment_status', 'student_status', 'block_section')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # year_level
        self.fields['year_level'].queryset = YearLevel.objects.none()

        if 'course' in self.data:
            try:
                course_id = int(self.data.get('course'))
                self.fields['year_level'].queryset = YearLevel.objects.filter(
                    course=course_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Year_level queryset
        elif self.instance.pk:
            self.fields['year_level'].queryset = self.instance.course.year_level_set.order_by(
                'name')

        # semester
        self.fields['semester'].queryset = Semester.objects.none()

        if 'year_level' in self.data:
            try:
                year_level_id = int(self.data.get('year_level'))
                self.fields['semester'].queryset = Semester.objects.filter(
                    year_level_id=year_level_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Year_level queryset
        elif self.instance.pk:
            self.fields['semester'].queryset = self.instance.course.year_level.semester_set.order_by(
                'name')

        # enrollment_status
        self.fields['enrollment_status'].queryset = EnrollmentStatus.objects.none()

        if 'semester' in self.data:
            try:
                semester_id = int(self.data.get('semester'))
                self.fields['enrollment_status'].queryset = EnrollmentStatus.objects.filter(
                    semester_id=semester_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Year_level queryset
        elif self.instance.pk:
            self.fields['enrollment_status'].queryset = self.instance.course.year_level.semester.enrollment_status_set.order_by(
                'name')



