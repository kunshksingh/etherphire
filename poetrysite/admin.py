from django.contrib import admin

from .models import Poems

class PoemAdmin(admin.ModelAdmin):
    list_display = ['poem_name', 'poem', 'tags']
    # whatever you want in your admin panel like filter, search and ...

admin.site.register(Poems, PoemAdmin)