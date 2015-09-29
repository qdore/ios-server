#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
from django.http import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('tel', 'user_id', 'name', 'gender')
    search_fields = ('tel', 'user_id', 'name')

admin.site.register(user.Users, UserAdmin)

class StatusAdmin(admin.ModelAdmin):
    list_display = ('tel', 'brief')
    search_fields = ('tel',)

admin.site.register(status.Status, StatusAdmin)

class PraiseAdmin(admin.ModelAdmin):
    list_display = ('status_id', 'tel')
    search_fields = ('status_id', 'tel')

admin.site.register(praise_status.PraiseStatus, PraiseAdmin)

admin.site.register(status_pic.StatusPics)

class AttentAdmin(admin.ModelAdmin):
    list_display = ('attent_tel', 'tel_by_attent')
    search_fields = ('attent_tel', 'tel_by_attent')

admin.site.register(attention_relation.AttentionRelation, AttentAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('commenter', 'comment_by','comment_content')
    search_fields = ('commenter', 'comment_by','comment_content')

admin.site.register(comment.Comment, CommentAdmin)

class CharAdmin(admin.ModelAdmin):
    list_display = ('sender', 'reciver', 'content', 'readed', 'send_time')
    search_fields = ('sender', 'reciver', 'content', 'readed')

admin.site.register(chat.Chat, CharAdmin)

def export_xls(modeladmin, request, queryset):
    import xlwt
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=mymodel.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet(u"工作表")
    row_num = 0
    columns = [
        (u"ID", 2000),
        (u"Title", 6000),
        (u"Description", 8000),
    ]
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    for col_num in xrange(len(columns)):
        ws.write(row_num, col_num, columns[col_num][0], font_style)
        ws.col(col_num).width = columns[col_num][1]
    font_style = xlwt.XFStyle()
    font_style.alignment.wrap = 1
    print queryset[0].id
    for obj in queryset:
        row_num += 1
        row = [
            obj.id,
            obj.title,
            obj.position,
        ]
        for col_num in xrange(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)
    return response

export_xls.short_description = u"导出Excel表"

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'position', 'time', 'user_time', 'appliers', 'approve_applier')
    list_filter = ('title', 'time', 'user_time', 'approve_applier', 'status')
    search_fields = ('title',)
    actions = [export_xls]

admin.site.register(job.Job, JobAdmin)

class ApplyOutAdmin(admin.ModelAdmin):
    list_display = ('tel','start_time','end_time','reason')
    search_fields = ('tel','start_time','end_time','reason')
    list_filter = ('tel','start_time','end_time','reason')

admin.site.register(apply_out.ApplyOut, ApplyOutAdmin)

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
