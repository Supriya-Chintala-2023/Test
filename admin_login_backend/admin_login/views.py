from django.shortcuts import render
from django.http import JsonResponse

def login_view(request):
    admin_id = request.POST.get('admin_id')
    password = request.POST.get('password')

    # Add your login logic here
    
    if admin_id == 'Naborino' and password == 'summer2023':
        return JsonResponse({'message': 'Login successful'})
    else:
        return JsonResponse({'message': 'Invalid credentials'}, status=401)
