from django.core.mail import EmailMultiAlternatives
from django.db import models

# Create your models here.
class link_keyword(models.Model):
    keyword_values = models.CharField(primary_key=True, max_length=100, verbose_name='Keyword', help_text='Enter keyword here')
    keyword_values_arabic = models.CharField(max_length=100, verbose_name='Arabic Keyword',
                                             help_text='Enter keyword in arabic here', default='')
    links = models.TextField(max_length=1000, verbose_name='Link', help_text='Enter corresponding link here')

    def __str__(self):
        return self.keyword_values

    class Meta:
        # Add verbose name
        verbose_name_plural = 'Keywords and Links'
        verbose_name = 'keyword and link'


class text_keyword(models.Model):
    keyword_value = models.TextField(primary_key=True, verbose_name='Question', help_text='Enter question here')
    desc = models.TextField(verbose_name='Intent', help_text='Enter corresponding response here')
    tag = models.TextField(max_length = 100, verbose_name='Tag', help_text='Enter corresponding unique tag here')

    def __str__(self):
        return self.keyword_value

    class Meta:
        # Add verbose name
        verbose_name_plural = 'Questions and Intents'
        verbose_name = 'question and intent'


class About_Us(models.Model):
    about_us_paragraph = models.TextField(primary_key=True, help_text="Enter about us here")

    def __str__(self):
        return self.about_us_paragraph

    class Meta:
        # Add verbose name
        verbose_name_plural = 'About Us'
        verbose_name = 'about us'


class manual_response(models.Model):
    new_keyword = models.CharField(max_length=100, verbose_name='Non-Database Keyword', primary_key=True)
    admin_data = models.TextField(verbose_name='Admin Response')
    email_id = models.EmailField(verbose_name='Added By', default='')

    def __str__(self):
        return self.new_keyword

    class Meta:
        # Add verbose name
        verbose_name_plural = 'Manual Responses'
        verbose_name = 'manual response'

class links_manual_response(models.Model):
    new_topic = models.CharField(max_length=100, verbose_name='New Topic', primary_key=True)
    admin_data = models.TextField(verbose_name='Admin Response')
    email_id = models.EmailField(verbose_name='Added By', default='')

    def __str__(self):
        return self.new_topic

    class Meta:
        # Add verbose name
        verbose_name_plural = 'Manual Responses to Links'
        verbose_name = 'manual response to link'

class AskConsultant(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    file_number = models.CharField(max_length=10, verbose_name='File Number', primary_key=True)
    inquiry = models.TextField(verbose_name='Inquiry')

    def __str__(self):
        return self.file_number

    class Meta:
        # Add verbose name
        verbose_name_plural = 'Inquiries'
        verbose_name = 'inquiry'


# ARABIC MODELS

class text_keyword_arabic(models.Model):
    keyword_value_arabic = models.CharField(primary_key=True,max_length=100, verbose_name='Question', help_text='Enter question here')
    desc_arabic = models.TextField(verbose_name='Intent', help_text='Enter corresponding response here')

    def __str__(self):
        return self.keyword_value_arabic

    class Meta:
        # Add verbose name
        verbose_name_plural = 'Questions and Intents (Arabic)'
        verbose_name = 'arabic question and intent'


class About_Us_arabic(models.Model):
    about_us_paragraph_arabic = models.TextField(primary_key=True)

    def __str__(self):
        return self.about_us_paragraph_arabic

    class Meta:
        # Add verbose name
        verbose_name_plural = 'About Us (Arabic)'
        verbose_name = 'about us'


class manual_response_arabic(models.Model):
    new_keyword_arabic = models.CharField(max_length=100, verbose_name='Non-Database Keyword', primary_key=True)
    admin_data_arabic = models.TextField(verbose_name='Admin Response')
    email_id_arabic = models.EmailField(verbose_name='Added By', default='')

    def __str__(self):
        return self.new_keyword_arabic

    class Meta:
        # Add verbose name
        verbose_name_plural = 'Manual Responses (Arabic)'
        verbose_name = 'arabic manual response'


class AskConsultant_arabic(models.Model):
    name_arabic = models.CharField(max_length=100, verbose_name='Name')
    file_number_arabic = models.CharField(max_length=10, verbose_name='File Number', primary_key=True)
    inquiry_arabic = models.TextField(verbose_name='Inquiry')

    def __str__(self):
        return self.file_number_arabic

    class Meta:
        # Add verbose name
        verbose_name_plural = 'Inquiries (Arabic)'
        verbose_name = 'inquiry in arabic'

class arabic_links_manual_response(models.Model):
    new_topic_arabic = models.CharField(max_length=100, verbose_name='New Topic', primary_key=True)
    admin_data = models.TextField(verbose_name='Admin Response')
    email_id_arabic = models.EmailField(verbose_name='Added By', default='')

    def __str__(self):
        return self.new_topic_arabic

    class Meta:
        # Add verbose name
        verbose_name_plural = 'Manual Responses to Arabic Links'
        verbose_name = 'manual response to arabic link'