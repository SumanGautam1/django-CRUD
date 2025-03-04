from django.shortcuts import render, redirect
from .models import Details
from django.contrib import messages

def details(request):
    """
    Handles the display and creation of Details entries.

    If the request method is POST, it extracts data from the form (name, age, email, remark),
    creates a new Details object, and saves it to the database. Then, it redirects to the 'details' page.

    If the request method is GET, it retrieves all non-deleted Details objects and renders
    them on the 'details.html' template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Renders the 'details.html' template with the context data or redirects to the 'details' page.
    """
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        age = data.get('age')
        email = data.get('email')
        remark = data.get('remark')
        d = Details(name=name, age=age, email=email, remark=remark)
        d.save()
        messages.success(request, "Data added successfully!")
        return redirect('details')
    
    data = Details.objects.filter(is_deleted=False)
    return render(request, 'details.html', {'data':data})

def delete_data(request, id):
    """
    Handles the soft deletion of a Details entry.

    If the request method is POST, it retrieves the Details object with the given ID,
    marks it as deleted by setting `is_deleted` to True, and saves the changes.
    Then, it redirects to the 'details' page.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The ID of the Details object to be soft-deleted.

    Returns:
        HttpResponseRedirect: Redirects to the 'details' page.
    """
    if request.method == "POST":
        data = Details.objects.get(id=id)
        data.is_deleted = True
        data.save()
        return redirect('details')

def edit_data(request, id):
    """
    Handles the editing of a Details entry.

    If the request method is POST, it retrieves the updated data from the form (name, age, email, remark),
    updates the corresponding Details object, and saves the changes. Then, it redirects to the 'details' page.

    If the request method is GET, it renders the 'details.html' template.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The ID of the Details object to be edited.

    Returns:
        HttpResponse: Renders the 'details.html' template or redirects to the 'details' page.
    """
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
    """
    Displays all soft-deleted Details entries in the recycle bin.

    Retrieves all Details objects where `is_deleted` is True and renders them on the 'recycle.html' template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Renders the 'recycle.html' template with the context data.
    """
    rd = Details.objects.filter(is_deleted=True)
    return render(request,'recycle.html',{'rd':rd})

def delete_bin(request, id):
    """
    Permanently deletes a Details entry from the recycle bin.

    If the request method is POST, it retrieves the Details object with the given ID,
    permanently deletes it from the database, and redirects to the 'details' page.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The ID of the Details object to be permanently deleted.

    Returns:
        HttpResponseRedirect: Redirects to the 'details' page.
    """
    if request.method == "POST":
        data = Details.objects.get(id=id)
        data.delete()
        return redirect('details')

def restore_bin(request, id):
    """
    Restores a soft-deleted Details entry from the recycle bin.

    Retrieves the Details object with the given ID, marks it as not deleted by setting `is_deleted` to False,
    and saves the changes. Then, it redirects to the 'details' page.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The ID of the Details object to be restored.

    Returns:
        HttpResponseRedirect: Redirects to the 'details' page.
    """
    data = Details.objects.get(id=id)
    data.is_deleted = False
    data.save()
    return redirect('details')

def clearbin(request):
    """
    Permanently deletes all soft-deleted Details entries from the recycle bin.

    Retrieves all Details objects where `is_deleted` is True, permanently deletes them from the database,
    and redirects to the 'bin' page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponseRedirect: Redirects to the 'bin' page.
    """
    data = Details.objects.filter(is_deleted=True)
    data.delete()
    return redirect('bin')

