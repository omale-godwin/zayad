from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
# Create your views here.
from .models import Contact
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']


        contact = Contact(name=name, email=email, phone=phone, message=message, contact_date=datetime.now() )

        contact.save()

    # Send email
    # send_mail(
    #   'Property Listing Inquiry',
    #   'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
    #   'traversy.brad@gmail.com',
    #   [realtor_email, 'techguyinfo@gmail.com'],
    #   fail_silently=False
    # )

        messages.success(request, 'Your request has been submitted, we will get back to you soon')
        return redirect('contact')


        
    return render(request, 'contact/contact.html')















    