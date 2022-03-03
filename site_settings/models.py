from django.db import models




class SiteSettings(models.Model):
    site_name = models.CharField(max_length=200 , verbose_name='Site Name')
    site_url = models.CharField(max_length=200 , verbose_name='Site URL')
    site_address = models.CharField(max_length=300 , verbose_name='Site Address')
    site_phone = models.CharField(max_length=100 , null=True , blank=True , verbose_name='Site Phone')
    site_fax = models.CharField(max_length=200 , null=True , blank=True , verbose_name='Site Fax')
    site_email = models.EmailField(max_length=200 , null=True , blank=True , verbose_name='Site Email')
    about_us_text = models.TextField(verbose_name='About Us Text')
    site_copy_right = models.TextField(verbose_name='Copyright Text')
    site_logo = models.ImageField(upload_to='images/site-setting/' , verbose_name='Site Logo')
    is_main_setting = models.BooleanField(verbose_name='Site Main Settings')

    def __str__(self) -> str:
        super(SiteSettings , self).__str__()
        return self.site_name

    class Meta:
        verbose_name = 'Site Setting'
        verbose_name_plural = 'Site Settings'
        
        
        
        
        
class FooterLinkBox(models.Model):
    title = models.CharField(max_length=200 , verbose_name='Title')
    
    def __str__(self) -> str:
        super(FooterLinkBox , self).__str__()
        return self.title
    
    class Meta:
        verbose_name = 'Footer Link Setting'
        verbose_name_plural = 'Footer Link Settings'
        
        
 
        
        
class FooterLink(models.Model):
    title = models.CharField(max_length=200 , verbose_name='Title')
    url = models.URLField(max_length=500 , verbose_name='Links')
    footer_link_box = models.ForeignKey(to=FooterLinkBox , verbose_name='Category' , on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        super(FooterLink , self).__str__()
        return self.title
    
    class Meta:
        verbose_name = 'Footer Link'
        verbose_name_plural = 'Footer Links'
        
        
        
        
        
class Slider(models.Model):
    title = models.CharField(max_length=200 , verbose_name='Title')
    description = models.TextField(verbose_name='Slider Description')
    url_title = models.CharField(max_length=200 , verbose_name='URL Title')
    url = models.URLField(max_length=200 , verbose_name='URL Address')
    image = models.ImageField(upload_to='images/sliders' , verbose_name='Slider Image')
    is_active = models.BooleanField(default=False , verbose_name='Active / Inactive')
    
    def __str__(self) -> str:
        super(Slider , self).__str__()
        return self.title
    
    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliders'