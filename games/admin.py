from django.contrib import admin

from games.models import ActiveHero, Game

class ActiveHeroInline(admin.TabularInline):
    model = ActiveHero


class GameAdmin(admin.ModelAdmin):
    inlines = [
        ActiveHeroInline,
    ]


admin.site.register(ActiveHero)
admin.site.register(Game, GameAdmin)
