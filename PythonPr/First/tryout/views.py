from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index_view(request, *args, **kwargs):
	return render(request, 'stuff.html', {})



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

##########################

import requests
from .models import numbers #imports class NUMBERS from models.py
from .forms import NumbersForm  #import form NUMBERSFORM from forms.py


def numbers_main_view(request):
	# obj = numbers.objects.get(id=1) izsauc visus numuru ierakstus no DB


	where = 'http://numbersapi.com/'
	url = where
	number = ''
	form = NumbersForm()
	visible = 'false'

	if request.method == 'POST': # executed when Search button pressed

		# if  request.POST.get('main-butt'):

		if 'main_butt' in request.POST: #checks if name in method is the rightone

			number = request.POST.get('number') #takes input with name NUMBER
			visible = 'true'
						
			url = where + str(number) #add two string together
			form = NumbersForm() #cleansout form

			data = requests.get(url) #gets data from url

			nr_fact = { #data to add db and html page
				'number': number,
				'fact': data.text,
			}

			numbers.objects.create(**nr_fact) #creating new record - '**' required if more than one value in {}

			context = { #context to add for html page
				'numbers': nr_fact,
				'form' : form,
				'visible': visible,
			}

		elif 'hist_butt' in request.POST:

			final_data = []
			allnumbers = numbers.objects.all()
			for numb in allnumbers:

				all_numbers = {
					'number': numb.number,
					'fact': numb.fact,
				}
				
				final_data.append(all_numbers)

			context = {
			'form': form,
			'final_data': final_data
			}

		else:
			context = {
				'form' : form
			}


	else: #will be executed when button wasnt pressed
		context = {
			'form' : form
		}

	return render(request, "numbers/main.html", context)


############################


from .forms import numbers_form, testing_numbers

def numbers_create_view(request):
	my_form = testing_numbers()
	if request.method == "POST":

		my_form = testing_numbers(request.POST) #request post is for validation
		if my_form.is_valid(): #data is comfirmed by fields
			print(my_form.cleaned_data)
			content.objects.create(**my_form.cleaned_data)
			
		else:
			print(my_form.errors)
	# context = {			this is optional (less efficient) way, how you could add context
	#	"title": obj.title,
	#	"description": obj.description
	#}

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