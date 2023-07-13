from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib import messages
from django.core.mail import send_mail


from django.core.files.storage import FileSystemStorage
from django.conf.urls.static import static
from django.conf import settings

import mysql.connector as mcdb
conn = mcdb.connect(host="localhost", user="root", passwd="", database='coachingdb')
print('Successfully connected to database')
cur = conn.cursor()

# Create your views here.
def index(request):
    return render (request,'adminpages/index.html')


def table_admin(request):
    cur.execute("SELECT * FROM `tbl_admin`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request, 'adminpages/table_admin.html', {'mydata': data})   

def table_admin_deleteprocess(request,id):
    #id=request.Get['id']
    #id=User.object.get(id=id)
    print(id)
    messages.add_message(request,messages.SUCCESS,'Record Deleted')
    cur.execute("delete from `tbl_admin` where `admin_id` = {}".format(id))
    conn.commit()
    return redirect(table_admin)

def table_admin_editprocess(request,id):
    print("Edit id is",id)
    cur.execute("select * from `tbl_admin` where `admin_id` = {}".format(id))
    data=cur.fetchone()
    print(list(data))
    return render(request,'edit.html',{'mydata':data})

    

def table_admission(request):
    cur.execute('''SELECT
    `tbl_admission`.`admission_id`
    , `tbl_student`.`student_name`
    , `tbl_admission`.`admission_date`
    , `tbl_standerd`.`standerd_name`
    , `tbl_admission`.`admission_fees`
FROM
    `coachingdb`.`tbl_admission`
    INNER JOIN `coachingdb`.`tbl_student` 
        ON (`tbl_admission`.`student_id` = `tbl_student`.`student_id`)
    INNER JOIN `coachingdb`.`tbl_standerd` 
        ON (`tbl_admission`.`standerd_id` = `tbl_standerd`.`standerd_id`);''')
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request, 'adminpages/table_admission.html', {'mydata': data})  

def table_admission_deleteprocess(request,id):
    #id=request.Get['id']
    #id=User.object.get(id=id)
    print(id)
    messages.add_message(request,messages.SUCCESS,'Record Deleted')
    cur.execute("delete from `tbl_admission` where `admission_id` = {}".format(id))
    conn.commit()
    return redirect(table_admission)

def table_admission_editprocess(request,id):
    print("Edit id is:",id)
    messages.add_message(request,messages.SUCCESS,'Record Edit')
    cur.execute("select * from `tbl_admission` where `admission_id` = {}".format(id))
    data=cur.fetchone()
    print(list(data))    
    return render(request,'adminpages/table_admission_editprocess.html',{"mydata":data})


def updatedata(request):
    if request.method == 'POST':
        print(request.POST)
        txt1=request.POST['txt1']
        txt2=request.POST['txt2']
        txt3=request.POST['txt3']
        txt4=request.POST['txt4']
        messages.add_message(request,messages.SUCCESS,'Successfully Updated Data')
        cur.execute("update `tbl_admission` set `admission_fees`='{}',`standerd_id` = '{}',`student_id` = '{}' where `admission_id`='{}'".format(txt4,txt3,txt2,txt1))
        conn.commit()
        return redirect(table_admission)
    else:
        return redirect(table_admission)




def table_attendance(request):
    cur.execute('''SELECT
    `tbl_attendance`.`attendance_id`
    , `tbl_standerd`.`standerd_name`
    , `tbl_student`.`student_name`
    , `tbl_attendance`.`attendance_date`
    , `tbl_attendance`.`attendance_ispresent`
FROM
    `coachingdb`.`tbl_student`
    INNER JOIN `coachingdb`.`tbl_attendance` 
        ON (`tbl_student`.`student_id` = `tbl_attendance`.`student_id`)
    INNER JOIN `coachingdb`.`tbl_standerd` 
        ON (`tbl_standerd`.`standerd_id` = `tbl_attendance`.`standerd_id`);''')
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request, 'adminpages/table_attendance.html', {'mydata': data}) 

def table_attendance_deleteprocess(request,id):
    #id=request.Get['id']
    #id=User.object.get(id=id)
    print(id)
    messages.add_message(request,messages.SUCCESS,'Record Deleted')
    cur.execute("delete from `tbl_attendance` where `attendance_id` = {}".format(id))
    conn.commit()
    return redirect(table_attendance)




