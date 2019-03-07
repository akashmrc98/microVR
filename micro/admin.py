from django.contrib import admin
from .models import Zuke_User, Zuke_Subscribed, Videos, User_Filters, Issue



class Issue_Admin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "issue"
    )

class Video_Admin(admin.ModelAdmin):
    list_display = (
        "video_id",
        "video_title",
        "genere",
        "vtype",
        "contents",
        "label",
    )

class User_Admin(admin.ModelAdmin):
    list_display = (
        "user_id",
        "name",
        "dob",
        "sex",
        "phone",
        "email",
    )

admin.site.register(Zuke_User, User_Admin)
admin.site.register(Zuke_Subscribed)
admin.site.register(Videos, Video_Admin)
admin.site.register(Issue, Issue_Admin)
admin.site.site_header = 'Micro Videos'
admin.site.site_title = 'Micro Videos'