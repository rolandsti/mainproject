from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index_view(request, *args, **kwargs):
	return render(request, 'index.html', {})

def home_view(request, *args, **kwargs):
	context = {
		"location" : "Home",
		"some_number" : 10
	}
	return render(request, "home.html", context)


def about_view(request,*args, **kwargs):
	context = {
		"location" : "About",
		"some_number" : 10,
		"some_list": [111, 222, 333, "Hello"]
	}
	return render(request, 'about.html', context)

def string_view(*args, **kwargs):
	return HttpResponse("<h1>Hello</h1>") #html string

from .models import content #tiek importets modela satrus

def numbers_main_view(request):
	obj = content.objects.get(id=1)
	# context = {			this is optional (less efficient) way, how you could add context
	# 	"title": obj.title,
	# 	"description": obj.description
	# }

	context = {		
		'object': obj
	}

	return render(request, "numbers/main.html", context)



from .forms import numbers_form, testing_numbers

def numbers_create_view(request):
	my_form = testing_numbers()
	if request.method == "POST":

		my_form = testing_numbers(request.POST) #request post is for validation
		if my_form.is_valid(): #data is comfirmed by fields
			print(my_form.cleaned_data)
			#content.objects.create(**my_form.cleaned_data)
			
		else:
			print(my_form.errors)
	context = {
		"form" 	: my_form,
		"sss"	: "title"
		
	}

###############
###############

# 
# 	if request.method == "POST":
# 		record = request.POST.get('title')
# 		print(record)
# 	context = {
# 		'stuff': record,
# 	}

#############
#############

	# form = numbers_form(request.POST or None)
	# if form.is_valid():
	# 	#form.save()
	# 	form = numbers_form() #clears out the form
	# context = {		
	# 	'form': form
	# }

	return render(request, "numbers/main_create.html", context)