def table_chapter(request):
    cur.execute('''SELECT
    `tbl_chapter`.`chapter_id`
    , `tbl_chapter`.`chapter_name`
    , `tbl_chapter`.`chapter_weightage`
    , `tbl_standerd`.`standerd_name`
    , `tbl_subject`.`subject_name`
FROM
    `coachingdb`.`tbl_standerd`
    INNER JOIN `coachingdb`.`tbl_chapter` 
        ON (`tbl_standerd`.`standerd_id` = `tbl_chapter`.`standerd_id`)
    INNER JOIN `coachingdb`.`tbl_subject` 
        ON (`tbl_subject`.`subject_id` = `tbl_chapter`.`subject_id`);''')
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request, 'adminpages/table_chapter.html', {'mydata': data})  

def table_chapter_deleteprocess(request,id):
    #id=request.Get['id']
    #id=User.object.get(id=id)
    print(id)
    messages.add_message(request,messages.SUCCESS,'Record Deleted')
    cur.execute("delete from `tbl_chapter` where `chapter_id` = {}".format(id))
    conn.commit()
    return redirect(table_chapter)



def table_exam(request):
    cur.execute('''SELECT
    `tbl_exam`.`exam_id`
    , `tbl_exammaster`.`examMaster_name`
    , `tbl_exam`.`exam_date`
    , `tbl_exammaster`.`examMaster_mark`
    , `tbl_standerd`.`standerd_name`
    , `tbl_subject`.`subject_name`
FROM
    `coachingdb`.`tbl_exam`
    INNER JOIN `coachingdb`.`tbl_standerd` 
        ON (`tbl_exam`.`standerd_id` = `tbl_standerd`.`standerd_id`)
    INNER JOIN `coachingdb`.`tbl_subject` 
        ON (`tbl_exam`.`subject_id` = `tbl_subject`.`subject_id`)
    INNER JOIN `coachingdb`.`tbl_exammaster` 
        ON (`tbl_exam`.`examMaster_name` = `tbl_exammaster`.`examMaster_id`);''')
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request, 'adminpages/table_exam.html', {'mydata': data})   

def table_exam_deleteprocess(request,id):
    #id=request.Get['id']
    #id=User.object.get(id=id)
    print(id)
    messages.add_message(request,messages.SUCCESS,'Record Deleted')
    cur.execute("delete from `tbl_exam` where `exam_id` = {}".format(id))
    conn.commit()
    return redirect(table_exam)


def table_examMaster(request):
    cur.execute("SELECT * FROM `tbl_examMaster`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request, 'adminpages/table_examMaster.html', {'mydata': data}) 

def table_examMaster_deleteprocess(request,id):
    #id=request.Get['id']
    #id=User.object.get(id=id)
    print(id)
    messages.add_message(request,messages.SUCCESS,'Record Deleted')
    cur.execute("delete from `tbl_examMaster` where `examMaster_id` = {}".format(id))
    conn.commit()
    return redirect(table_examMaster)




def table_fees(request):
    cur.execute('''SELECT
    `tbl_fees`.`fees_id`
    , `tbl_fees`.`fees_date`
    , `tbl_fees`.`fees_amount`
    , `tbl_fees`.`fees_method`
    , `tbl_admission`.`admission_fees`
    , `tbl_student`.`student_name`
    , `tbl_standerd`.`standerd_name`
    , `tbl_fees`.`fees_dueamount`
    , `tbl_fees`.`fees_paidamount`
    , `tbl_fees`.`fees_dueamount` - `tbl_fees`.`fees_paidamount` as dueamount
FROM
    `coachingdb`.`tbl_admission`
    INNER JOIN `coachingdb`.`tbl_fees` 
        ON (`tbl_admission`.`admission_id` = `tbl_fees`.`admission_id`)
    INNER JOIN `coachingdb`.`tbl_standerd` 
        ON (`tbl_standerd`.`standerd_id` = `tbl_fees`.`standerd_id`)
    INNER JOIN `coachingdb`.`tbl_student` 
        ON (`tbl_student`.`student_id` = `tbl_fees`.`student_id`);''')
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request, 'adminpages/table_fees.html', {'mydata': data})   

