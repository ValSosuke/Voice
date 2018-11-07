from django import forms
from django.utils.translation import ugettext as _




EDITION = (('system', 'system'), ('memset', 'memset'), ('strcpy', 'strcpy'),('strlen','strlen'))
class UploadFileForm(forms.Form):
    file = forms.FileField(label='',)
    file1 = forms.FileField(label='',)
    Select_functions = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(),choices=EDITION)
#ClearableFileInput
    
    