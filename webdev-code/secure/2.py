from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()

@csrf_exempt
def add_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        # Django ORM uses parameterized queries by default
        user = User.objects.create(username=username, email=email)
        return HttpResponse('User added securely!')
    return render(request, 'add_user.html')
