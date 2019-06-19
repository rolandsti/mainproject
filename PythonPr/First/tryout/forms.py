from django import forms

from .models import content

class numbers_form(forms.ModelForm):
	class Meta:
		model = content
		fields = [
			'title',
			'description',
			'morefields',
		]

class testing_numbers(forms.Form):
	title		 = forms.CharField(label='The Title', widget=forms.TextInput(attrs={"placeholder": "type something here"}))
	description	 = forms.CharField(label='The description', widget=forms.Textarea(
																	attrs={
																		"class":"two",
																		"cols":30,
																		"rows" : 20
																		}
																	)

																)
	morefields	 = forms.CharField(label='The NO-USE-FIELD')