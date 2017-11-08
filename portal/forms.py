from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from datetime import datetime
from portal.models import Document, Profile, Comments


"""
UserCreationForm contain password1 and password2(conf.password)
it also check both password must be same
"""


class SignUpPage(UserCreationForm):                 # renders a signup form to user with the help of template
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


class Info(forms.ModelForm):                       # renders a form to user where he can fill his personal
                                                   # details with the help of template
    class Meta:
        model = Profile
        fields = ('First_Name', 'Last_Name', 'City', 'DOB', 'profile_pic', )

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('comment',)



class DocumentForm(forms.ModelForm):                   # to render to user a form where he can upload pictures
                                                       # it is connected to Document table in database
    class Meta:
        model = Document
        status = forms.ModelChoiceField(queryset=Document.objects.filter(uploaded_at=datetime.now()), empty_label=None)
        width = forms.IntegerField()
        height = forms.IntegerField()
        flip = forms.ModelChoiceField(queryset=Document.objects.filter(uploaded_at=datetime.now()), empty_label=None)
        rotate = forms.ModelChoiceField(queryset=Document.objects.filter(uploaded_at=datetime.now()), empty_label=None)
        blur = forms.ModelChoiceField(queryset=Document.objects.filter(uploaded_at=datetime.now()), empty_label=None)
        effect = forms.ModelChoiceField(queryset=Document.objects.filter(uploaded_at=datetime.now()), empty_label=None)
        fields = ('document', 'status', 'width', 'height','rotate', 'flip', 'blur', 'effect')


class UpdateForm(forms.ModelForm):                     # renders a form update pictures uploaded
                                                       # it is connected to Document table in database
    class Meta:
        model = Document
        status = forms.ModelChoiceField(queryset=Document.objects.filter(uploaded_at=datetime.now()),
                                        empty_label=None)
        width = forms.IntegerField()
        height = forms.IntegerField()
        flip = forms.ModelChoiceField(queryset=Document.objects.filter(uploaded_at=datetime.now()),
                                      empty_label=None)
        rotate = forms.ModelChoiceField(queryset=Document.objects.filter(uploaded_at=datetime.now()),
                                         empty_label=None)
        blur = forms.ModelChoiceField(queryset=Document.objects.filter(uploaded_at=datetime.now()),
                                      empty_label=None)
        effect = forms.ModelChoiceField(queryset=Document.objects.filter(uploaded_at=datetime.now()),
                                        empty_label=None)
        fields = ('status', 'width','height', 'flip', 'rotate', 'blur', 'effect')




