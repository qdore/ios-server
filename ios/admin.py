from django.contrib import admin

# Register your models here.
from ios.models import user

class UserAdmin(admin.ModelAdmin):
    list_display = ('tel',)
    search_fields = ('tel',)

admin.site.register(user.Users, UserAdmin)

#admin.site.register(home_page.HomePage)
#admin.site.register(about_fumeng.AboutFumeng)
#admin.site.register(company_culture.CompanyCulture)
#admin.site.register(contact_us.ContactUs)
#admin.site.register(social_ability.SocialAbility)
#
#
#class NewsAdmin(admin.ModelAdmin):
#    list_display = ('title', 'news_type')
#    search_fields = ('title',)
#    list_filter = ('news_type',)
#
#admin.site.register(news.News, NewsAdmin)
#admin.site.register(fumeng_business.FumengBusiness, NewsAdmin)
#admin.site.register(human_resources.HumanResource)
#
#class ImageAdmin(admin.ModelAdmin):
#    list_display = ('image', )
#    search_field = ('image', )
#admin.site.register(upload_image.UploadImage, ImageAdmin)
