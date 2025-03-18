from django.shortcuts import render
from django import forms

class MyForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    shift = forms.ChoiceField(label='Shift', choices=[('morning', 'Morning'), ('evening', 'Evening')])

def form_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Process the data
            return render(request, 'success.html', {'form': form})
    else:
        form = MyForm()
    return render(request, 'home.html', {'form': form})