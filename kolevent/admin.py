from django.contrib import admin
from kolevent.views import *
from kolevent.models import *


class sliderAdmin(admin.ModelAdmin):
    list_display = ['slidername', 'id']

class compAdmin(admin.ModelAdmin):
    list_display = ['companyname', 'companylogo']

class aboutusAdmin(admin.ModelAdmin):
    list_display = ['aboutustitle']
        

class homeAdmin(admin.ModelAdmin):
    display = ['image', 'content']
    
class logoAdmin(admin.ModelAdmin):
    display = ['image']

class servicesAdmin(admin.ModelAdmin):
    list_display = ['servicename']
    
class newsAdmin(admin.ModelAdmin):
    list_display = ['newsnme']
    
    
class albumAdmin(admin.ModelAdmin):
    list_display = ['albumname']
    
class tourAdmin(admin.ModelAdmin):
    display = ['name', 'image', 'content', 'date']
    
    
class galleryAdmin(admin.ModelAdmin):
    list_display = ['galleryname']
    
class twitAdmin(admin.ModelAdmin):
    display = ['image']
    
class videoAdmin(admin.ModelAdmin):
    list_display = ['videoname']

class promotionAdmin(admin.ModelAdmin):
    list_display = ['promotionname']
        
    


    
    

    

admin.site.register(video, videoAdmin)
admin.site.register(slider, sliderAdmin)
admin.site.register(twit, twitAdmin)
admin.site.register(comp, compAdmin)
admin.site.register(aboutus, aboutusAdmin)
admin.site.register(home, homeAdmin) 
admin.site.register(logo, logoAdmin)   
admin.site.register(services, servicesAdmin)
admin.site.register(news, newsAdmin)
admin.site.register(album, albumAdmin)
admin.site.register(tour, tourAdmin)
admin.site.register(gallery, galleryAdmin)
admin.site.register(promotion, promotionAdmin)
