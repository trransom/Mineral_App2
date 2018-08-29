from django import forms

class SearchBar(forms.ModelForm):
	search = forms.CharField(
				widget=forms.TextInput(
					attrs={'placeholder': 'Search for minerals by their name!'}
				)
			)
			