from django import forms 
# Django's built in valdiation
from django.core import validators

# To create custom validator, define the method outside the class
# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("Needs to start with Z")

class FormName(forms.Form):
    # With the validators from django.core, we can pass in a validator argument inside of the fields that takes in array of valdiations
    # name = forms.CharField(validators=[check_for_z])
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter your email again: ")
    text = forms.CharField(widget=forms.Textarea)
    # botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators = [validators.MaxLengthValidator(0)])
    
    # Basic way to do your own valdiation
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data["botcatcher"]
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("Gotcha bot")
        
    #     return botcatcher

    # Cleaning the entire form at once

    def clean(self): #clean indicates to Django that this is for all 
        all_clean_data = super().clean() # calling super is going to grab all the clean data at once
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Make sure email match")



    
    