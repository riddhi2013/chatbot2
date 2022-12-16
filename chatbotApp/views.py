# Create your views here.
import datetime
import time
import sys
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.http import JsonResponse
from django.shortcuts import redirect, render
from .forms import (InquiryForm, InquiryFormArabic, ManualResponse_arabicForm,
                    ManualResponseForm, Links_manualResponseForm, arabicLinks_manualResponseForm)
from .models import *
from .models import About_Us, About_Us_arabic, AskConsultant, link_keyword
from .trained_english_model import response
from .arabic_trained_model import response_arabic
global link_flag, text_flag
from django.core.mail import EmailMultiAlternatives


ans_input = ""


# Create your views here.

def home(request):
    if request.method == 'POST':
        form = request.POST
        print(form, 'form data .....')
        code = form.get('title')
        msgType = form.get('msgType')
        print(code)

        if msgType == 'About Us':
            ans_input = select_about_us()
        elif msgType == 'Consult Me' and code == '' :
            ans_input = 'Please enter your query'
        elif msgType == 'Consult Me' and code != '' :
            ans_input = select_text_by_keyword(code)
        elif msgType == 'Gain Knowledge' and code == '':
            ans_input = 'Enter a topic in which you would like to surf the materials available right now..'
        elif msgType == 'Gain Knowledge' and code != '' :
            ans_input = select_link_by_keyword(code)
        # elif code == 'Ask Your Consultant':
            # ans_input = u"<a href={0} style=\"color: yellow\">{1}</a>".format('/InquiryForm',
                                                                            #   'Click here to submit your inquiry!')        elif code == "":
            pass
        else:
            ans_input = "invalid option"

        if code == '':
            data_json = {
            'msg': msgType,

            'ans': ans_input
        }
        else:
            data_json = {
            'msg': code,

            'ans': ans_input
        }

        return JsonResponse(data_json)

    context = {}
    return render(request, 'chatbotApp/index.html', context)

def home_arabic(request):
    if request.method == 'POST':
        form = request.POST
        print(form, 'form data .....')
        code = form.get('title')
        msgType = form.get('msgType')

        if msgType == 'عن الخدمة':
            ans_input = select_about_us_arabic()
        elif msgType == 'استشرني' and code == '' :
            ans_input = 'الرجاء إدخال الاستعلام الخاص بك'
        elif msgType == 'استشرني' and code != '' :
            ans_input = select_text_by_keyword_arabic(code)
        elif msgType == 'مكتبة الجودة والاعتماد الأكاديمي' and code == '':
            ans_input = 'أدخل موضوعًا ترغب في تصفح المواد المتاحة فيه الآن ..'
        elif msgType == 'مكتبة الجودة والاعتماد الأكاديمي' and code != '' :
            ans_input = select_link_by_keyword_arabic(code)

        if code == '':
            data_json = {
            'msg': msgType,

            'ans': ans_input
        }
        else:
            data_json = {
            'msg': code,

            'ans': ans_input
        }

        return JsonResponse(data_json)

    context = {}
    return render(request, 'chatbotApp/index_arabic.html', context)


def english_menu():
    menu = "Welcome to Quality and Academic Accreditation Chatbot </br></br> Please select an option :"\
        "\t </br> 1. About the Service \n\t  </br> 2. Consult Me \n\t  </br> 3. Gain Knowledge \n\t </br> 4. Ask your consultant\n\t </br> 5. Show menu again"
    return menu


def arabic_menu():
    arabic_menu = "مرحبًا بكم في Chatbot للجودة والاعتماد الأكاديمي  </br> </br> الرجاء تحديد خيار :"\
        "\t </br>1. حول الخدمة ، </br> 2. استشرني  </br> 3. اكتساب المعرفة  </br> 4. اسأل مستشارك  </br> 5 . مخرج "
    return arabic_menu


def select_about_us():
    """
    Query about us in the about us table
    :return:
    """
    aboutUs = About_Us.objects.filter(about_us_paragraph__isnull=False)
    aboutUs = aboutUs[0]
    return aboutUs.about_us_paragraph


def select_about_us_arabic():
    """
    Query about us in the about us arabic table
    :return:
    """
    aboutUs_arabic = About_Us_arabic.objects.filter(
        about_us_paragraph_arabic__isnull=False)
    aboutUs_arabic = aboutUs_arabic[0]
    return aboutUs_arabic.about_us_paragraph_arabic


def select_text_by_keyword(queryString):
    """
    Query in the text_keyword table
    :return:
    """
    bot_response = response(queryString)
    form_link = u"<a href = {0} style =\"color: yellow\">{1}</a>".format('/queryForm',
                                                                             'click here to submit your query directly to the admin!')
    if bot_response:
        return bot_response+'<br> If you think that I have not provided you the right answer, kindly ' + form_link
    else:
        return 'Sorry, I don\'t have an answer for this right now.. <br><br>' + form_link


def select_text_by_keyword_arabic(queryString):
    """
    Query in the text_keyword_arabic table
    :return:
    # """
    bot_response = response_arabic(queryString)
    form_link = u"<a href = {0} style =\"color: yellow\">{1}</a>".format('/queryForm1',
                                                                             'انقر هنا لإرسال استفسارك مباشرة إلى المسؤول!')
    if bot_response:
        return bot_response+'<br> If you think that I have not provided you the right answer, kindly ' + form_link
    else:
        return 'في حال انكم غير راضين عن اجابتي، فضلا . '+ form_link


