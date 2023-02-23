from django.contrib import admin

from demo_app.models import Demo


@admin.register(Demo)
class DemoAdmin(admin.ModelAdmin):
    pass
