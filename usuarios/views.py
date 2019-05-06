from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from usuarios.models import User

# Create your views here.

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email','name','last_name']

def user_list(request, template_name='usuarios/user_list.html'):
    usuarios = User.objects.all()
    data = {}
    data['object_list'] = usuarios
    return render(request, template_name, data)

def user_create(request, template_name='usuarios/user_form.html'):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('user_list')
    return render(request, template_name, {'form':form})

def user_update(request, pk, template_name='usuarios/user_edit.html'):
    user= get_object_or_404(User, pk=pk)
    form = UserForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('user_list')
    return render(request, template_name, {'form':form})

def user_delete(request, pk, template_name='usuarios/user_confirm_delete.html'):
    user= get_object_or_404(User, pk=pk)    
    if request.method=='POST':
        user.delete()
        return redirect('user_list')
    return render(request, template_name, {'object':User})  