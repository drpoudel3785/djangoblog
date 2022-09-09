from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User, auth
from email.message import EmailMessage
import ssl 
import smtplib
from .models import tbl_Employee
import datetime as dt
import pandas as pd
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import csv
import uuid

# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login') 
            
    else:
        return render(request, 'account/login.html')



def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                print("Username Taken")
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                print("Email Taken")
            else:
                user = User.objects.create_user(username=username, 
                password=password1, email=email, first_name=first_name, 
                last_name=last_name)
                user.save()
                lid = User.objects.latest('id')
                print("User Created")
                email_sender = "dharmarajpoudel@gmail.com"
                email_password = "zlptgjwgewgrkylz"

                email_receiver = email
                subject = "User Registration Success";
                body = """
  <h1>Welcome to the Site</h1>
  <p>THis is test body message</p>
  <a href='https://localhost:8000/verify/?id="""+ str(lid.id)+ """'>Verify</a>

"""
                em = EmailMessage()
                em['From'] = email_sender
                em['To'] = email
                em['subject'] = subject
                em.set_content(body)
                em.set_type('text/html')
                #temp-mail.org
                context  = ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as smtp:
                    smtp.login(email_sender, email_password)
                    smtp.sendmail(email_sender, email_receiver, em.as_string())      
        else:
            print("Password not Match")
        return redirect('/')
    else:
        return render(request, 'account/register.html')


# Create your views here.


 
def Import_csv(request):
    print('s')               
    try:
        if request.method == 'POST' and request.FILES['myfile']:
          
            myfile = request.FILES['myfile']        
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            excel_file = uploaded_file_url
            
            print(excel_file) 
            #empexceldata = pd.read_csv("."+excel_file, header = 0, encoding='unicode_escape', on_bad_lines='skip')
            empexceldata = pd.read_excel("."+excel_file)
            print(type(empexceldata))
            dbframes = empexceldata
          
            for dbframe in dbframes.itertuples():
                print(dbframe) 
                print(dbframe.DOB)
                print(dbframe.Empcode)
                fromdate_time_obj = dt.datetime.strptime(dbframe.DOB, '%d-%m-%Y')
                obj = tbl_Employee.objects.create(Empcode=dbframe.Empcode,firstName=dbframe.firstName, middleName=dbframe.middleName,
                                                lastName=dbframe.lastName, email=dbframe.email, phoneNo=dbframe.phoneNo, address=dbframe.address, 
                                                exprience=dbframe.exprience, gender=dbframe.gender, DOB=fromdate_time_obj,
                                                #DOB = dbframe.DOB,
                                                qualification=dbframe.qualification)
                print(type(obj))
                obj.save()
 
            return render(request, 'account/importexcel.html', {
                'uploaded_file_url': uploaded_file_url
            })    
    except Exception as identifier:            
        print(identifier)
     
    return render(request, 'account/importexcel.html',{})
def export_users_csv(request):
    if request.method == 'POST':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f"attachment; filename=EmployeeData{uuid.uuid4()}.csv"       
        writer = csv.writer(response)
        writer.writerow(['Employee Detail'])       
                 
         
        writer.writerow(['Employee Code','Employee Name','Relation Name','Last Name','gender','DOB','e-mail','Contact No' ,'Address' ,'exprience','Qualification'])
 
        users = tbl_Employee.objects.all().values_list('Empcode','firstName' , 'middleName' , 'lastName','gender','DOB','email','phoneNo' ,'address','exprience','qualification')
         
        for user in users:
            writer.writerow(user)
        return response
 
    return render(request, 'account/exportexcel.html')
