from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import AskConsultant, AskConsultant_arabic, manual_response, manual_response_arabic, links_manual_response, arabic_links_manual_response


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class InquiryForm(forms.ModelForm):
    class Meta:
        model = AskConsultant
        fields = ['name', 'file_number', 'inquiry']

class InquiryFormArabic(forms.ModelForm):
    class Meta:
        model = AskConsultant_arabic
        fields = ['name_arabic', 'file_number_arabic', 'inquiry_arabic']

class ManualResponseForm(forms.ModelForm):
    class Meta:
        model = manual_response
        fields = ['new_keyword', 'email_id']

class ManualResponse_arabicForm(forms.ModelForm):
    class Meta:
        model = manual_response_arabic
        fields = ['new_keyword_arabic', 'email_id_arabic']

class Links_manualResponseForm(forms.ModelForm):
    class Meta:
        model = links_manual_response
        fields = ['new_topic', 'email_id']

class arabicLinks_manualResponseForm(forms.ModelForm):
    class Meta:
        model = arabic_links_manual_response
        fields = ['new_topic_arabic', 'email_id_arabic']