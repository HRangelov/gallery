from django.contrib import admin

from paintings.models import Painting, Like, Comment


class LikeInline(admin.TabularInline):
    model = Like


class PaintingAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'name', 'year')
    list_filter = ('type', 'year')
    inlines = (
        LikeInline,
    )


admin.site.register(Painting, PaintingAdmin)
admin.site.register(Comment)
admin.site.register(Like)