from django.shortcuts import render,redirect
from .ii import result
from .models import Predictions
from .forms import PredictionsForm
#from django.views.generic import DetailView,UpdateView,DeleteView
#
#
#class TaskDetailView(DetailView):
#    model = Task
#    template_name = 'main/details_view.html'
#    context_object_name = 'task'
#class TaskUpdateView(UpdateView):
#    model = Task
#    template_name = 'main/create.html'
#    form_class = TaskForm
#class TaskDeleteView(DeleteView):
#    model = Task
#    success_url = '/'
#    template_name = 'main/delete.html'
#def сreate(request):
#    error = ''
#    if request.method == 'POST':
#        form = TaskForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('home')
#        else:
#            error = 'Форма не верна'
#    form = TaskForm()
#    context = {
#        'form': form
#    }
#    return render(request,'main/create.html',context)
def index(request):
    
    if request.method == 'POST':
        forms = PredictionsForm(request.POST)
        

        if forms.is_valid():
            forms.save()
            return redirect('home')
        else:
            pass
        
    else:
        error = 'Форма не верна' 
    answer = None
    predictions = Predictions.objects.order_by('-id')[:1]
    forms = PredictionsForm()

    if predictions:
        if str(result(predictions[0].full_text)) == '0':
            answer = False
        else:
            answer = True
    data = {'title': 'Главная Страница','predictions':predictions,'forms':forms,'response_type':answer}
    error = ''

    return render(request, 'main/index.html', data)


def about(request):
    data = {'title': 'О нас'}
    return render(request, 'main/about.html', data)


def documentation(request):
    data = {'title': 'Документация',}
    return render(request, 'main/documentation.html', data)