def table_fees_deleteprocess(request,id):
    #id=request.Get['id']
    #id=User.object.get(id=id)
    print(id)
    messages.add_message(request,messages.SUCCESS,'Record Deleted')
    cur.execute("delete from `tbl_fees` where `fees_id` = {}".format(id))
    conn.commit()
    return redirect(table_fees)



def table_reportcard(request):
    cur.execute('''SELECT
    `tbl_reportcard`.`reportcard_id`
    , `tbl_student`.`student_name`
    , `tbl_attendance`.`attendance_ispresent`
    , `tbl_exam`.`exam_mark`
    , `tbl_reportcard`.`obtained_mark`
    , `tbl_reportcard`.`reportcard_details`
FROM
    `coachingdb`.`tbl_student`
    INNER JOIN `coachingdb`.`tbl_reportcard` 
        ON (`tbl_student`.`student_id` = `tbl_reportcard`.`student_id`)
    INNER JOIN `coachingdb`.`tbl_attendance` 
        ON (`tbl_attendance`.`attendance_id` = `tbl_reportcard`.`attendance_id`)
    INNER JOIN `coachingdb`.`tbl_exam` 
        ON (`tbl_exam`.`exam_id` = `tbl_reportcard`.`exam_id`);''')
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request, 'adminpages/table_reportcard.html', {'mydata': data})  

def table_reportcard_deleteprocess(request,id):
    #id=request.Get['id']
    #id=User.object.get(id=id)
    print(id)
    messages.add_message(request,messages.SUCCESS,'Record Deleted')
    cur.execute("delete from `tbl_reportcard` where `reportcard_id` = {}".format(id))
    conn.commit()
    return redirect(table_reportcard)

    

