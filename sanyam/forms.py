from django import forms
import pandas as pd

class UploadFileForm(forms.Form):
#    title = forms.CharField(max_length=50)
    file = forms.FileField()
