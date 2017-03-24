# pylint: disable=too-many-public-methods
# pylint: disable=no-member
"""
django admin pages for organization models
"""
from django.contrib import admin
from organizations.models import (Organization, OrganizationCourse, OrganizationUser)


class OrganizationAdmin(admin.ModelAdmin):
    """
    Admin for the Organization table.
    soft-delete on the organizations
    """
    list_display = ('name', 'short_name', 'logo', 'created', 'active', 'apiKey')
    readonly_fields = ('created',)
    ordering = ['created']
    actions = ['activate_selected', 'deactivate_selected']

    def get_actions(self, request):
        """ return actions """
        actions = super(OrganizationAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def activate_selected(self, request, queryset):
        """activate the selected entries"""
        queryset.update(active=True)
        if queryset.count() == 1:
            message_bit = "1 organization entry was"
        else:
            message_bit = "%s organization entries were" % queryset.count()
        self.message_user(request, "%s successfully activated." % message_bit)

    def deactivate_selected(self, request, queryset):
        """deactivate the selected entries"""
        queryset.update(active=False)
        if queryset.count() == 1:
            message_bit = "1 organization entry was"
        else:
            message_bit = "%s organization entries were" % queryset.count()
        self.message_user(request, "%s successfully deactivated." % message_bit)

    deactivate_selected.short_description = "Deactivate s selected entries"
    activate_selected.short_description = "Activate s selected entries"


class OrganizationCourseAdmin(admin.ModelAdmin):
    """
    Admin for the OrganizationCourse table.
    """
    list_display = ('course_id', 'organization', 'active')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """
        list down the active organizations
        """
        if db_field.name == 'organization':
            kwargs['queryset'] = Organization.objects.filter(active=True)

        return super(OrganizationCourseAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


class OrganizationUserAdmin(admin.ModelAdmin):
    """
    Admin for the OrganizationUser table.
    """
    list_display = ('user_id', 'organization', 'active', 'is_staff')

    raw_id_fields = ('user_id',)
    search_fields = ('user__username',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """
        list down the active organizations
        """
        if db_field.name == 'organization':
            kwargs['queryset'] = Organization.objects.filter(active=True)

        return super(OrganizationUserAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(OrganizationCourse, OrganizationCourseAdmin)
admin.site.register(OrganizationUser, OrganizationUserAdmin)