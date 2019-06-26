from django.http import HttpResponse, HttpRequest
import requests
from django.shortcuts import render
from .models import numbers #imports class NUMBERS from models.py
from .forms import NumbersForm  #import form NUMBERSFORM from forms.py


def MainPage(request):

	where = 'http://numbersapi.com/'
	url = where
	number = ''
	form = NumbersForm()
	visible = False

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
				'numbers': nr_fact,
				'form' : form,
				'visible': visible,
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
			}

		else:
			context = {
				'form' : form,
				'visible': visible,
			}


	else: #will be executed when button wasnt pressed
		context = {
			'form' : form,
			'visible': visible,
		}
	print("hello")
	return render(request, "numbers/main.html", context)
