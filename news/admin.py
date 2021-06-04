from django.contrib import admin

# Register your models here.
from .models import dailyhighlights, trendingnews


# admin.site.register(post)


class dailyhighlightsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(dailyhighlights, dailyhighlightsAdmin)


class trendingnewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(trendingnews, trendingnewsAdmin)