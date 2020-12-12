from django.contrib import admin

from paintings.models import Painting, Like, Comment


class LikeInline(admin.TabularInline):
    model = Like


class PaintingAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'name', )
    list_filter = ('type', )
    inlines = (
        LikeInline,
    )



admin.site.register(Painting, PaintingAdmin)
admin.site.register(Comment)
admin.site.register(Like)