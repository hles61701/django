from django.shortcuts import render
from django.contrib import messages

from account.forms import UserForm


def register(request):
    '''
    Register a new user
    '''
    template = 'account/register.html'
    if request.method == 'GET':
        return render(request, template, {'userForm': UserForm()})

    # POST
    userForm = UserForm(request.POST)
    if not userForm.is_valid():
        return render(request, template, {'userForm': userForm})

    userForm.save()
    messages.success(request, '歡迎註冊')
    return redirect('main:main')
