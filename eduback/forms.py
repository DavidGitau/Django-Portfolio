from django import forms
from django.forms.widgets import (
    CheckboxSelectMultiple, 
    RadioSelect
)
from educenter.models import (
    About, 
    Blog, 
    Course, 
    Event, 
    FunFact, 
    Interest, 
    Notice,
    Requirement, 
    Research, 
    School,
    Scholarship, 
    Teacher
)
from crispy_forms.helper import FormHelper
from django.utils.translation import gettext_lazy as l
from crispy_forms.layout import (
    Div, 
    Field, 
    Fieldset, 
    HTML, 
    Layout, 
    MultiField, 
    Reset,
    Submit, 
)
from crispy_forms.bootstrap import (
    InlineCheckboxes, 
    InlineRadios, 
)
    


 
def Hellper(self, *args, **kwargs):
        self.helper = FormHelper
        self.fields['header_about'].widget = RadioSelect()
        self.fields['header_about'].queryset = About.objects.all()

        


class ButtonLayout(Layout):
    def __init__(self, *args, **kwargs):
        super().__init__(
            Submit('save', 'Save', css_class = 'btngrp'),
            Reset('reset', 'Reset', css_class = 'btngrp')
        )



class NameContentLayout(Layout):
    def __init__(self, *args, **kwargs):
        super().__init__(
            Field('name', wrapper_class = 'it2'),
            Field('content', wrapper_class = 'it2'),
            Field('header_about', css_class = 'it3'),
        )



