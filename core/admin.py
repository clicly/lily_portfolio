from django.contrib import admin
from .models import *

# Register your models here.
# Home
admin.site.register(Home)

# About
class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    '''
        Admin View for About
    '''
    inlines = [
        ProfileInline,
    ]

class SkillInline(admin.TabularInline):
    '''
        Admin View for Skills
    '''
    model = Skill
    extra = 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''
        Admin View for
    '''
    inlines = [
        SkillInline,
    ]

admin.site.register(Portfolio)
admin.site.register(Certificate)
admin.site.register(Project)
admin.site.register(Language)
admin.site.register(Education)
