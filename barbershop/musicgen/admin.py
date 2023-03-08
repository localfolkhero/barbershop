from django.contrib import admin

from .models import MusicScoreRecord
# Register your models here.

@admin.register(MusicScoreRecord)
class MusicScoreRecordAdmin(admin.ModelAdmin):
    list_display = ('slug', 'owner', 'name', 'created')