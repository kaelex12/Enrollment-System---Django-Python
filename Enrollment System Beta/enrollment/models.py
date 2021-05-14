from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from django.utils import timezone


class UserManager(BaseUserManager):

    def create_user(self, email,
                    full_name=None,
                    first_name=None,
                    middle_name=None,
                    last_name=None,
                    address=None,
                    mobile_num=None,
                    congressional_district=None,
                    gender=None,
                    birth_place=None,
                    birth_date=None,
                    age=None,
                    citizenship=None,
                    religion=None,
                    civil_status=None,
                    father_name=None,
                    father_occupation=None,
                    mother_name=None,
                    mother_occupation=None,
                    guardian_name=None,
                    guardian_phone_number=None,
                    elementary=None,
                    elementary_academic_year=None,
                    elementary_honors_received=None,
                    high_school=None,
                    high_school_academic_year=None,
                    high_school_honors_received=None,
                    college=None,
                    college_academic_year=None,
                    college_honors_received=None, password=None,
                    is_new_student=True,
                    is_bsit_student=False,
                    is_bit_student=False,
                    is_active=True,  is_staff=False, is_admin=False):
        """
        Creates and saves a User with the given email and password.
        """

        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError("Users must have a password")

        # def phone_number_isValid(phone1, phone2):
        #     Pattern = re.compile("(0)?[11][0-9]{9}")
        #     return Pattern.match(phone1, phone2)

        # if (phone_number_isValid(mobile_num, guardian_phone_number)):
        user_obj = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            address=address,
            mobile_num=mobile_num,
            congressional_district=congressional_district,
            gender=gender,
            birth_place=birth_place,
            birth_date=birth_date,
            age=age,
            citizenship=citizenship,
            religion=religion,
            civil_status=civil_status,
            father_name=father_name,
            father_occupation=father_occupation,
            mother_name=mother_name,
            mother_occupation=mother_occupation,
            guardian_name=guardian_name,
            guardian_phone_number=guardian_phone_number,
            elementary=elementary,
            elementary_academic_year=elementary_academic_year,
            elementary_honors_received=elementary_honors_received,
            high_school=high_school,
            high_school_academic_year=high_school_academic_year,
            high_school_honors_received=high_school_honors_received,
            college=college,
            college_academic_year=college_academic_year,
            college_honors_received=college_honors_received
        )
        # else:
        #     raise ValueError("Invalid Phone Number")

        user_obj.set_password(password)  # change user password
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.new_student = is_new_student
        user_obj.bsit_student = is_bsit_student
        user_obj.bit_student = is_bit_student
        user_obj.is_active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, full_name=None, password=None):
        user = self.create_user(
            email,
            full_name=full_name,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, email, full_name=None, password=None):
        user = self.create_user(
            email,
            full_name=full_name,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)

    # persnol information
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    CIVIL_STATUS = (
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widow', 'Widow'),
    )

    full_name = models.CharField(max_length=255, blank=True, null=True)

    profile_pic = models.ImageField(
        default="defaultprofile.png", null=True, blank=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    mobile_num = models.CharField(max_length=11, blank=True, null=True)
    congressional_district = models.CharField(
        max_length=50, blank=True, null=True)
    gender = models.CharField(
        max_length=50, blank=True, choices=GENDER, null=True)
    birth_place = models.CharField(max_length=50, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    citizenship = models.CharField(max_length=50, blank=True, null=True)
    religion = models.CharField(max_length=50, blank=True, null=True)
    civil_status = models.CharField(
        max_length=50, blank=True, choices=CIVIL_STATUS, null=True)
    father_name = models.CharField(max_length=50, blank=True, null=True)
    father_occupation = models.CharField(max_length=50, blank=True, null=True)
    mother_name = models.CharField(max_length=50, blank=True, null=True)
    mother_occupation = models.CharField(max_length=50, blank=True, null=True)
    guardian_name = models.CharField(max_length=50, blank=True, null=True)
    guardian_phone_number = models.CharField(
        max_length=11, blank=True, null=True)
    elementary = models.CharField(max_length=50, blank=True, null=True)
    elementary_academic_year = models.CharField(
        max_length=50, blank=True, null=True)
    elementary_honors_received = models.CharField(
        max_length=50, blank=True, null=True)
    high_school = models.CharField(max_length=50, blank=True, null=True)
    high_school_academic_year = models.CharField(
        max_length=50, blank=True, null=True)
    high_school_honors_received = models.CharField(
        max_length=50, blank=True, null=True)
    college = models.CharField(max_length=50, blank=True, null=True)
    college_academic_year = models.CharField(
        max_length=50, blank=True, null=True)
    college_honors_received = models.CharField(
        max_length=50, blank=True, null=True)

    new_student = models.BooleanField(default=True)
    bsit_student = models.BooleanField(default=False)
    bit_student = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # staff user non superuser
    admin = models.BooleanField(default=False)  # superuser
    timestamp = models.DateTimeField(auto_now_add=True)

    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Email & Password are required by default.

    objects = UserManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_new_student(self):
        return self.new_student

    @property
    def is_bsit_student(self):
        return self.bsit_student

    @property
    def is_bit_student(self):
        return self.bit_student

    @property
    def is_staff(self):
        "Is the user a member of staff?"

        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

# Subject Form


class Course(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class YearLevel(models.Model):
    Year_Level = (
        ('1st', '1st'),
        ('2nd', '2nd'),
        ('3rd', '3rd'),
        ('4th', '4th'),
    )
    name = models.CharField(max_length=30, blank=True,
                            null=True, choices=Year_Level)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Semester(models.Model):
    Semesters = (
        ('1st', '1st'),
        ('2nd', '2nd'),
    )
    name = models.CharField(max_length=30, blank=True,
                            null=True, choices=Semesters)
    year_level = models.ForeignKey(YearLevel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Subject(models.Model):
    course_code = models.CharField(max_length=50, blank=True, null=True)
    descriptive_title = models.CharField(max_length=50, blank=True, null=True)
    pre_requisite = models.CharField(max_length=50, blank=True, null=True)
    unit = models.IntegerField(blank=True, null=True)
    num_hours_lec = models.IntegerField(blank=True, null=True)
    num_hours_lab = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.descriptive_title


class OfferedSubject(models.Model):
    Day = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
    )
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, blank=True, null=True)
    mis_code = models.CharField(max_length=50, blank=True, null=True)
    select = models.BooleanField(default=False)
    time = models.CharField(max_length=50, blank=True, null=True)
    day = models.CharField(max_length=50, blank=True, null=True, choices=Day)
    room = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.mis_code


class EnrollmentStatus(models.Model):
    Enrollment_Status = (
        ('Regular', 'Regular'),
        ('Irregular', 'Irregular'),
    )
    name = models.CharField(max_length=100, blank=True,
                            null=True, choices=Enrollment_Status)
    identifier_regular = models.BooleanField(default=False)
    identifier_irregular = models.BooleanField(default=False)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    mis_code1 = models.ForeignKey(
        OfferedSubject, on_delete=models.CASCADE, related_name='mis_code_set1')
    mis_code2 = models.ForeignKey(
        OfferedSubject, on_delete=models.CASCADE, related_name='mis_code_set2')
    mis_code3 = models.ForeignKey(
        OfferedSubject, on_delete=models.CASCADE, related_name='mis_code_set3')
    mis_code4 = models.ForeignKey(
        OfferedSubject, on_delete=models.CASCADE, related_name='mis_code_set4')
    mis_code5 = models.ForeignKey(
        OfferedSubject, on_delete=models.CASCADE, related_name='mis_code_set5')
    mis_code6 = models.ForeignKey(
        OfferedSubject, on_delete=models.CASCADE, related_name='mis_code_set6')
    mis_code7 = models.ForeignKey(
        OfferedSubject, on_delete=models.CASCADE, related_name='mis_code_set7')
    mis_code8 = models.ForeignKey(
        OfferedSubject, on_delete=models.CASCADE, related_name='mis_code_set8')
    mis_code9 = models.ForeignKey(
        OfferedSubject, on_delete=models.CASCADE, related_name='mis_code_set9')
    mis_codeA = models.ForeignKey(
        OfferedSubject, on_delete=models.CASCADE, related_name='mis_code_setA')
    mis_codeB = models.ForeignKey(
        OfferedSubject, on_delete=models.CASCADE, related_name='mis_code_setB')
    mis_codeC = models.ForeignKey(
        OfferedSubject, on_delete=models.CASCADE, related_name='mis_code_setC')
    mis_codeD = models.ForeignKey(
        OfferedSubject, on_delete=models.CASCADE, related_name='mis_code_setD')
    mis_codeE = models.ForeignKey(
        OfferedSubject, on_delete=models.CASCADE, related_name='mis_code_setE')
    mis_codeF = models.ForeignKey(
        OfferedSubject, on_delete=models.CASCADE, related_name='mis_code_setF')

    def __str__(self):
        return self.name


class SubjectForm(models.Model):
    Student_Status = (
        ('New', 'New'),
        ('Old', 'Old'),
        ('Transferee', 'Transferee'),
        ('Returnee', 'Returnee'),
        ('Shiftee', 'Shiftee'),
        ('Cross Enrollee', 'Cross Enrollee'),
    )
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=100, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    major = models.CharField(max_length=100, blank=True, null=True)
    year_level = models.ForeignKey(YearLevel, on_delete=models.CASCADE)
    school_year = models.CharField(max_length=100, blank=True, null=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    enrollment_status = models.ForeignKey(
        EnrollmentStatus, on_delete=models.CASCADE)
    student_status = models.CharField(
        max_length=50, blank=True, null=True, choices=Student_Status)
    block_section = models.CharField(max_length=100, blank=True, null=True)
