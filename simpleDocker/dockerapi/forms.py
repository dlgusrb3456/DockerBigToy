from django import forms

class CreateForm(forms.Form):
    stack_name = forms.CharField(max_length=15)
    create_yml = forms.CharField(widget=forms.Textarea)

class CreateNetworkForm(forms.Form):
    network_driver = forms.CharField(max_length=15)
    network_name = forms.CharField(max_length=15)

class loginForm(forms.Form):
    docker_id = forms.CharField(max_length=15)
    docker_pw = forms.CharField(widget=forms.Textarea)

