from django.db import models



class ContactUs(models.Model):
    title = models.CharField(max_length=300 , verbose_name="title")
    email = models.EmailField(max_length=300 , verbose_name="email")
    fullname = models.CharField(max_length=300 , verbose_name="full name")
    message = models.TextField(verbose_name="message")
    created_at = models.DateTimeField(verbose_name="Created at" , auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at" , auto_now=True)
    response = models.TextField(verbose_name="admin's Response" , null= True , blank=True)
    is_read_by_admin = models.BooleanField(verbose_name="read by admin" , default=False)

    def __str__(self) -> str:
        super(ContactUs , self).__str__()
        return self.fullname

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "List of Contacts"




class UserProfile(models.Model):
    image = models.ImageField(upload_to='images')