from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

import requests
from .models import numbers #imports class NUMBERS from models.py
from .forms import NumbersForm, NumbersEntry, WholeNumbersForm  #import form NUMBERSFORM from forms.py
from .functions import MainPage
from django.http import JsonResponse
from .forms import numbers_form, testing_numbers



def numbers_main_view(request): #history button and search

	#obj = numbers.objects.get(id=1) #izsauc visus numuru ierakstus no DB
	#MainPage(request)


	where = 'http://numbersapi.com/'
	url = where
	number = ''
	form = NumbersForm()
	popform = WholeNumbersForm()
	visible = False
	try:
		if request.method == 'POST': # checks if post activated

			# if  request.POST.get('main-butt'):

			if 'main_butt' in request.POST: #checks if name in method is the rightone

				number = request.POST.get('number') #takes input with name NUMBER
				visible = True
							
				url = where + str(number) #add two string together
				form = NumbersForm() #cleansout form

				data = requests.get(url) #gets data from url

				nr_fact = { #data to add db and html page
					'number': number,
					'fact': data.text,
					}

				numbers.objects.create(**nr_fact) #creating new record - '**' required if more than one value in {}

				context = { #context to add for html page
					'numbers'	: nr_fact,
					'form' 		: form,
					'visible'	: visible,
					'popform'	: popform,
				}

			elif 'hist_butt' in request.POST:

				final_data = []
				allnumbers = numbers.objects.all()
				for numb in allnumbers:
					
					all_numbers = {
						'id': numb.id,
						'number': numb.number,
						'fact': numb.fact,
					}
					
					final_data.append(all_numbers)

				context = {
				'form': form,
				'final_data': final_data,
				'popform': popform,
				}

			else:
				context = {
					'form' : form,
					'visible': visible,
					'popform': popform,
				}


		else: #will be executed when button wasnt pressed
			context = {
				'form' : form,
				'visible': visible,
				'popform': popform,
			}
		


		return render(request, "numbers/main.html", context)

	except:
		visible = False
		form = NumbersForm()
		context = {
				'form' : form,
				'visible' : visible,
				'somealert': 'Something went horribly wrong... Maybe too big of a number:)',
				'popform': popform,
			}

		return render(request, "numbers/main.html", context)

###########################
###########################


def numbers_entry_view(request, entry_id):

	try:

		obj = numbers.objects.get(id=entry_id)
		form = NumbersEntry(initial= {'fact': obj.fact,})
		
		final_data = []
		allnumbers = numbers.objects.all()

		for numb in allnumbers:
			if numb.number == obj.number and numb.id != obj.id:
				
				related_data = {
						'id': numb.id,
						'number': numb.number,
						'fact': numb.fact,
				}

				final_data.append(related_data)

		context = {
			'final_data': final_data,
			'form': form,
			'number' : obj.number,
			'id': obj.id,
		}

		return render(request, "numbers/main_entry.html", context)
	except:

		raise Http404("Impossible action")

	


###########################
###########################


def numbers_delete_view (request, entry_id):

	try:

		page = request.GET.get('location')
		obj = numbers.objects.get(pk=entry_id)
		obj.delete()
		data = {'info' : 'Entry has been deleted!'}

		return JsonResponse(data)

	except:

		raise Http404("Impossible action")



def numbers_edit_view (request, entry_id):

	try:
		form = request.GET.get('form')
		if form == "":
		
			data = {'info' : 'Cannot save a blank field!'}

		# elif form.is_integer() == true:
		# 	data = {'info' : 'Cant save just number!'}

		else:

			obj = numbers.objects.get(pk=entry_id)
			obj.fact = form
			obj.save()
			data = {'info' : 'Done!'}
			
		return JsonResponse(data)

	except:

		raise Http404("Impossible action")
	

###########################
###########################


def numbers_create_view(request):

	try:

		
		number = request.GET.get('number')
		fact = request.GET.get('fact')
		print(number)
		print(fact)
		if fact == "" or number == "":

			
			data = {
				'info' : 'Can NOT save a blank field!',
				'success' : 'false',
			}

		# elif isinstance(serialize(input), int):

		# 	data = {
		# 		'info' : 'Invalid description!',
		# 		'success' : 'false',
		# 	}

		else:
			success = True
			new_entry = {
				'number' : number,
				'fact'	: fact,
			}			
			numbers.objects.create(**new_entry)
			data = {
				'info' : 'Changes have been made',
				'success' : 'true',
			}
			
			


		return JsonResponse(data)

	except:

		raise Http404("Impossible action")
	

  

def stuff_create_view(request):
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