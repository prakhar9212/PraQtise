from django.contrib import admin

from .models import total
# Register your models here.


class totalAdmin(admin.ModelAdmin):
    class Meta:
        model=total

admin.site.register(total,totalAdmin)
