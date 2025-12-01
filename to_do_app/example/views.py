from django.shortcuts import render, redirect
from django.views import View
from .models import Task, Category

class CreateTaskView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'create_task.html', {'categories': categories})
    
    def post(self, request):
        title = request.POST.get('title')
        description = request.POST.get('description')
        priority = request.POST.get('priority')
        due_date = request.POST.get('due_date')
        category_id = request.POST.get('category')
        
        category = Category.objects.get(id=category_id)
        task = Task.objects.create(
            title=title,
            description=description,
            priority=priority,
            due_date=due_date,
            category=category,
            user=request.user
        )
        return redirect('task_list')

def home(request):
    return render(request, 'home.html')