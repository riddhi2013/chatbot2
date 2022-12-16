from django.contrib import admin
from .models import *
from django.core.mail import EmailMultiAlternatives

# Register your models here.
admin.site.register(link_keyword)
admin.site.register(text_keyword)
admin.site.register(About_Us)
class manual_responseAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if change:
            subject='Admin has responded to your query!'
            message='Your query : ' + obj.new_keyword + '\nAdmin Response : ' + obj.admin_data
            sender='test1.saubhagyam@gmail.com'
            recipient=obj.email_id
            mail = EmailMultiAlternatives(subject, message, sender, [recipient])
            mail.send()
            super().save_model(request, obj, form, change)
        else:
            super().save_model(request, obj, form, change)

admin.site.register(manual_response, manual_responseAdmin)
# admin.site.register(AskConsultant)
admin.site.register(text_keyword_arabic)
admin.site.register(About_Us_arabic)
# admin.site.register(AskConsultant_arabic)
class manual_response_arabicAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if change:
            subject='لقد رد المسؤول على استفسارك!'
            message='طلبك :' + obj.new_keyword_arabic + '\nاستجابة المسؤول : ' + obj.admin_data_arabic
            sender='test1.saubhagyam@gmail.com'
            recipient=obj.email_id_arabic
            mail = EmailMultiAlternatives(subject, message, sender, [recipient])
            mail.send()
            super().save_model(request, obj, form, change)
        else:
            super().save_model(request, obj, form, change)

admin.site.register(manual_response_arabic, manual_response_arabicAdmin)

class links_manual_responseAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if change:
            subject='Admin has responded to your query!'
            message='Topic : ' + obj.new_topic + '\nMaterial : ' + obj.admin_data
            sender='test1.saubhagyam@gmail.com'
            recipient=obj.email_id
            mail = EmailMultiAlternatives(subject, message, sender, [recipient])
            mail.send()
            super().save_model(request, obj, form, change)
        else:
            super().save_model(request, obj, form, change)

admin.site.register(links_manual_response, links_manual_responseAdmin)

class arabic_links_manual_responseAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if change:
            subject='لقد رد المسؤول على استفسارك!'
            message='عنوان :' + obj.new_topic_arabic + '\n مواد : ' + obj.admin_data
            sender='test1.saubhagyam@gmail.com'
            recipient=obj.email_id_arabic
            mail = EmailMultiAlternatives(subject, message, sender, [recipient])
            mail.send()
            super().save_model(request, obj, form, change)
        else:
            super().save_model(request, obj, form, change)

admin.site.register(arabic_links_manual_response, arabic_links_manual_responseAdmin)
