# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 22:15:27 2018

@author: SANTIAGO
"""

from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)