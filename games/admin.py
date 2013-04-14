from django.contrib import admin

from games.models import ActiveHero, Game

class ActiveHeroInline(admin.TabularInline):
    model = ActiveHero


class GameAdmin(admin.ModelAdmin):
    list_display = ('profile', 'pk', 'created_at',)
    inlines = [
        ActiveHeroInline,
    ]


admin.site.register(ActiveHero)
admin.site.register(Game, GameAdmin)
