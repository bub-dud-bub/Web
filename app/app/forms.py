# -*- coding: cp1251 -*-
"""
Definition of forms.
"""

from tkinter import FALSE
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from.models import Blog
from.models import Comment

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': '��� ������������'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'������'}))

class AnketaForm(forms.Form):
    name = forms.CharField(label="���� ���", min_length=2, max_length=100)
    city = forms.CharField(label="��� �����", min_length=2, max_length=100)
    job = forms.CharField(label="��� ��� �������", min_length=2, max_length=100)
    gender = forms.ChoiceField(label="��� ���",
                            choices=[('1', '�������'), ('2', '�������')],
                            widget=forms.RadioSelect, initial=1)
    internet = forms.ChoiceField(label="�� ����������� ����������",
                                choices=(('1', '������ ����'),
                                ('2', '��������� ��� � ����'),
                                ('3', '��������� ��� � ������'),
                                ('4', '��������� ��� � �����')), initial=1)
    notice = forms.BooleanField(label='�������� ������� � ����� �� E-mail?', required=False)
    email = forms.EmailField(label="��� E-mail", min_length=7)
    message = forms.CharField(label="������� � ����", widget=forms.Textarea(attrs={'rows':12,'cols':20}))
                             
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment  
        fields = ('text',)  
        labels = {'text': "�����������"}

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'image',)
        lavels = {'title': "���������", 'descrition': "������� ����������", 'content': "������ ����������", 'image': "��������"}