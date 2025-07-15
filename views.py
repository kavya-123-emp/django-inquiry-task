from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomerForm  # import the form

def inquiry_view(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your inquiry has been submitted successfully.')
            return redirect('inquiry')  # redirect after successful form submission
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomerForm()

    return render(request, 'inquiry_form.html', {'form': form})
