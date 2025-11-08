from django.shortcuts import render, redirect
from .models import Funding
from .forms import FundingForm

def funding_list(request):
    fundings = Funding.objects.all()
    return render(request, 'funding/funding_list.html', {'fundings': fundings})

def funding_create(request):
    if request.method == 'POST':
        form = FundingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('funding_list')
    else:
        form = FundingForm()
    return render(request, 'funding/funding_form.html', {'form': form})

def funding_update(request, pk):
    funding = Funding.objects.get(pk=pk)
    if request.method == 'POST':
        form = FundingForm(request.POST, instance=funding)
        if form.is_valid():
            form.save()
            return redirect('funding_list')
    else:
        form = FundingForm(instance=funding)
    return render(request, 'funding/funding_form.html', {'form': form})

def funding_delete(request, pk):
    funding = Funding.objects.get(pk=pk)
    if request.method == 'POST':
        funding.delete()
        return redirect('funding_list')
    return render(request, 'funding/funding_confirm_delete.html', {'funding': funding})