class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.title = 'About'
        
        # self.helper.add_input(Submit('save', 'Save'))
        self.helper.layout = Layout(
            NameContentLayout(),
            ButtonLayout()
        )
        


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ['summary']
        labels = {
            'post_date': l('Date'),
            'post_read': l('Number of visits'),
            'post_share': l('Times shared'),
            'heading': l('Headline'),
            'image_url': l('Image')
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Hellper(self)
        self.title = 'Blog'

        self.fields['author'].widget = RadioSelect()
        self.fields['author'].queryset = Teacher.objects.all()

        self.helper.layout = Layout(
            Field('heading', wrapper_class = 'it2'),
            Field('content', wrapper_class = 'it2'),
            Div(
                Field('post_date', wrapper_class = 'it1'),
                Field('post_read', wrapper_class = 'it1'),
                Field('post_share', wrapper_class = 'it1'),
                Field('post_comments', wrapper_class = 'it1'),
                Field('image_url', wrapper_class = 'it1'),
                css_class = 'first_div'
            ),
            Field('author', css_class = 'it3'),
            ButtonLayout()
        )


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        # fields = '__all__'
        exclude = ['funding', 'summary']
        labels = {
            'name': l('Course Name'),
            'content': l('About Course'),
            'c_length': l('Length'),
            'c_duration': l('Hours per week'),
            'c_requirement': l('Requirements'),
            'c_teacher': l('Teacher'),
            'c_school': l('Faculty'),
            'image_url': l('Image')
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Hellper(self)
        self.title = 'Course'

        self.fields['c_requirement'].widget = CheckboxSelectMultiple()
        self.fields['c_requirement'].queryset = Requirement.objects.all()

        self.helper.layout = Layout(
            NameContentLayout(),
            Div(
                Field('c_length', wrapper_class = 'it1'),
                Field('c_duration', wrapper_class = 'it1'),
                Field('c_teacher', wrapper_class = 'it1'),
                Field('c_school', wrapper_class = 'it1'),
                Field('fees', wrapper_class = 'it1'),
                Field('image_url', wrapper_class = 'it1'), 
                css_class = 'first_div'
            ),
                Field('c_requirement' , wrapper_class = 'cbox', css_class = 'it3'),
                ButtonLayout()
        )



class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['summary']
        labels = {
            'name': l('Event name'),
            'content': l('About the event'),
            'event_date': l('Date'),
            'event_time': l('Time'),
            'e_speaker': l('Speakers'),
            'image_url': l('Image')
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Hellper(self)
        # self.helper = FormHelper
        self.title = 'Event'

        self.fields['e_speaker'].widget = CheckboxSelectMultiple()
        self.fields['e_speaker'].queryset = Teacher.objects.all()

        self.helper.layout = Layout(
            NameContentLayout(),
            Div(
                Field('location', wrapper_class = 'it1'),
                Field('event_date', wrapper_class = 'it1'),
                Field('event_time', wrapper_class = 'it1'),
                Field('fee', wrapper_class = 'it1'),
                css_class = 'first_div'
            ),
            Field('image_url', wrapper_class = 'it1'), 
            Field('e_speaker', css_class = 'it3'),
            ButtonLayout()
        )


class FunFactForm(forms.ModelForm):
    class Meta:    
        model = FunFact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.title = 'Funfact'

        self.helper.layout = Layout(
            NameContentLayout(),
            Field('number', wrapper_class = 'it2'),
            ButtonLayout()
        )


class InterestForm(forms.ModelForm):
    class Meta:    
        model = Interest
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.title = 'Interest'

        self.helper.layout = Layout(
            NameContentLayout(),
            ButtonLayout()
        )

class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        exclude = ['summary']
        labels = {
            'name': l('Title'),
            'notice_date': l('Date')
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Hellper(self)
        self.title = 'Notice'

        self.helper.layout = Layout(
            NameContentLayout(),
            Field('notice_date', wrapper_class = 'it1'),
            ButtonLayout()
        )

class RequirementForm(forms.ModelForm):
    class Meta:
        model = Requirement
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.title = 'Requirement'

        self.helper.layout = Layout(
            NameContentLayout(),
            ButtonLayout()
        )

class ResearchForm(forms.ModelForm):
    class Meta:
        model = Research
        fields = '__all__'
        labels = {
            'summary': l('About the research'),
            'image_url': l('Image')
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Hellper(self)
        self.title = 'Research'

        self.helper.layout = Layout(
            NameContentLayout(),
            Field('summary', wrapper_class = 'it2'),
            Field('image_url', wrapper_class = 'it1'),
            ButtonLayout()
        )

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.title = 'School'

        self.helper.layout = Layout(
            NameContentLayout(),
            ButtonLayout()
        )

class ScholarshipForm(forms.ModelForm):
    class Meta:
        model = Scholarship
        exclude = ['summary']
        labels = {
            'image_url': l('Image'),
            # 'content': l('About scholarship'),
            's_course': l('Course'),
            's_requirement': l('Requirements')
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Hellper(self)
        self.title = 'Scholarship'

        self.fields['s_course'].widget = RadioSelect()
        self.fields['s_course'].queryset = Course.objects.all()

        self.fields['s_requirement'].widget = CheckboxSelectMultiple()
        self.fields['s_requirement'].queryset = Requirement.objects.all()

        self.helper.layout = Layout(
            NameContentLayout(),
            Field('s_course', css_class = 'it3'),
            Field('image_url', wrapper_class = 'it1'),
            Field('s_requirement', css_class = 'it3'),
            Submit('save', 'Save', css_class = 'btngrp'),
            Reset('reset', 'Reset', css_class = 'btngrp')
        )


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        exclude = ['summary']
        labels = {
            'content': l('Biography'),
            't_interest': l('Interests'),
            't_courses': l('Courses taught'),
            'image_url': l('Image')
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Hellper(self)
        self.title = 'Teacher'

        self.fields['t_interest'].widget = forms.CheckboxSelectMultiple()
        self.fields['t_interest'].queryset = Interest.objects.all()

        self.fields['t_courses'].widget = forms.CheckboxSelectMultiple()
        self.fields['t_courses'].queryset = Course.objects.all()
        
        self.helper.layout = Layout(
            NameContentLayout(),
            Field('education', wrapper_class = 'it2'),
            Div(
                Field('email', wrapper_class = 'it1'),
                Field('phone', wrapper_class = 'it1'),
                Field('social_media', wrapper_class = 'it1'),
                Field('address', wrapper_class = 'it1'),
                Field('image_url', wrapper_class = 'it1'),
                css_class = 'firstdiv'
            ),
            Field('t_interest', css_class = 'it3'),
            Field('t_courses', css_class = 'it3'),
            Submit('save', 'Save', css_class = 'btngrp'),
            Reset('reset', 'Reset', css_class = 'btngrp')
        )