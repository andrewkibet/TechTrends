from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Staff, Leave
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, 'forms/index.html')

def sup(request):
    if User.is_authenticated:
        code = request.user.username
        fname = request.user.first_name
        lname = request.user.last_name
        full_name = fname +" "+ lname
        leaves =Leave.objects.filter(sup_code=code, supervised=False)
        if leaves is not None:
            if request.method == 'POST':
                sub_fname = request.POST['sub_fname']
                sub_lname = request.POST['sub_lname']
                substitute = sub_fname + " " + sub_lname
                sub_pjnumber = request.POST['sub_pjnumber']
                sub_job = request.POST['sub_job']
                sub_dept = request.POST['sub_dept']
                approved = request.POST['approved']
                comments = request.POST['comments']
                date = request.POST['date']
                leave_id = request.POST['leave_id']

                leave = Leave.objects.get(id=leave_id)
                leave.sub_code = sub_pjnumber
                leave.sub_job = sub_job
                leave.substitute = substitute
                leave.unit = sub_dept
                leave.Approved = approved
                leave.sup_comment = comments
                leave.approval_date = date
                leave.supervisor = full_name
                leave.supervised = True
                

                if approved == True:
                    eocode = leave.eo_code
                    executive = User.objects.get(username = eocode)
                    staff_name = leave.staff.user.first_name + " " + leave.staff.user.last_name
                    eo_mail = executive.email
                    subject = 'Leave Application'
                    message = f'You have pending Leave Assessment from {staff_name}. Please login to your Leave Management system to assess it.'
                    # email_from = settings.EMAIL_HOST_USER
                    email_from = 'johngachunga21@gmail.com'
                    recipient = [eo_mail]
                    auth_user = settings.EMAIL_HOST_USER
                    auth_password = settings.EMAIL_HOST_PASSWORD
                    send_mail(subject, message, email_from, recipient, auth_user, auth_password)

                    leave.save()
                else:
                    subject = 'Leave Approval'
                    message = 'Your Leave application has NOT been approved.'
                    # email_from = settings.EMAIL_HOST_USER
                    staff_mail = leave.staff.user.email
                    email_from = 'johngachunga21@gmail.com'
                    recipient = [staff_mail]
                    auth_user = settings.EMAIL_HOST_USER
                    auth_password = settings.EMAIL_HOST_PASSWORD
                    send_mail(subject, message, email_from, recipient, auth_user, auth_password)
                    leave.save()


                messages.success(request, "Leave Applied by"+" " + leave.staff.user.first_name +" "  "Successfully assessed.")

            return render(request, 'forms/supervisor.html', {'leaves':leaves, 'name':fname, 'full_name':full_name})
        else:
            messages.error(request, "You don\'t have any messages.")
            return redirect('/apply')  
    else:
        messages.error(request, "You need to be authenticated to access this page. Please login!")
        return redirect('/home')

def lapp(request):
    return render(request, 'forms/lapp.html')

def assess(request):
    if User.is_authenticated:
        code = request.user.username
        name = request.user.first_name
        full_name = name +" "+request.user.last_name
        leaves = Leave.objects.filter(eo_code=code, assessed=False)

        if request.method == 'POST':
            leave_id = request.POST['leave_id']
            prev_year_bal = request.POST['prev_year_bal']
            entitlement = request.POST['entitlement']
            total_leave_days = prev_year_bal + entitlement
            days_taken = request.POST['days_taken']
            days = request.POST['days']
            dayss_taken = days_taken + days
            balance = request.POST['balance']

            comments = request.POST['comments']
            date = request.POST['Date']

            leave = Leave.objects.get(id=leave_id)
            leave.staff.prev_year_bal = prev_year_bal
            leave.staff.entitlement = entitlement
            leave.staff.days_taken = dayss_taken
            leave.staff.balance = balance
            leave.staff.total_leave_days = total_leave_days

            leave.executive = full_name
            leave.exec_comment = comments
            leave.assess_date = date
            leave.assessed = True
            

            subject = 'Leave Approval'
            message = 'Your Leave application has been APPROVED.'
            # email_from = settings.EMAIL_HOST_USER
            staff_mail = leave.staff.user.email
            email_from = 'johngachunga21@gmail.com'
            recipient = [staff_mail]
            auth_user = settings.EMAIL_HOST_USER
            auth_password = settings.EMAIL_HOST_PASSWORD
            send_mail(subject, message, email_from, recipient, auth_user, auth_password)
            leave.save()

            messages.success(request, "Leave Applied by"+" " + leave.staff.user.first_name +" "  "Successfully assessed.")

        return render(request, 'forms/assess.html', {'full_name' : full_name,'leaves' : leaves, 'name':name})
    else:
        messages.error(request, "You need to be authenticated to access this page. Please login!")
        return redirect('/home')

