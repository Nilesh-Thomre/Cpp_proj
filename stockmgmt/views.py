from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages

def home(request):
	title = 'Welcome: This is the Home Page'
	context = {
	"title": title,
	}
	return render(request, "home.html",context)
def list_item(request):
	title = 'List of Items'
	queryset = Stock.objects.all()
	context = {
		"title": title,
		"queryset": queryset,
	}
	return render(request, "list_item.html", context)

def add_items(request):
    form = StockCreateForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully added')

        return redirect('/list_item')
    
    context = {
        "form": form,
        "title": "Add Item",
    }
    
    return render(request, "add_items.html", context)

def update_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = StockUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = StockUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			messages.success(request, 'Successfully updated')

			return redirect('/list_item')

	context = {
		'form':form
	}
	return render(request, 'add_items.html', context)
def delete_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		messages.success(request, 'Successfully deleted')
		return redirect('/list_item')
	return render(request, 'delete_items.html')