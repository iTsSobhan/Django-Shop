from django import forms
from .models import ContactUs




class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['fullname' , 'email' , 'title' , 'message']
        widgets = {
            'fullname':forms.TextInput(attrs={
                'class':'form-control' ,
                'placeholder':'نام و نام خانوادگی'
            }) ,
            'email':forms.EmailInput(attrs={
                'class':'form-control' ,
                'placeholder':'ایمیل'
            }) ,
            'title':forms.TextInput(attrs={
                'class':'form-control' ,
                'placeholder':'عنوان'
            }) ,
            'message':forms.Textarea(attrs={
                'class':'form-control' ,
                'placeholder':'متن پیام' ,
                'rows':5 ,
                'id':'message'
            })
        }
        labels = {
            'fullname':'نام و نام خانوادگی' ,
            'email':'ایمیل' ,
            'title':'عنوان' ,
            'message':'متن پیام'
        }
        error_messages = {
            'fullname':{'required':'لطفا نام و نام خانوادگی خود را وارد کنید'} ,
            'email':{'required':'لطفا ایمیل خود را وارد کنید'} ,
            'title':{'required':'لطفا عنوان را وارد کنید'} ,
            'message':{'required':'لطفا متن پیام را وارد کنید'}
        }





# class ProfileForm(forms.Form):
#     user_image = forms.ImageField()