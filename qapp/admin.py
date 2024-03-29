from django.contrib import admin
from qapp.models import Photo, Profile, Comments, Flag, Block

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'poster', 'visible')
    date_hierarchy = 'timestamp'
admin.site.register(Photo, PhotoAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('created', 'deviceUUID')
admin.site.register(Profile, ProfileAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'poster', 'comment')
admin.site.register(Comments, CommentAdmin)

class FlagAdmin(admin.ModelAdmin):
    list_display = ('photourl', 'photospecs', 'userurl', 'flagger')
admin.site.register(Flag, FlagAdmin)

class BlockAdmin(admin.ModelAdmin):
    pass
admin.site.register(Block, BlockAdmin)
