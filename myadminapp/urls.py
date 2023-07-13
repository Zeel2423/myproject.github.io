from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    
    #path('tables',views.tables,name='tables'),
    path('table_admin',views.table_admin,name='table_admin'),
    path('table_admin_deleteprocess/<int:id>',views.table_admin_deleteprocess,name='table_admin'),
    path('table_admin_editprocess/<int:id>',views.table_admin_editprocess,name='table_admin'),

    path('table_admission',views.table_admission,name='table_admission'),
    path('table_admission_deleteprocess/<int:id>',views.table_admission_deleteprocess,name='table_admission'),
    path('table_admission_editprocess/<int:id>',views.table_admission_editprocess,name='table_admission'),
    path('updatedata',views.updatedata,name='table_admission'),

    path('table_attendance',views.table_attendance,name='table_attendance'),
    path('table_attendance_deleteprocess/<int:id>',views.table_attendance_deleteprocess,name='table_attendance'),

    path('table_chapter',views.table_chapter,name='table_chapter'),
    path('table_chapter_deleteprocess/<int:id>',views.table_chapter_deleteprocess,name='table_chapter'),

    path('table_exam',views.table_exam,name='table_exam'),
    path('table_exam_deleteprocess/<int:id>',views.table_exam_deleteprocess,name='table_exam'),

    path('table_examMaster',views.table_examMaster,name='table_examMaster'),
    path('table_examMaster_deleteprocess/<int:id>',views.table_examMaster_deleteprocess,name='table_examMaster'),


    path('table_fees',views.table_fees,name='table_fees'),
    path('table_fees_deleteprocess/<int:id>',views.table_fees_deleteprocess,name='table_fees'),

    path('table_reportcard',views.table_reportcard,name='table_reportcard'),
    path('table_reportcard_deleteprocess/<int:id>',views.table_reportcard_deleteprocess,name='table_reportcard'),

    path('table_standerd',views.table_standerd,name='table_standerd'),
    path('table_standerd_deleteprocess/<int:id>',views.table_standerd_deleteprocess,name='table_standerd'),

    path('table_student',views.table_student,name='table_student'),
    path('table_student_deleteprocess/<int:id>',views.table_student_deleteprocess,name='table_student'),

    path('table_subject',views.table_subject,name='table_subject'),
    path('table_subject_deleteprocess/<int:id>',views.table_subject_deleteprocess,name='table_subject'),

    path('table_teacher',views.table_teacher,name='table_teacher'),
    path('table_teacher_deleteprocess/<int:id>',views.table_teacher_deleteprocess,name='table_teacher'),

    path('table_timetable',views.table_timetable,name='table_timetable'),
    path('table_timetable_deleteprocess/<int:id>',views.table_timetable_deleteprocess,name='table_timetable'),



    path('form_admin',views.form_admin,name='form_admin'),
    path('form_admin_addprocess',views.form_admin_addprocess,name='form_admin_addprocess'),

    path('form_teacher',views.form_teacher,name='form_teacher'),
    path('form_teacher_addprocess',views.form_teacher_addprocess,name='form_teacher_addprocess'),

    path('form_student',views.form_student,name='form_student'),
    path('form_student_addprocess',views.form_student_addprocess,name='form_student_addprocess'),


    path('form_standerd',views.form_standerd,name='form_standerd'),
    path('form_standerd_addprocess',views.form_standerd_addprocess,name='form_standerd_addprocess'),
    
    path('form_subject',views.form_subject,name='form_subject'),
    path('form_subject_addprocess',views.form_subject_addprocess,name='form_subject_addprocess'),
    
    path('form_admission',views.form_admission,name='form_admission'),
    path('form_admission_addprocess',views.form_admission_addprocess,name='form_admission_addprocess'),

    path('form_chapter',views.form_chapter,name='form_chapter'),
    path('form_chapter_addprocess',views.form_chapter_addprocess,name='form_chapter_addprocess'),

    path('form_exam',views.form_exam,name='form_exam'),
    path('form_exam_addprocess',views.form_exam_addprocess,name='form_exam_addprocess'),

    path('form_examMaster',views.form_examMaster,name='form_examMaster'),
    path('form_examMaster_addprocess',views.form_examMaster_addprocess,name='form_examMaster_addprocess'),
    

    path('form_timetable',views.form_timetable,name='form_timetable'),
    path('form_timetable_addprocess',views.form_timetable_addprocess,name='form_timetable_addprocess'),

    path('form_attendance',views.form_attendance,name='form_attendance'),
    path('form_attendance_addprocess',views.form_attendance_addprocess,name='form_attendance_addprocess'),

    path('form_fees',views.form_fees,name='form_fees'),
    path('form_fees_addprocess',views.form_fees_addprocess,name='form_fees_addprocess'),

    path('form_reportcard',views.form_reportcard,name='form_reportcard'),
    path('form_reportcard_addprocess',views.form_reportcard_addprocess,name='form_reportcard_addprocess'),

    path('login',views.login,name='login'),
    path('loginpageprocess',views.loginpageprocess,name='loginpageprocess'),
    path('userlogout',views.userlogout,name='userlogout'),

    path('signup',views.signup,name='signup'),
    path('signup_addprocess',views.signup_addprocess,name='signup_addprocess'),

    path('forgotpassword',views.forgotpassword,name='forgotpassword'),
    path('forgotpasswordprocess',views.forgotpasswordprocess,name='forgotpasswordprocess'),

    path('changepassword',views.changepassword,name='changepassword'),
    path('changepasswordprocess',views.changepasswordprocess,name='changepasswordprocess'),

    

]