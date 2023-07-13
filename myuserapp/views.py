from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib import messages

from django.core.files.storage import FileSystemStorage
from django.conf.urls.static import static

from django.core.mail import send_mail
from django.conf import settings
import mysql.connector as mcdb
conn = mcdb.connect(host="localhost", user="root", passwd="", database='coachingdb')
print('Successfully connected to database')
cur = conn.cursor()


# Create your views here.

def home(request):
    return render(request,'userpages/home.html')

def about(request):
    return render(request,'userpages/about.html')
def contact(request):
    return render(request,'userpages/contact.html')
  
def pricing(request):
    return render(request,'userpages/pricing.html')

def changepassword(request):
    return render(request,'userpages/changepassword.html')

def changepasswordprocess(request):
    if 'user_id' in request.COOKIES and request.session.has_key('user_id'):
        user_id = request.session['user_id']
        opass = request.POST['opass']
        npass = request.POST['npass']
        cpass = request.POST['cpass']
        #Fetch Old Password from DB
        cur.execute("select * from `tbl_student` where `student_id` = {}".format(user_id))
        db_data = cur.fetchone()
        if db_data is not None:
            if len(db_data) > 0:
                #Compare Old Password with DB Old Password
                oldpassword_db = db_data[5]
                if opass == oldpassword_db:
                    #Compare New and Confirm Password
                    if npass != cpass:
                        messages.success(request, 'New and Confirm Password Not Matched ')
                        return render(request, 'userpages/changepassword.html')
                    else:
                        cur.execute("update  `tbl_student` set `student_password` = {} where `student_id`={}".format(npass,user_id))
                        conn.commit()
                        messages.success(request, 'Password Changed successfully')
                        return render(request, 'userpages/changepassword.html')
                else:
                    messages.success(request, 'Old Password Not Matched ')
                    return render(request, 'userpages/changepassword.html')
            else:
                redirect(login) 
        else: 
            redirect(login) 
    else:
        return redirect(login)  

def forgotpassword(request):
    return render(request,'userpages/forgotpassword.html')

def forgotpasswordprocess(request):
    print(request.POST)
    admin_email = request.POST['txt1']
    cur.execute("select * from `tbl_student` where `student_email` = '{}' ".format(admin_email))
    db_data = cur.fetchone()
        
    if db_data is not None:
        if len(db_data) > 0:
            #Fetch Data
            admin_db_id = db_data[0]
            admin_db_email = db_data[4]
            admin_db_password = db_data[5]
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
            return render(request, 'userpages/forgotpassword.html') 
    messages.success(request, 'Wrong Email Details')
    return render(request, 'userpages/forgotpassword.html')



def signup(request):
    return render(request,'userpages/signup.html')

def signup_addprocess(request):
    if request.method == 'POST':
        print(request.POST)
        aname = request.POST['txt1']
        gender = request.POST['txt2']
        dob = request.POST['txt3']
        email = request.POST['txt4']
        password = request.POST['txt5']
        cno = request.POST['txt6']
        pno = request.POST['txt7']
        address = request.POST['txt8']

        #Get File Value
        myfile = request.FILES['txt9']
        fs = FileSystemStorage()
        myfileupload = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(myfileupload)
        print("URL: " + uploaded_file_url)

        messages.add_message(request,messages.SUCCESS,'Sign up Successful')

        cur.execute("INSERT INTO `tbl_student`(`student_name`,`student_gender`,`student_D_O_B`,`student_email`,`student_password`,`student_mobileno`,`student_parentnno`,`student_address`,`student_img`) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(aname,gender,dob,email,password,cno,pno,address,myfile))
        conn.commit()
        return redirect(signup) 
    else:
        return redirect(signup)


def mailsenddemo(request):
    subject = 'Django Mail Demo'
    message = ' Hello How are you ?'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['ashvinrajput36@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponse("Mail Sent")


def login(request):
    return render(request,'userpages/login.html')

def loginpageprocess(request):
    user_email = request.POST['txt1']
    user_pass = request.POST['txt2']
    cur.execute("select * from `tbl_student` where `student_email` = '{}' and `student_password` = '{}'".format(user_email,user_pass))
    data = cur.fetchone()
    if data is not None:
        if len(data) > 0:
            #Fetch Data
            user_db_id = data[0]#fatch id of user
            user_db_email = data[1]#fatch email of user
            print(user_db_id)
            print(user_db_email)
            #store user information in Session
            request.session['user_id'] = user_db_id
            request.session['user_email'] = user_db_email
            #store user information in cookie
            response = redirect(userhome)
            response.set_cookie('user_id', user_db_id)
            response.set_cookie('user_email', user_db_email)
            return response
            #Cookie Code
        else:
                messages.success(request,'Log in Failed!')
                return render(request, 'userpages/login.html')
    messages.success(request,'Login Failed!')     
    return render(request, 'userpages/login.html')
   
def userhome(request):
    
    
    
    if 'user_email' in request.COOKIES and request.session.has_key('user_email'):
        user_emails=request.session['user_email']
        user_emailc=request.session['user_email']
        print("Session Email is" + user_emails)
        print("Cookie Email is" + user_emailc)
        return render(request, 'userpages/userhome.html')
    else:
        return render(request, 'userpages/userhome.html')  

    
    
    
def userlogout(request):
    del request.session['user_email']    
    del request.session['user_id'] 
    response=redirect(login)
    response.delete_cookie('user_id')   
    response.delete_cookie('user_email')   
    return response


def teachers(request):
    cur.execute("SELECT * FROM `tbl_teacher`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request, 'userpages/teachers.html', {'mydata': data})

def fees(request):
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
FROM
    `coachingdb`.`tbl_admission`
    INNER JOIN `coachingdb`.`tbl_fees` 
        ON (`tbl_admission`.`admission_id` = `tbl_fees`.`admission_id`)
    INNER JOIN `coachingdb`.`tbl_standerd` 
        ON (`tbl_standerd`.`standerd_id` = `tbl_fees`.`standerd_id`)
    INNER JOIN `coachingdb`.`tbl_student` 
        ON (`tbl_student`.`student_id` = `tbl_fees`.`student_id`);''')
    data1 = cur.fetchall()
    #return list(data)
    print(list(data1))

    return render(request,'userpages/fees.html',{'mydata1': data1 })

def timetable(request):
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
    return render(request, 'userpages/timetable.html', {'mydata': data})  

def reportcard(request):
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
    data2 = cur.fetchall()
    #return list(data)
    print(list(data2))


    return render(request,'userpages/reportcard.html', { 'mydata2': data2})

