from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import (
    BlogCategoryModel,
    BlogTagModel,
    BlogAuthorModel,
    BlogModel,
    BlogCommentModel,
)

class MyTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(BlogCategoryModel)
class BlogCategoryAdmin(MyTranslationAdmin):
    list_display = ('title', 'parent', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('parent',)
    ordering = ('title',)



@admin.register(BlogTagModel)
class BlogTagAdmin(MyTranslationAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)



@admin.register(BlogAuthorModel)
class BlogAuthorAdmin(MyTranslationAdmin):
    list_display = ('get_full_name', 'avatar', 'created_at', 'updated_at')
    search_fields = ('first_name', 'last_name')
    ordering = ('first_name', 'last_name')



@admin.register(BlogModel)
class BlogAdmin(MyTranslationAdmin):
    list_display = ('title',  'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('categories', 'author')
    filter_horizontal = ('categories', 'author')




@admin.register(BlogCommentModel)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment', 'created_at', 'updated_at')
    search_fields = ('user__username', 'comment')
    list_filter = ('user',)
