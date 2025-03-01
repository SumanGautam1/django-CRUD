from django.shortcuts import render, redirect
from .models import Details

# Create your views here.
def details(request):
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        age = data.get('age')
        email = data.get('email')
        remark = data.get('remark')
        Details.objects.create(name=name, age=age, email=email, remark=remark)
        return redirect('details')
    
    data = Details.objects.filter(is_deleted=False)
    return render(request, 'details.html', {'data':data})

def delete_data(request, id):
    if request.method == "POST":
        data = Details.objects.get(id=id)
        data.is_deleted = True
        data.save()
        return redirect('details')
    

def edit_data(request,id):
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        age = data.get('age')
        email = data.get('email')
        remark = data.get('remark')
        old_data = Details.objects.get(id=id)
        old_data.name = name
        old_data.age = age
        old_data.email = email
        old_data.remark = remark
        old_data.save()
        return redirect('details')
    
    return render(request, 'details.html')

def recycle(request):
    rd = Details.objects.filter(is_deleted=True)
    return render(request,'recycle.html',{'rd':rd})

def delete_bin(request, id):
    if request.method == "POST":
        data = Details.objects.get(id=id)
        data.delete()
        return redirect('details')
    

def restore_bin(request, id):
    data = Details.objects.get(id=id)
    data.is_deleted = False
    data.save()
    return redirect('details')


def clearbin(request):
    data = Details.objects.filter(is_deleted=True)
    data.delete()
    return redirect('bin')