def select_link_by_keyword(queryString):
    """
        Query in the link_keyword table
        :return:
        """
    link_keyword_value = link_keyword.objects.filter(
        keyword_values__contains=str(queryString))
    if link_keyword_value:
        final_response = link_keyword_value[0].links
        return final_response

    else:
        error_msg = "Sorry, there are no links available regarding this right now.."
        noLink_form = u"<a href = {0} style =\"color: yellow\">{1}</a>".format('/linkForm',
                                                                             'Click here to submit your query directly to the admin!')
        return error_msg + '<br>' + noLink_form

def select_link_by_keyword_arabic(queryString):
    link_keyword_arabic_value = link_keyword.objects.filter(
        keyword_values_arabic__contains=str(queryString))
    if link_keyword_arabic_value:
        final_response = link_keyword_arabic_value[0].links
        return final_response

    else:
        error_msg = "عذرا ، لا توجد روابط متاحة بخصوص هذا الآن .."
        noLink_form = u"<a href = {0} style =\"color: yellow\">{1}</a>".format('/linkForm_arabic',
                                                                             'انقر هنا لإرسال استفسارك مباشرة إلى المسؤول!')
        return error_msg + '<br>' + noLink_form



def AskConsultant(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            Inquiry = form.save(commit=False)
            Inquiry.name = request.POST.get('name')
            Inquiry.file_number = request.POST.get('file_number')
            Inquiry.inquiry = request.POST.get('inquiry')
            Inquiry.save()
            return redirect('home')
    else:
        form = InquiryForm
    return render(request, 'chatbotApp/InquiryForm.html', {'form': form})


def AskConsultant_arabic(request):
    if request.method == 'POST':
        form = InquiryFormArabic(request.POST)
        if form.is_valid():
            Inquiry = form.save(commit=False)
            Inquiry.name = request.POST.get('name')
            Inquiry.file_number = request.POST.get('file_number')
            Inquiry.inquiry = request.POST.get('inquiry')
            Inquiry.save()
            return redirect('home')
    else:
        form = InquiryForm
    return render(request, 'chatbotApp/InquiryForm1.html', {'form': form})

def manualResponse(request):
    if request.method == 'POST':
        form = ManualResponseForm(request.POST)
        if form.is_valid():
            Query = form.save(commit=False)
            Query.new_keyword = request.POST.get('new_keyword')
            Query.email_id = request.POST.get('email_id')
            Query.save()
            new_key_mail('A new query has been added!', 'Query : ' + Query.new_keyword + '\nGo to https://yabushark.pythonanywhere.com/admin/chatbotApp/manual_response to provide response', 'test1.saubhagyam@gmail.com', 'test1.saubhagyam@gmail.com')
            return redirect('home')
    else:
        form = ManualResponseForm
    return render(request, 'chatbotApp/queryForm.html', {'form': form})

def manualResponse_links(request):
    if request.method == 'POST':
        form = Links_manualResponseForm(request.POST)
        if form.is_valid():
            Query = form.save(commit=False)
            Query.new_topic = request.POST.get('new_topic')
            Query.email_id = request.POST.get('email_id')
            Query.save()
            new_key_mail('A new inquiry for material has been added!', 'Topic : ' + Query.new_topic + '\nGo to https://yabushark.pythonanywhere.com/admin/chatbotApp/links_manual_response to provide response', 'test1.saubhagyam@gmail.com', 'test1.saubhagyam@gmail.com')
            return redirect('home')
    else:
        form = Links_manualResponseForm
    return render(request, 'chatbotApp/linkForm.html', {'form': form})

def arabic_manualResponse_links(request):
    if request.method == 'POST':
        form = arabicLinks_manualResponseForm(request.POST)
        if form.is_valid():
            Query = form.save(commit=False)
            Query.new_topic_arabic = request.POST.get('new_topic_arabic')
            Query.email_id_arabic = request.POST.get('email_id_arabic')
            Query.save()
            new_key_mail('تمت إضافة استفسار جديد عن المواد!', 'عنوان : ' + Query.new_topic_arabic + '\nاذهب إلى https://yabushark.pythonanywhere.com/admin/chatbotApp/arabic_links_manual_response/ لتقديم استجابة', 'test1.saubhagyam@gmail.com','test1.saubhagyam@gmail.com')
            return redirect('home')
    else:
        form = arabicLinks_manualResponseForm
    return render(request, 'chatbotApp/linkForm_arabic.html', {'form': form})


def manualResponse_arabic(request):
    if request.method == 'POST':
        form = ManualResponse_arabicForm(request.POST)
        if form.is_valid():
            Query = form.save(commit=False)
            Query.new_keyword = request.POST.get('new_keyword_arabic')
            Query.email_id = request.POST.get('email_id_arabic')
            Query.save()
            new_key_mail('تم إضافة استعلام جديد!', 'طلبك : ' + Query.new_keyword_arabic + '\n اذهب إلى https://yabushark.pythonanywhere.com/admin/chatbotApp/manual_response_arabic/ لتقديم استجابة',  'test1.saubhagyam@gmail.com','test1.saubhagyam@gmail.com')
            return redirect('home')
    else:
        form = ManualResponseForm
    return render(request, 'chatbotApp/queryForm1.html', {'form': form})


def exit():
    exit = "Thank You!"
    return exit


def arabic_exit():
    arabic_exit = 'اشكرك'
    return arabic_exit


def new_key_mail(sub,msg,sender,recipient):
    subject = sub
    message = msg
    # 'A new query ''%s'' is added to the database. \nRun the server and go to https://yabushark.pythonanywhere.com/admin/chatbotApp/manual_response/ to add response.' % (question)
    mail = EmailMultiAlternatives(
        subject, message, sender, [recipient])
    mail.send()
