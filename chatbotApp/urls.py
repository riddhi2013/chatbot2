from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('chatbot/',views.home,name="home"),
    path('',views.home_arabic,name="home_arabic"),
    # path('', TemplateView.as_view(template_name="chatbotApp/SelectLanguage.html")),
    path('InquiryForm/', views.AskConsultant, name="inquiryForm"),
    path('InquiryForm1/', views.AskConsultant_arabic, name="inquiryForm1"),
    path('queryForm/', views.manualResponse, name="queryForm"),
    path('queryForm1/', views.manualResponse_arabic, name="queryForm1"),
    path('linkForm/', views.manualResponse_links, name="linkForm"),
    path('linkForm_arabic/', views.arabic_manualResponse_links, name="linkForm_arabic")
]