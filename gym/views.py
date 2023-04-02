from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import gym_website
from django.contrib.auth.models import User
from .models import contact_detail
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
# below import  done for sending emails
from django.conf import settings
from django.core import mail
from django.core.mail import send_mail
from django.core.mail import EmailMessage

# Create your views here.


def save(request):

    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        gender = request.POST.get("gender")
        dob = request.POST.get("dob")

        database = gym_website(name=name, phone=phone,
                               email=email, gender=gender, dob=dob)
        database.save()
        return HttpResponse('Data is saved')

    return render(request, "gym/project.html")


def handlelogin(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        pass1 = request.POST.get("pass1")
        myuser = authenticate(username=uname, password=pass1)
        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login Successful")
            return redirect("/")
        else:
            messages.success(request, "Invalid Credentials")
            return redirect("/login")

    return render(request, 'gym/login.html')


def handlesignup(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        Email = request.POST.get("email")
        Pass1 = request.POST.get("pass1")
        Pass2 = request.POST.get("pass2")
        if Pass1 != Pass2:
            messages.warning(request, "Password is incorrect")
            return redirect('/signup')

        try:
            if User.objects.get(username=uname):
                messages.info(request, "username Already taken")
                return redirect('/signup')

        except:
            pass
        try:
            if User.objects.get(email=Email):
                messages.success(request, "Email Already taken")
                return redirect('/signup')

        except:
            pass

        mydata = User.objects.create_user(uname, Email, Pass1)
        mydata.save()
        messages.success(request, "Login is Successful")
        return redirect('/login')

    return render(request, 'gym/signup.html')


def contact(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        Email = request.POST.get("email")
        Description = request.POST.get("description")
        database1 = contact_detail(
            name=uname, email=Email, message=Description)
        database1.save()
        from_email = settings.EMAIL_HOST_USER
        connection = mail.get_connection()
        connection.open()
        email_message = mail.EmailMessage(f' Email from {uname} ', f' Usermail : {Email} \n\n\n Query : {Description} ', from_email, [
                                          'shahusupa19et@student.mes.ac.in','surajshahu559@gmail.com',], connection=connection)
        connection.send_messages([email_message])
        connection.close()
        messages.info(request,"Your Response has been recorded , we will get back soon.....")
        return redirect('/contact')
        

    return render(request, "gym/contact.html")

def handlelogout(request):
    logout(request)
    messages.info(request,"Logout Successfully")
    return redirect('/login')
