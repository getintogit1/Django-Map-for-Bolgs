from django.contrib import admin
from .models        import Attraction

class AttractionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Attraction, AttractionAdmin)
