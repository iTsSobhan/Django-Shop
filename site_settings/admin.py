from django.contrib import admin
from .models import (SiteSettings , FooterLinkBox , FooterLink , Slider)




class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ['title' , 'url']
    


class SliderAdmin(admin.ModelAdmin):
    list_display = ['title' , 'url' , 'is_active']
    list_editable = ['url' , 'is_active']




admin.site.register(SiteSettings)
admin.site.register(FooterLinkBox)
admin.site.register(FooterLink , FooterLinkAdmin)
admin.site.register(Slider , SliderAdmin)