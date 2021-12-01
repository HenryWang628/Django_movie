from django.contrib import admin
from .models import Movie
from .models import Grade
from .models import Genre
from .models import Region
from .models import Language

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name','duration','grade')

admin.site.register(Movie, MovieAdmin)
admin.site.register(Grade)
admin.site.register(Genre)
admin.site.register(Region)
admin.site.register(Language)