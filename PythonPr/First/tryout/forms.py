from django import forms

from .models import content, numbers

class numbers_form(forms.ModelForm):
	class Meta:
		model = content
		fields = [
			'title',
			'description',
			'morefields',
		]

class testing_numbers(forms.Form):
	title		 = forms.CharField(label='The Title', widget=forms.TextInput(attrs={"placeholder": "Virsraksts"}))
	description	 = forms.CharField(label='The description', widget=forms.Textarea(
																	attrs={
																		"class":"two",
																		"cols": 30,
																		"rows" : 20,
																		"placeholder" : "Ziņa"
																		}
																	)

																)
	morefields	 = forms.CharField(label='The NO-USE-FIELD')

class NumbersForm(forms.ModelForm):
	class Meta:
		model = numbers
		fields = ['number']
		widgets = {'number': forms.NumberInput(attrs={	"class"			: "main-input",
														"placeholder" 	: "type some number",
														"id"			: "le_input",
														"autocomplete"	: "off"
														} ) }


class NumbersEntry(forms.ModelForm):
	class Meta:
		model = numbers
		fields = ['fact']
		widgets =	{ 'fact' : forms.Textarea	(attrs=	{	"class" : "entry-fact-input",
															"id"	: "entry-fact-input",
															"cols"	: 1,
															"rows"	: 4,
														}
												)
					}

class WholeNumbersForm(forms.Form):
	number		= forms.CharField(label='The Title', widget=forms.NumberInput(attrs={
																		"placeholder": "type your number here",
																		"id"	: "pop-number",
																		"class"	: "pop-number",
																		"autocomplete" : "off",
																		}))
	fact		= forms.CharField(label='The description', widget=forms.Textarea(
																	attrs={
																		"class"	:"pop-fact",
																		"id"	:"pop-fact",
																		"cols"	: 1,
																		"rows" 	: 6,
																		"placeholder" : "what is interesting about it?",
																		}
																	)

																)
class KeySearchForm(forms.Form):
		keywords = forms.CharField(label='The Title', widget=forms.TextInput(attrs={
																		"placeholder": "what do you want to find?",
																		"id"	: "search_field",
																		"class"	: "main-input",
																		"autocomplete" : "off",
																		}))