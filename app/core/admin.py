from django.utils.translation import gettext as _
...

fieldsets = (
    (None, {'fields': ('email', 'password')}),
    (_('Personal Info'), {'fields': ('name',)}),
    (
        _('Permissions'),
        {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }
    ),
    (_('Important dates'), {'fields': ('last_login',)}),
)
