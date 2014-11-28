from django.contrib import admin
from web.models import Scenario,Library


class LibraryAdmin(admin.ModelAdmin):
    list_display = ['ref', 'added_on']

admin.site.register(Library, LibraryAdmin)

class ScenarioAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Scenario, ScenarioAdmin)