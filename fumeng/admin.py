from django.contrib import admin

# Register your models here.
from fumeng.models import about_fumeng
from fumeng.models import company_culture
from fumeng.models import contact_us
from fumeng.models import fumeng_business
from fumeng.models import home_page
from fumeng.models import social_ability
from fumeng.models import news

admin.site.register(home_page.HomePage)
admin.site.register(about_fumeng.AboutFumeng)
admin.site.register(company_culture.CompanyCulture)
admin.site.register(contact_us.ContactUs)
admin.site.register(fumeng_business.FumengBusiness)
admin.site.register(social_ability.SocialAbility)
admin.site.register(news.News)
