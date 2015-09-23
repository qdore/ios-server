from django.contrib import admin

# Register your models here.
from ios.models import user
from ios.models import status
from ios.models import praise_status
from ios.models import status_pic
from ios.models import attention_relation
from ios.models import chat
from ios.models import comment
from ios.models import job
from ios.models import apply_out

class UserAdmin(admin.ModelAdmin):
    list_display = ('tel', 'user_id', 'name', 'gender')
    search_fields = ('tel', 'user_id', 'name')

admin.site.register(user.Users, UserAdmin)

class StatusAdmin(admin.ModelAdmin):
    list_display = ('tel', 'brief')
    search_fields = ('tel',)

admin.site.register(status.Status, StatusAdmin)
admin.site.register(praise_status.PraiseStatus)
admin.site.register(status_pic.StatusPics)
admin.site.register(attention_relation.AttentionRelation)
admin.site.register(comment.Comment)

class CharAdmin(admin.ModelAdmin):
    list_display = ('sender', 'reciver', 'content', 'readed')
    search_fields = ('sender', 'reciver', 'content', 'readed')

admin.site.register(chat.Chat, CharAdmin)

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'position', 'sponsor_name')
    search_fields = ('title', 'position', 'sponsor_name')

admin.site.register(job.Job, JobAdmin)
admin.site.register(apply_out.ApplyOut)

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