def table_standerd(request):
    cur.execute("SELECT * FROM `tbl_standerd`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request, 'adminpages/table_standerd.html', {'mydata': data}) 

def table_standerd_deleteprocess(request,id):
    #id=request.Get['id']
    #id=User.object.get(id=id)
    print(id)
    messages.add_message(request,messages.SUCCESS,'Record Deleted')
    cur.execute("delete from `tbl_standerd` where `standerd_id` = {}".format(id))
    conn.commit()
    return redirect(table_standerd)

        

def table_student(request):
    cur.execute("SELECT * FROM `tbl_student`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request, 'adminpages/table_student.html', {'mydata': data}) 

def table_student_deleteprocess(request,id):
    #id=request.Get['id']
    #id=User.object.get(id=id)
    print(id)
    messages.add_message(request,messages.SUCCESS,'Record Deleted')
    cur.execute("delete from `tbl_student` where `student_id` = {}".format(id))
    conn.commit()
    return redirect(table_student)

        

def table_subject(request):
    cur.execute("SELECT * FROM `tbl_subject`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request, 'adminpages/table_subject.html', {'mydata': data}) 

def table_subject_deleteprocess(request,id):
    #id=request.Get['id']
    #id=User.object.get(id=id)
    print(id)
    messages.add_message(request,messages.SUCCESS,'Record Deleted')
    cur.execute("delete from `tbl_subject` where `subject_id` = {}".format(id))
    conn.commit()
    return redirect(table_subject)

        

def table_teacher(request):
    cur.execute("SELECT * FROM `tbl_teacher`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request, 'adminpages/table_teacher.html', {'mydata': data}) 

def table_teacher_deleteprocess(request,id):
    #id=request.Get['id']
    #id=User.object.get(id=id)
    print(id)
    messages.add_message(request,messages.SUCCESS,'Record Deleted')
    cur.execute("delete from `tbl_teacher` where `teacher_id` = {}".format(id))
    conn.commit()
    return redirect(table_teacher)



def table_timetable(request):
    cur.execute('''SELECT
    `tbl_timetable`.`table_id`
    , `tbl_standerd`.`standerd_name`
    , `tbl_timetable`.`table_time`
    , `tbl_timetable`.`table_day`
    , `tbl_subject`.`subject_name`
FROM
    `coachingdb`.`tbl_timetable`
    INNER JOIN `coachingdb`.`tbl_standerd` 
        ON (`tbl_timetable`.`standerd_id` = `tbl_standerd`.`standerd_id`)
    INNER JOIN `coachingdb`.`tbl_subject` 
        ON (`tbl_timetable`.`subject_id` = `tbl_subject`.`subject_id`);''')
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request, 'adminpages/table_timetable.html', {'mydata': data})  

def table_timetable_deleteprocess(request,id):
    #id=request.Get['id']
    #id=User.object.get(id=id)
    print(id)
    messages.add_message(request,messages.SUCCESS,'Record Deleted')
    cur.execute("delete from `tbl_timetable` where `table_id` = {}".format(id))
    conn.commit()
    return redirect(table_timetable)



def form_admin(request):
    return render (request,'adminpages/form_admin.html')

def form_admin_addprocess(request):
    if request.method == 'POST':
        print(request.POST)
        aname = request.POST['txt2']
        aemail = request.POST['txt3']
        apassword = request.POST['txt4']
         
        messages.add_message(request,messages.SUCCESS,'form submited')

        cur.execute("INSERT INTO `tbl_admin`(`admin_name`,`admin_email`,`admin_password`) VALUES ('{}','{}','{}')".format(aname,aemail,apassword))
        conn.commit()
        return redirect(form_admin) 
    else:
        return redirect(form_admin)
        
def form_teacher(request):
    return render (request,'adminpages/form_teacher.html')

def form_teacher_addprocess(request):
    if request.method == 'POST':
        print(request.POST)
        tname = request.POST['txt2']
        tgender= request.POST['txt3']
        temail = request.POST['txt4']
        tpassword = request.POST['txt5']
        tmono = request.POST['txt6']
        taddress = request.POST['txt7']
        tquli = request.POST['txt8']

        #Get File Value
        myfile = request.FILES['txt9']
        fs = FileSystemStorage()
        myfileupload = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(myfileupload)
        print("URL: " + uploaded_file_url)

        messages.add_message(request,messages.SUCCESS,'form submited')
    

        cur.execute("INSERT INTO `tbl_teacher`(`teacher_name`,`teacher_gender`,`teacher_email`,`teacher_password`,`teacher_mobileno`,`teacher_address`,`teacher_qulification`,`teacher_img`) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(tname,tgender,temail,tpassword,tmono,taddress,tquli,myfile))
        conn.commit()
        return redirect(form_teacher) 
    else:
        return redirect(form_teacher)


def form_student(request):
    return render (request,'adminpages/form_student.html')

def form_student_addprocess(request):
    if request.method == 'POST':
        print(request.POST)
        sname = request.POST['txt2']
        sgender= request.POST['txt3'] 
        sdob = request.POST['txt4']
        semail = request.POST['txt5']
        spassword = request.POST['txt6']
        smono = request.POST['txt7']
        spano = request.POST['txt8']
        saddress = request.POST['txt9']

        #Get File Value
        myfile = request.FILES['txt10']
        fs = FileSystemStorage()
        myfileupload = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(myfileupload)
        print("URL: " + uploaded_file_url)

        messages.add_message(request,messages.SUCCESS,'form submited')

        cur.execute("INSERT INTO `tbl_student`(`student_name`,`student_gender`,`student_D_O_B`,`student_email`,`student_password`,`student_mobileno`,`student_parentnno`,`student_address`,`student_img`) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(sname,sgender,sdob,semail,spassword,smono,spano,saddress,myfile))
        conn.commit()
        return redirect(form_student) 
    else:
        return redirect(form_student)
        

def form_standerd(request):
    return render (request,'adminpages/form_standerd.html')



def form_standerd_addprocess(request):
    if request.method == 'POST':
        print(request.POST)
        stdname = request.POST['txt2']

        messages.add_message(request,messages.SUCCESS,'form submited')

        cur.execute("INSERT INTO `tbl_standerd`(`standerd_name`) VALUES ('{}')".format(stdname))
        conn.commit()
        return redirect(form_standerd) 
    else:
        return redirect(form_standerd)


def form_subject(request):
    return render (request,'adminpages/form_subject.html')

def form_subject(request):
    cur.execute("SELECT * FROM `tbl_standerd`")
    data=cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'adminpages/form_subject.html',{'mydata':data})


def form_subject_addprocess(request):
    if request.method == 'POST':
        print(request.POST)
        subname = request.POST['txt2']

        messages.add_message(request,messages.SUCCESS,'form submited')
        
        cur.execute("INSERT INTO `tbl_subject`(`subject_name`) VALUES ('{}')".format(subname))
        conn.commit()
        return redirect(form_subject) 
    else:
        return redirect(form_subject)


def form_admission(request):
    return render (request,'adminpages/form_admission.html')

def form_admission(request):
    cur.execute("SELECT * FROM `tbl_student`")
    data=cur.fetchall()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `tbl_standerd`")
    data1=cur.fetchall()
    #return list(data)
    print(list(data1))
    return render(request,'adminpages/form_admission.html', {'mydata':data,'mydata1':data1})



def form_admission_addprocess(request):
    if request.method == 'POST':
        print(request.POST)
        admdate = request.POST['txt2']
        sid = request.POST['txt3']
        stdid = request.POST['txt4']
        admfees = request.POST['txt5']

        messages.add_message(request,messages.SUCCESS,'form submited')

        cur.execute("INSERT INTO `tbl_admission`(`student_id`,`admission_date`,`standerd_id`,`admission_fees`) VALUES ('{}','{}','{}','{}')".format(admdate,sid,stdid,admfees))
        conn.commit()
        return redirect(form_admission) 
    else:
        return redirect(form_admission)


def form_chapter(request):
    return render (request,'adminpages/form_chapter.html')

def form_chapter(request):
    cur.execute("SELECT * FROM `tbl_standerd`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `tbl_subject`")
    data1=cur.fetchall()
    #return list(data)
    print(list(data1))
    return render(request,'adminpages/form_chapter.html',{'mydata':data,'mydata1':data1})



def form_chapter_addprocess(request):
    if request.method == 'POST':
        print(request.POST)
        chname= request.POST['txt2']
        chweghtage = request.POST['txt3']
        stdid = request.POST['txt4']
        subid = request.POST['txt5']

        messages.add_message(request,messages.SUCCESS,'form submited')

        cur.execute("INSERT INTO `tbl_chapter`(`chapter_name`,`chapter_weightage`,`standerd_id`,`subject_id`) VALUES ('{}','{}','{}','{}')".format(chname,chweghtage,stdid,subid))
        conn.commit()
        return redirect(form_chapter) 
    else:
        return redirect(form_chapter)


def form_exam(request):
    return render (request,'adminpages/form_exam.html')

def form_exam(request):
    cur.execute("SELECT * FROM `tbl_examMaster`")
    data3=cur.fetchall()
    #return list(data3)
    print(list(data3))
    cur.execute("SELECT * FROM `tbl_standerd`")
    data=cur.fetchall()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `tbl_subject`")
    data1=cur.fetchall()
    #return list(data)
    print(list(data1))
    cur.execute("SELECT * FROM `tbl_examMaster`")
    data2=cur.fetchall()
    #return list(data)
    print(list(data2))
    return render(request,'adminpages/form_exam.html',{'mydata3':data3,'mydata':data,'mydata1':data1,'mydata2':data2})



def form_exam_addprocess(request):
    if request.method == 'POST':
        print(request.POST)
        exname= request.POST['txt3']
        exdate= request.POST['txt4']    
        totalmark = request.POST['txt5']
        stdid = request.POST['txt6']
        subid = request.POST['txt7']

        messages.add_message(request,messages.SUCCESS,'form submited')


        cur.execute("INSERT INTO `tbl_exam`(`examMaster_name`,`exam_date`,`exam_mark`,`standerd_id`,`subject_id`) VALUES ('{}','{}','{}','{}','{}')".format(exname,exdate,totalmark,stdid,subid))
        conn.commit()
        return redirect(form_exam) 
    else:
        return redirect(form_exam)

def form_examMaster(request):
    return render (request,'adminpages/form_examMaster.html')

def form_examMaster_addprocess(request):
    if request.method == 'POST':
        print(request.POST)
        exmname= request.POST['txt3']
        exmmark= request.POST['txt4']    
        
        messages.add_message(request,messages.SUCCESS,'form submited')


        cur.execute("INSERT INTO `tbl_examMaster`(`examMaster_name`,`examMaster_mark`) VALUES ('{}','{}')".format(exmname,exmmark))
        conn.commit()
        return redirect(form_examMaster) 
    else:
        return redirect(form_examMaster)





def form_attendance(request):
    return render (request,'adminpages/form_attendance.html')

def form_attendance(request):
    cur.execute("SELECT * FROM `tbl_standerd`")
    data=cur.fetchall()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `tbl_student`")
    data1=cur.fetchall()
    #return list(data)
    print(list(data1))
    return render(request,'adminpages/form_attendance.html',{'mydata':data,'mydata1':data1})


def form_attendance_addprocess(request):
    if request.method == 'POST':
        print(request.POST)
        stdid = request.POST['txt2']
        sid = request.POST['txt3']
        atddate = request.POST['txt4']
        atdispre = request.POST['txt5']

        messages.add_message(request,messages.SUCCESS,'attendance approving')

        cur.execute("INSERT INTO `tbl_attendance`(`standerd_id`,`student_id`,`attendance_date`,`attendance_ispresent`) VALUES ('{}','{}','{}','{}')".format(stdid,sid,atddate,atdispre))
        conn.commit()
        return redirect(form_attendance) 
    else:
        return redirect(form_attendance)


def form_fees(request):
    return render (request,'adminpages/form_fees.html')

def form_fees(request):
    cur.execute("SELECT * FROM `tbl_admission`")
    data=cur.fetchall()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `tbl_student`")
    data1=cur.fetchall()
    #return list(data)
    print(list(data1))
    cur.execute("SELECT * FROM `tbl_standerd`")
    data2=cur.fetchall()
    #return list(data)
    print(list(data2))
    return render(request,'adminpages/form_fees.html',{'mydata':data,'mydata1':data1,'mydata2':data2})


def form_fees_addprocess(request):
    if request.method == 'POST':
        print(request.POST)
        fdate = request.POST['txt2']
        famount= request.POST['txt3']
        fmethod = request.POST['txt4']
        studid = request.POST['txt5']
        stdid = request.POST['txt5']
        admid = request.POST['txt5']
        fdueamount = request.POST['txt6']
        fpaidamount = request.POST['txt7'] 

        messages.add_message(request,messages.SUCCESS,'form submited')
   
        cur.execute("INSERT INTO `tbl_fees`(`fees_date`,`fees_amount`,`fees_method`,`admission_id`,`student_id`,`standerd_id`,`fees_dueamount`,`fees_paidamount`) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(fdate,famount,fmethod,admid,studid,stdid,fdueamount,fpaidamount))
        conn.commit()
        return redirect(form_fees) 
    else:
        return redirect(form_fees)


def form_reportcard(request):
    return render (request,'adminpages/form_reportcard.html')

def form_reportcard(request):
    cur.execute("SELECT * FROM `tbl_student`")
    data=cur.fetchall()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `tbl_attendance`")
    data1=cur.fetchall()
    #return list(data)
    print(list(data1))
    cur.execute("SELECT * FROM `tbl_exam`")
    data2=cur.fetchall()
    #return list(data)
    print(list(data2))
    return render(request,'adminpages/form_reportcard.html',{'mydata':data,'mydata1':data1,'mydata2':data2})


def form_reportcard_addprocess(request):
    if request.method == 'POST':
        print(request.POST)
        sid = request.POST['txt2']
        atdid = request.POST['txt3']
        exid = request.POST['txt4']
        omark = request.POST['txt5']
        repodetail = request.POST['txt6']

        messages.add_message(request,messages.SUCCESS,'form submited')

        cur.execute("INSERT INTO `tbl_reportcard`(`student_id`,`attendance_id`,`exam_id`,`obtained_mark`,`reportcard_details`) VALUES ('{}','{}','{}','{}','{}')".format(sid,atdid,exid,omark,repodetail))
        conn.commit()
        return redirect(form_reportcard) 
    else:
        return redirect(form_reportcard)

def form_timetable(request):
    return render (request,'adminpages/form_timetable.html')

def form_timetable(request):
    cur.execute("SELECT * FROM `tbl_subject`")
    data=cur.fetchall()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `tbl_standerd`")
    data1=cur.fetchall()
    #return list(data)
    print(list(data1))
    return render(request,'adminpages/form_timetable.html',{'mydata':data,'mydata1':data1})


def form_timetable_addprocess(request):
    if request.method == 'POST':
        print(request.POST)
        sid = request.POST['txt2']
        tt = request.POST['txt3']
        tday = request.POST['txt4']
        subid = request.POST['txt5']

        messages.add_message(request,messages.SUCCESS,'form submited')

        cur.execute("INSERT INTO `tbl_timetable`(`standerd_id`,`table_time`,`table_day`,`subject_id`) VALUES ('{}','{}','{}','{}')".format(sid,tt,tday,subid))
        conn.commit()
        return redirect(form_timetable) 
    else:
        return redirect(form_timetable)

def signup(request):
    return render(request,'adminpages/signup.html')

def signup_addprocess(request):
    if request.method == 'POST':
        print(request.POST)
        aname = request.POST['txt1']
        aemail = request.POST['txt2']
        apass = request.POST['txt3']

        messages.add_message(request,messages.SUCCESS,'form submited')

        cur.execute("INSERT INTO `tbl_admin`(`admin_name`,`admin_email`,`admin_password`) VALUES ('{}','{}','{}')".format(aname,aemail,apass))
        conn.commit()
        return redirect(signup) 
    else:
        return redirect(signup)


def forgotpassword(request):
    return render(request,'adminpages/forgotpassword.html')

def forgotpasswordprocess(request):
    print(request.POST)
    admin_email = request.POST['txt1']
    cur.execute("select * from `tbl_admin` where `admin_email` = '{}' ".format(admin_email))
    db_data = cur.fetchone()
        
    if db_data is not None:
        if len(db_data) > 0:
            #Fetch Data
            admin_db_id = db_data[0]
            admin_db_email = db_data[2]
            admin_db_password = db_data[3]
            print(admin_db_id)
            print(admin_db_email)
            
            subject = 'Forgot Password'
            message = ' Your Password is  ' + admin_db_password
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [admin_db_email,]
            send_mail( subject, message, email_from, recipient_list )
            messages.success(request, 'Password Sent on Email ID')
            return redirect(login)
            #Cookie Code
        else:
            messages.success(request, 'Wrong Email Details')
            return render(request, 'adminpages/forgotpassword.html') 
    messages.success(request, 'Wrong Email Details')
    return render(request, 'adminpages/forgotpassword.html')


def changepassword(request):
    return render(request,'adminpages/changepassword.html')

def changepasswordprocess(request):
    if 'admin_id' in request.COOKIES and request.session.has_key('admin_id'):
        admin_id = request.session['admin_id']
        opass = request.POST['opass']
        npass = request.POST['npass']
        cpass = request.POST['cpass']
        #Fetch Old Password from DB
        cur.execute("select * from `tbl_admin` where `admin_id` = {}".format(admin_id))
        db_data = cur.fetchone()
        if db_data is not None:
            if len(db_data) > 0:
                #Compare Old Password with DB Old Password
                oldpassword_db = db_data[3]
                if opass == oldpassword_db:
                    #Compare New and Confirm Password
                    if npass != cpass:
                        messages.success(request, 'New and Confirm Password Not Matched ')
                        return render(request, 'adminpages/changepassword.html')
                    else:
                        cur.execute("update  `tbl_admin` set `admin_password` = {} where `admin_id`={}".format(npass,admin_id))
                        conn.commit()
                        messages.success(request, 'Password Changed successfully')
                        return render(request, 'adminpages/changepassword.html')
                else:
                    messages.success(request, 'Old Password Not Matched ')
                    return render(request, 'adminpages/changepassword.html')
            else:
                redirect(login) 
        else: 
            redirect(login) 
    else:
        return redirect(login)  

def login(request):
    return render(request,'adminpages/login.html')

def loginpageprocess(request):
    admin_email = request.POST['txt1']
    admin_pass = request.POST['txt2']
    cur.execute("select * from `tbl_admin` where `admin_email` = '{}' and `admin_password` = '{}'".format(admin_email,admin_pass))
    data = cur.fetchone()
    if data is not None:
        if len(data) > 0:
            #Fetch Data
            admin_db_id = data[0]#fatch id of user
            admin_db_email = data[1]#fatch email of user
            print(admin_db_id)
            print(admin_db_email)
            #store user information in Session
            request.session['admin_id'] = admin_db_id
            request.session['admin_email'] = admin_db_email
            #store user information in cookie
            response = redirect(index)
            response.set_cookie('admin_id', admin_db_id)
            response.set_cookie('admin_email', admin_db_email)
            return response
            #Cookie Code
        else:
                messages.success(request,'Log in Failed!')
                return render(request, 'userpages/login.html')
    messages.success(request,'Login Failed!')     
    return render(request, 'adminpages/login.html')

def userlogout(request):
    del request.session['admin_email']    
    del request.session['admin_id'] 
    response=redirect(login)
    response.delete_cookie('admin_id')   
    response.delete_cookie('admin_email')   
    return response

