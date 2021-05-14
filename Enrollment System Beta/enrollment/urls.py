from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # User URL...
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    # New Student URL...
    path('new-student/dashboard/', views.newStudentPage, name="newStudentPage"),
    path('new-student/update-information/<str:pk>/',
         views.newStudentUpdateInfo, name='newStudentUpdateInfo'),
    path('new-student/display-information/', views.displayNewStudentInfo,
         name="displayNewStudentInfo"),
    path('new-student/profile/', views.newStudentProfile, name="newStudentProfile"),

    # BSIT Student URL...
    path('bsit-student/dashboard/', views.bsitStudentPage, name="bsitStudentPage"),
    path('bsit-student/update-information/<str:pk>/',
         views.bsitStudentUpdateInfo, name='bsitStudentUpdateInfo'),
    path('bsit-student/display-information/', views.displayBsitStudentInfo,
         name="displayBsitStudentInfo"),
    path('bsit-student/profile/', views.bsitStudentProfile,
         name="bsitStudentProfile"),

    # BIT Student URL...
    path('bit-student/dashboard/', views.bitStudentPage, name="bitStudentPage"),
    path('bit-student/update-information/<str:pk>/',
         views.bitStudentUpdateInfo, name='bitStudentUpdateInfo'),
    path('bit-student/display-information/', views.displayBitStudentInfo,
         name="displayBitStudentInfo"),
    path('bit-student/profile/', views.bitStudentProfile, name="bitStudentProfile"),

    # Faculty URL...
    path('faculty/', views.facultyPage, name="faculty"),

    # Student Subject Form
    path('subject-form-1/', views.studentSubjectForm1,
         name="studentSubjectForm1"),
    path('subject-form-2/',
         views.studentSubjectForm2, name="studentSubjectForm2"),
    path('ajax/load-year_levels/', views.load_year_levels,
         name='ajax_load_year_levels'),
    path('ajax/load-semesters/', views.load_semesters, name='ajax_load_semesters'),
    path('ajax/load-enrollment_statuses/', views.load_enrollment_statuses,
         name='ajax_load_enrollment_statuses'),

    # User Password Reset
    path('reset_password/',
         auth_views.PasswordResetView.as_view(
             template_name="enrollment/user/password/password_reset.html"),
         name="reset_password"),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(
             template_name="enrollment/user/password/password_reset_sent.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name="enrollment/user/password/password_reset_form.html"),
         name="password_reset_confirm"),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name="enrollment/user/password/password_reset_done.html"),
         name="password_reset_complete"),

]
