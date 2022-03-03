from django import forms
from django.core import validators
from django.core.exceptions import ValidationError




class RegisterForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={
            'placeholder':' ایمیل خود را وارد کنید'
        }),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ],
        error_messages={
            'required':'لطفا ایمیل خود را وارد کنید',
            'max_length':'ایمیل نمیتواند بیشتر از 100 کرکتر باشد'
        }
    )

    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(attrs={
            'placeholder':'کلمه عبور خود را وارد کنید'
        }),
        validators=[
            validators.MinLengthValidator(8),
            validators.MaxLengthValidator(50)
        ],
        error_messages={
            'required':'لطفا کلمه عبور خود را وارد کنید',
            'max_length':'کلمه عبور نمیتواند بیشتر از 100 کرکتر باشد',
            'min_length':'کلمه عبور نمیتواند کمتر از 8 کرکتر باشد'
        }
    )

    confirm_password = forms.CharField(
        label='تایید کلمه عبور',
        widget=forms.PasswordInput(attrs={
            'placeholder':'کلمه عبور خود را تایید کنید'
        }),
        validators=[
            validators.MinLengthValidator(8),
            validators.MaxLengthValidator(50)
        ],
        error_messages={
            'required':'لطفا کلمه عبور خود را دوباره وارد کنید',
            'max_length':'تکرار کلمه عبور نمیتواند بیشتر از 100 کرکتر باشد',
            'min_length':'تکرار کلمه عبور نمیتواند کمتر از 8 کرکتر باشد'
        }
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if (password == confirm_password):
            return confirm_password
        raise ValidationError('پسورد ها مطابقت ندارند')





class LoginForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={
            'placeholder':'ایمیل خود را وارد کنید'
        }),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ],
        error_messages={
            'required':'لطفا ایمیل خود را وارد کنید',
            'max_length':'ایمیل نمیتواند بیشتر از 100 کرکتر باشد'
        }
    )

    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(attrs={
            'placeholder':'کلمه عبور خود را وارد کنید'
        }),
        validators=[
            validators.MinLengthValidator(8),
            validators.MaxLengthValidator(50)
        ],
        error_messages={
            'required':'لطفا کلمه عبور خود را وارد کنید',
            'max_length':'کلمه عبور نمیتواند بیشتر از 100 کرکتر باشد',
            'min_length':'کلمه عبور نمیتواند کمتر از 8 کرکتر باشد'
        }
    )





class ForgetPasswordForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={
            'placeholder':'ایمیل خود را برای بازیابی وارد کنید'
        }),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )





class ResetPasswordForm(forms.Form):
    password = forms.CharField(
        label=' کلمه عبور جدید',
        widget=forms.PasswordInput(attrs={
            'placeholder':'کلمه عبور جدید خود را وارد کنید'
        }),
        validators=[
            validators.MinLengthValidator(8),
            validators.MaxLengthValidator(50)
        ],
        error_messages={
            'required':'لطفا کلمه عبور جدید خود را وارد کنید',
            'max_length':'کلمه عبور جدید نمیتواند بیشتر از 100 کرکتر باشد',
            'min_length':'کلمه عبور جدید نمیتواند کمتر از 8 کرکتر باشد'
        }
    )

    confirm_password = forms.CharField(
        label='تایید کلمه عبور جدید',
        widget=forms.PasswordInput(attrs={
            'placeholder':'کلمه عبور جدید خود را تایید کنید'
        }),
        validators=[
            validators.MinLengthValidator(8),
            validators.MaxLengthValidator(50)
        ],
        error_messages={
            'required':'لطفا  کلمه عبور جدید خود را دوباره وارد کنید',
            'max_length':'تکرار  کلمه عبور جدید نمیتواند بیشتر از 100 کرکتر باشد',
            'min_length':'تکرار  کلمه عبور جدید نمیتواند کمتر از 8 کرکتر باشد'
        }
    )