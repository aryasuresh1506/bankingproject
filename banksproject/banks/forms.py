import json
from django import forms
from django.forms import ModelForm
from .models import Forum, Branches,Register

class RegisterForm(forms.ModelForm):
    password_confirmation = forms.CharField(widget=forms.PasswordInput(),label="Confirm Password")
    class Meta:
        model = Register
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get("password_confirmation")

        if password and password_confirmation and password != password_confirmation:
            self.add_error('password_confirmation',"Password and confirmation do not match")

        return cleaned_data

class UserForum(forms.ModelForm):
    CHOICES = [
        ('Debit', 'Debit Card'),
        ('Credit', 'Credit Card'),
        ('Cheque', 'Through Cheque'),
    ]
    material = forms.MultipleChoiceField(
        choices=CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False)
    class Meta:
        model = Forum
        fields = ['username', 'name', 'dob', 'age', 'gender', 'phoneno', 'email', 'address', 'district', 'branch', 'accounttype', 'material']
        widgets={
            'dob':forms.DateInput(attrs={'type':'date'}),
            'gender':forms.RadioSelect()
        }

    def clean_material(self):
        return ','.join(self.cleaned_data['material'])

    def __init__(self,*args,**kwargs):
        super(UserForum, self).__init__(*args,**kwargs)
        branches_data = list(Branches.objects.values('id','branch','district'))
        self.fields['branch'].widget = forms.Select()
        self.fields['branch'].queryset = Branches.objects.none()
        self.branches_json =json.dumps(branches_data)
        self.fields['district'].widget = forms.Select(
            choices=[('', 'Select District')] + [(district, district) for district in
                                                 Branches.objects.values_list('district', flat=True).distinct()])
        self.fields['username'].widget.attrs['readonly']=True

        if self.instance and self.instance.material:
            self.fields['material'].initial = self.instance.material.split(',')


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Register
        fields = ['username', 'password']
