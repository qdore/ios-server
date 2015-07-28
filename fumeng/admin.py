from django.contrib import admin

# Register your models here.
from fumeng.models import about_fumeng
from fumeng.models import company_culture
from fumeng.models import contact_us
from fumeng.models import fumeng_business
from fumeng.models import home_page
from fumeng.models import social_ability
from fumeng.models import news
from fumeng.models import human_resources
from fumeng.models import upload_image

admin.site.register(home_page.HomePage)
admin.site.register(about_fumeng.AboutFumeng)
admin.site.register(company_culture.CompanyCulture)
admin.site.register(contact_us.ContactUs)
admin.site.register(social_ability.SocialAbility)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'news_type')
    search_fields = ('title',)
    list_filter = ('news_type',)

admin.site.register(news.News, NewsAdmin)
admin.site.register(fumeng_business.FumengBusiness, NewsAdmin)
admin.site.register(human_resources.HumanResource)

class ImageAdmin(admin.ModelAdmin):
    list_display = ('image', )
    search_field = ('image', )
admin.site.register(upload_image.UploadImage, ImageAdmin)
