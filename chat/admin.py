from django.contrib import admin
from django import forms
from chat.models import Message


class MessageAdmin(admin.ModelAdmin):
	list_display = ('text', 'author', 'file', 'time')
	list_filter = ('author', 'time')
	search_fields = ('text', 'author')
	readonly_fields = ('time',)
	fieldsets = (
		(None, {
			'fields': ('text', 'author', 'file', 'time')
		}),
	)

class MessageAdminForm(forms.ModelForm):
	class Meta:
		model = Message
		fields = '__all__'
		widgets = {
			'text': forms.Textarea(attrs={'rows': 3}),
		}

admin.site.register(Message, MessageAdmin)
