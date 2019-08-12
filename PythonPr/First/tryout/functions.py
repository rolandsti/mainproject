
import json
import os.path
import requests
from .models import numbers, cities #imports class NUMBERS from models.py
from .forms import *  #import form NUMBERSFORM from forms.py



def main_page_function(request):

	where = 'http://numbersapi.com/'
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
		


		return (context) #retuns json

	except Exception as e:
		print(type(e))
		visible = False
		form = NumbersForm()
		context = {
				'form' : form,
				'visible' : visible,
				'somealert': 'Something went horribly wrong... try different number:(',
				'popform': popform,
			}
	return (context)  #retuns json


def entry_page_function(request, entry_id): 

		obj = numbers.objects.get(id=entry_id)
		form = NumbersEntry(initial= {'fact': obj.fact,})
		
		final_data = []
		allnumbers = numbers.objects.all()
		final_data_count = 0

		for numb in allnumbers:
			if numb.number == obj.number and numb.id != obj.id:
				final_data_count += 1
				related_data = {
						'id': numb.id,
						'number': numb.number,
						'fact': numb.fact,
				}

				final_data.append(related_data)

		context = {
			'final_data_count' : final_data_count,
			'final_data': final_data,
			'form': form,
			'number' : obj.number,
			'id': obj.id,
		}
		return (context)


def delete_entry_function(request, entry_id):

		page = request.GET.get('location')
		obj = numbers.objects.get(pk=entry_id)
		obj.delete()


def edit_entry_function(request, entry_id):

		form = request.GET.get('form')
		if form == "":
		
			data = {'info' : 'Cannot save a blank field!'}

		else:

			obj = numbers.objects.get(pk=entry_id)
			obj.fact = form
			obj.save()
			print(1)
			data = {'info' : 'Done!'}

		return(data)


def create_entry_function(request): 

		number = request.GET.get('number')
		fact = request.GET.get('fact')

		if fact == "" or number == "":		
			data = {
				'info' : 'Can NOT save a blank field!',
				'success' : 'false',
			}

		else:
			success = True
			new_entry = {
				'number' : number,
				'fact'	: fact,
			}			
			numbers.objects.create(**new_entry)
			data = {
				'info' : 'Your fact was saved',
				'success' : 'true',
			}

		return (data)

def search_keyword_function(request):

		form = KeySearchForm()
		if request.method == 'GET':

			keywords = request.GET.get('keywords')
			if keywords != "":
				keyArray = keywords.split(" ")
				
				final_data = []
				all_numbers = numbers.objects.all()
				found_result_count = 0
				form = KeySearchForm()


				for one_entry in all_numbers:
					bingo = False
					number_string = str(one_entry.number)
					fact_string = str(one_entry.fact)
					for keyword in keyArray:
						if keyword.lower() in number_string.lower() or keyword.lower() in fact_string.lower():
							bingo = True

					if bingo == True:
						found_result_count += 1
						found_results = {
								'id': 		one_entry.id,
								'number': 	one_entry.number,
								'fact': 	one_entry.fact,
								}
						final_data.append(found_results)


			data = {
					"found_result_count": 	found_result_count,
					"final_data": 			final_data,			
				}

		return(data)

def list_of_cities_function(request):

	found_result_count = 0
	if request.method == 'GET':	
		city_to_find = request.GET.get('location')
		all_cities = cities.objects.all()
		final_data = []
		
		#leng = 0

		for one_city in all_cities:	
				
			# if len(one_city.name) > leng:
			# 		leng = len(one_city.name)
			# 		print (leng)
			# 		print (one_city.name)

			if city_to_find.lower() in one_city.name.lower():
			
				found_result_count += 1
				found_result = { 
				"city_id": one_city.city_id,
				"city_name": one_city.name,
				"country": one_city.country,
				}

				final_data.append(found_result)
				if found_result_count >= 7000:
					data = {
							"result_count"	: found_result_count,
							"final_data"	: final_data,
							"somealert"		: "There are 7000+ resuts... please be more specific",
					}
					break
				else:
					data = {"result_count"	: found_result_count,
							"final_data"	: final_data,
							}
			else:
				data = {
							"result_count"	: found_result_count,
							"final_data"	: final_data,
							}
	else:
		data = {
			"result_count": found_result_count,
		}

	return(data)