def apply(request):
    if User.is_authenticated:
        pj = request.user.username
        name = request.user.first_name
        full_name = name + " " + request.user.last_name
        email = request.user.email
        sect = request.user.staff.section
        design = request.user.staff.designation
        num = request.user.staff.number
        state = request.user.staff.station


        if request.method == "POST":
            designation = request.POST['designation']
            section = request.POST['section']
            station = request.POST['station']
            number = request.POST['number']

            myuser = User.objects.get(username=pj)
            # staff = Staff.objects.get(staff=myuser)

            if myuser is not None:
                myuser.staff.designation = designation
                myuser.staff.section = section
                myuser.staff.station = station
                myuser.staff.number = number
                myuser.save()
                
            
            days = request.POST['days']
            typ = request.POST['typ']
            fdate = request.POST['from_date']
            tdate = request.POST['to_date']
            rdate =request.POST['report']
            specify = request.POST['specify']
            address = request.POST['address']
            lnumber = request.POST['lnumber']

            efname = request.POST['efname']
            elname = request.POST['elname']
            sfname = request.POST['sfname']
            slname = request.POST['slname']

            sup = User.objects.get(first_name=sfname, last_name=slname)
            executive = User.objects.get(first_name=efname, last_name=elname)
            if sup is not None and executive is not None:
                sup_mail = sup.email
                # eomail = executive.email
                sup_username = sup.username
                eo_username = executive.username
                exstatus = executive.staff.status
                if(exstatus==False):
                    messages.error(request,"Invalid Executive Officer")
                    return redirect('/apply')
                else:
                    staff = Staff.objects.get(user=myuser)

                    leave = Leave.objects.create(staff=staff)
                    leave.days = days
                    leave.leave_type = typ
                    leave.wef = fdate
                    leave.upto = tdate
                    leave.report_date = rdate
                    leave.others = specify
                    leave.address = address
                    leave.contact = lnumber 
                    leave.sup_code = sup_username 
                    leave.eo_code = eo_username 

                    subject = 'Leave Application'
                    message = f'You have pending Leave approval from {full_name}. Please login to your Leave Management system to assess it.'
                    email_from = settings.EMAIL_HOST_USER
                    recipient = [sup_mail]
                    auth_user = settings.EMAIL_HOST_USER
                    auth_password = settings.EMAIL_HOST_PASSWORD
                    send_mail(subject, message, email_from, recipient, auth_user, auth_password)
                    leave.save()
                    
                    messages.success(request, "Application successfull. Wait for a confirmation Email.")
                    logout(request)
                    return redirect('/home')
                
            elif sup is None:
                messages.error(request,"* Invalid Direct Supervisor. Please Your supuervisor's details and that they are Registered.*")
                return redirect('/apply')
            else:
                messages.error(request,"* Invalid Executive Officer. Please Your Executive's details and that they are Registered. *")
                return redirect('/apply')
        return render(request, 'forms/apply.html', {'name' : name, 'full_name': full_name, 'section' : sect,
                    'number' : num, 'email' : email, 'station' : state, 'designation' : design, 'pjnum' : pj})
    else:
        messages.error(request, "You need to be authenticated to access this page. Please login!")
        return redirect('/home')

def test(request):
#     pj = {{pjnum}}
#     myuser = User.objects.get(username=pj)
#     staff = Staff.objects.get(user=myuser)

#     pjnumber = myuser.username
#     name = myuser.first_name
#     email = myuser.email
#     section = staff.section
#     number = staff.number
#     email = staff.email
#     station = staff.station
#     designation = staff.designation
#     full_name = myuser.first_name + " " + myuser.last_name
    return render(request, 'forms/test.html')

def signup(request):

    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST['lname']
        pjnumber = request.POST['pjnumber']
        designation = request.POST['designation']
        station = request.POST['station']
        section = request.POST['section']
        number = request.POST['num']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username=pjnumber):
            messages.error(request, "PJ Number already exists! Please try some other Usernumber")
        
        if User.objects.filter(email=email):
            messages.error(request, "Email already exists. Please try some other email")
        

        if password1!=password2:
            messages.error(request, "Passwords didn\'t match")
        else:        
            myuser = User.objects.create_user(username=pjnumber,email = email, password=password1)
            myuser.first_name = fname
            myuser.last_name = lname 
            myuser.email = email

            myuser.save()

            staff = Staff(user=myuser)
            staff.designation = designation
            staff.station = station
            staff.section = section
            staff.number = number

            staff.save()

            return redirect('/')


    return render(request, 'forms/signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['pjnumber']
        password = request.POST['password']

        myuser = authenticate(username=username, password=password)

        if myuser is not None:
            login(request, myuser)
            staff = Staff.objects.get(user=myuser)
            if staff.status == True:
                return redirect('assess')
            else:
                return redirect('apply')
        else:
            messages.error(request, "Invalid Username or Password.")

    return render(request, 'forms/signin.html')

def signout(request):
    logout(request)
    return redirect('home')
