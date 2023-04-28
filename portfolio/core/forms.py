from django import forms
from django_countries import widgets, countries
from django.forms.widgets import TextInput, EmailInput
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import RegionalPhoneNumberWidget

class TailwindTextInput(TextInput):
    def __init__(self, attrs=None):
        default_attrs = {'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border-2 border-amber-300 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white"type="text"'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)

class TailwindEmailInput(EmailInput):
    def __init__(self, attrs=None):
        default_attrs = {'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border-2 border-amber-300 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white" type="text"'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50, widget=TailwindTextInput)
    last_name = forms.CharField(max_length=50, widget=TailwindTextInput)
    email_address = forms.EmailField(max_length=150, widget=TailwindEmailInput)
    phone_number = PhoneNumberField(region="SE", widget=RegionalPhoneNumberWidget(attrs={'class':'appearance-none block w-full bg-gray-200 text-gray-700 border-2 border-amber-300 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white'}))
    country = forms.ChoiceField(widget=widgets.CountrySelectWidget(attrs={'class':'appearance-none block w-full bg-gray-200 text-gray-700 border-2 border-amber-300 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white', 'style':'font-family: Roboto'}), choices=countries)
    title = forms.CharField(max_length=50, widget=TailwindTextInput)
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'appearance-none block w-full bg-gray-200 text-gray-700 border-2 border-amber-300 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white', 'style':'font-family: Roboto'}), max_length=2000)
    user_agreement = forms.BooleanField(required=True)
