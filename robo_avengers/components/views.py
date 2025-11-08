from django.shortcuts import render, redirect
from .models import Component
from .forms import ComponentForm

def component_list(request):
    components = Component.objects.all()
    return render(request, 'components/component_list.html', {'components': components})

def component_create(request):
    if request.method == 'POST':
        form = ComponentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('component_list')
    else:
        form = ComponentForm()
    return render(request, 'components/component_form.html', {'form': form})

def component_update(request, pk):
    component = Component.objects.get(pk=pk)
    if request.method == 'POST':
        form = ComponentForm(request.POST, instance=component)
        if form.is_valid():
            form.save()
            return redirect('component_list')
    else:
        form = ComponentForm(instance=component)
    return render(request, 'components/component_form.html', {'form': form})

def component_delete(request, pk):
    component = Component.objects.get(pk=pk)
    if request.method == 'POST':
        component.delete()
        return redirect('component_list')
    return render(request, 'components/component_confirm_delete.html', {'component': component})