from django.shortcuts import render, redirect
from django.contrib import messages

from agriapp.forms import ImageUploadForm
from agriapp.models import Contact, Admin, Farmers, Customers, ImageModel, Register_courses


# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == 'POST':
        mycontact = Contact(
            fname=request.POST['fname'],
            lname=request.POST['lname'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            county=request.POST['county'],
            message=request.POST['message']
        )
        mycontact.save()
        messages.success(request, 'Your contact has been sent')
        return redirect('/contact')
    else:
        return render(request, 'contact.html')

def courses(request):
    return render(request, 'courses.html')

def shop(request):
    return render(request, 'shop.html')

def sign_farmer(request):
    if request.method == 'POST':
        farmers=Farmers(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            password=request.POST['password'],
        )
        farmers.save()
        return redirect('sign_farmer')
    else:
        return render(request, 'sign_farmer.html')

    return render(request, 'sign_farmer.html')

def login_farmer(request):
        return render(request,'sign_farmer.html')

def sign_customer(request):
    if request.method == 'POST':
        customers=Customers(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            password=request.POST['password'],
        )
        customers.save()
        messages.success(request, 'Your customers have been saved.')
        return redirect('sign_customer')
    else:
        return render(request,'sign_customer.html')

    return render(request, 'sign_customer.html')

def login_customer(request):
        return render(request,'sign_customer.html')

def register_courses(request):
    if request.method == 'POST':
        members=Register_courses(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            gender=request.POST['gender'],
            location=request.POST['location'],
            course=request.POST['course'],
            hours=request.POST['hours'],
        )
        members.save()
        messages.success(request, 'You have successfully registered.')
        return redirect('register_courses')
    else:
        return render(request,'register_courses.html')

    return render(request, 'register_courses.html')

def admin_courses(request):
    allcourses=Register_courses.objects.all()
    return render(request,'admin_couses.html',{'allcourses':allcourses})

def admin_home(request):
    if request.method == 'POST':
        if Admin.objects.filter(
            username=request.POST['username'],
            password=request.POST['password']
        ).exists():
            messages.success(request, 'You have successfully logged in.')
            return render(request,'admin_home.html')
        else:
            return render(request, 'admin_login.html')
    else:
        return render(request, 'admin_login.html')

def admin_login(request):
    return render(request, 'admin_login.html')

def admin_courses(request):
    allcourses=Register_courses.objects.all()
    return render(request, 'admin_courses.html',{'allcourses':allcourses})

def farmers_dashboard(request):
    if request.method == 'POST':
        if Farmers.objects.filter(
            email=request.POST['email'],
            password=request.POST['password']
        ).exists():
            return redirect('farmers_dashboard')
        else:
            return render(request,'sign_farmer.html')
    else:
        return render(request, 'sign_farmer.html')

def product_details(request):
    allimage=ImageModel.objects.all()
    return render(request,'product_detail.html',{'allimage':allimage})


def shop(request):
    images = ImageModel.objects.all()
    return render(request, 'shop.html', {'images': images})

def admin_farmers(request):
    allfarmers = Farmers.objects.all()
    return render(request,'admin_farmers.html',{'farmers':allfarmers})

def customer(request):
    if request.method == 'POST':
        if Customers.objects.filter(
            email=request.POST['email'],
            password=request.POST['password']
        ).exists():
            messages.success(request, 'You have successfully logged in.')
            return redirect('customer_dashboard')
        else:
            return render(request,'sign_customer.html')
    else:
        return render(request, 'sign_customer.html')

def customer_dashboard(request):
    customers = ImageModel.objects.all()
    return render(request, 'customer_dashboard.html',{'customers':customers})

def admin_contacts(request):
    allcontacts = Contact.objects.all()
    return render(request,'admin_contact.html',{'allcontacts':allcontacts})
