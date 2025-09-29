from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import TelegramUsers, AnonymFeedbackModel, IdentifiedFeedbackModel

admin.site.site_header = "Lumos School Feedback"
admin.site.site_title = "Lumos School Admin Portal"
admin.site.index_title = "Welcome to Lumos School Portal"
admin.site.unregister(Group)
admin.site.unregister(User)

class TelegramUsersAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'username', 'telegram_id')
    list_display_links = ('full_name', 'username', 'telegram_id')
    search_fields = ('full_name', 'telegram_id')

admin.site.register(TelegramUsers, TelegramUsersAdmin)

class AnonymFeedbackModelAdmin(admin.ModelAdmin):
    list_display = ('short_feedback', 'status')
    list_display_links = ('short_feedback', 'status')
    fields = ('feedback', 'status')
    def short_feedback(self, obj):
        return obj.feedback[:50] + ("..." if len(obj.feedback) > 50 else "")
    short_feedback.short_description = "Feedback"
admin.site.register(AnonymFeedbackModel, AnonymFeedbackModelAdmin)

class IdentifiedFeedbackModelAdmin(admin.ModelAdmin):
    list_display = ('short_feedback', 'full_name', 'telegram_id', 'status')
    list_display_links = ('short_feedback', 'full_name', 'telegram_id', 'status')
    def short_feedback(self, obj):
        return obj.feedback[:50] + ("..." if len(obj.feedback) > 50 else "")
    short_feedback.short_description = "Feedback"
admin.site.register(IdentifiedFeedbackModel, IdentifiedFeedbackModelAdmin)
