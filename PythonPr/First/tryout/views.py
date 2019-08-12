from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import numbers, content, cities #imports class NUMBERS from models.py
from .forms import *  #import form NUMBERSFORM from forms.py
from .functions import *
from .test_functions import *
from django.http import JsonResponse
from .forms import numbers_form, testing_numbers
from django.core import serializers
import json
import os
import os.path
import requests
	

def numbers_main_view(request): ### history button and search

	context = main_page_function(request);
	return render(request, "numbers/main.html", context)



def numbers_entry_view(request, entry_id): ### opens individual entries

	try:
		context = entry_page_function(request, entry_id)
		return render(request, "numbers/main_entry.html", context)

	except:
		raise Http404("Impossible action")

	

def numbers_delete_view (request, entry_id): ### deletes entries when called upon

	try:
		delete_entry_function(request, entry_id)
		data = {'info' : 'Entry has been deleted!'}
		return JsonResponse(data)

	except:
		raise Http404("Impossible action")



def numbers_edit_view (request, entry_id): ### edits entries in individual entry page

	try:
		data = edit_entry_function(request, entry_id)
		print(entry_id)
		return JsonResponse(data)

	except:

		raise Http404("Impossible action")

def numbers_create_view(request):  ### creates new entrie in main page

	try:
		data = create_entry_function(request)		
		return JsonResponse(data)

	except:

		raise Http404("Impossible action")
	


def settings_view(request): ### opens up settings page

	return render(request, 'settings/settings.html')


def search_keyword_view(request):
	
	try:
		form = KeySearchForm()
		result = search_keyword_function(request)

		data = {
		"found_result_count": 	result["found_result_count"],
		"final_data": 			result["final_data"],
		"form":					form,
		}
		

	except:
		form = KeySearchForm()
		data = {
			"form": form,
			"somealert": "Something went horribly wrong... try different keyword:(",
		}
	return render(request, 'searching.html', data)






def  api_search_keyword_view(request):
	try:
		result = search_keyword_function(request)
		

	except:
		result = {
		"found_result_count": 	result["found_result_count"],
		}
	return JsonResponse(result)





def apimerge_view(request, *args, **kwargs):

	if request.method == "GET":

		city_to_find = request.GET.get('location')

		if city_to_find and len(city_to_find) <= 100:

			result = list_of_cities_function(request)

			if result['result_count'] < 7000:
				data = {
					"result_count"	: result["result_count"],
					"final_data"	: result["final_data"],
					"input"			: city_to_find,
					}
			else:
				data = {
					"result_count"	: result["result_count"],
					"final_data"	: result["final_data"],
					"somealert"		: "There are 7000+ resuts... please be more specific",
					"input"			: city_to_find,
					}

			return render(request, 'apimerge/apimerge.html', data)

		else:
			if city_to_find and len(city_to_find) > 300:
				data = {"somealert" : "Invalid request"}
				return render(request, 'apimerge/apimerge.html', data)
			else:
				return render(request, 'apimerge/apimerge.html')

			








def apimerge_entry_view(request, keystring):
	try:
		if request.method == 'GET':
			city_id = keystring

			if len(city_id) < 10:
				query_params = "?id=" + city_id
				link = "http://127.0.0.1:7071/getsomedata" + query_params

				data = requests.get(link).json()			
				return render(request, "apimerge/apimerge_entry.html", data)

			else:
				data = {
					"somealert": "Invalid request",
				}
				return render(request, "apimerge/apimerge.html", data)
		
	except:
		data = {
					"somealert": "Invalid request",
				}


		return render(request, "apimerge/apimerge.html", data)


def list_of_cities_view(request):

	try:
		data = list_of_cities_function(request)
	except:
		found_result_count = 0
		data = {"result_count": found_result_count,}
	return JsonResponse(data, safe=False)



##### JSON file conversion to SQLlite ###
	# base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	# file_path = os.path.join(base_path, "tryout/templates/apimerge/smol_list.json")
	# print(file_path)
	# json_data = open(file_path, encoding="utf8")
	# data_load = json.load(json_data)
	# 
	# for city in data_load:
	# 	entry = {
	# 		"name": city['name'],
	# 		"country": city['country'],
	# 		"city_id": city['id']
	# 	}
	# cities.objects.create(**entry)

	# data = json.dumps(data_load)
	# json_data.close
	# return JsonResponse(data, safe=False)
##########################################

##########################################

#### DOWN FROM HERE IS NOTHING WORTHY ####

##########################################



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