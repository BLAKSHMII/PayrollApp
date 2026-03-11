from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Document

class DocumentAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'employee_name',
        'document_type',
        'document_number',
        'status',
        'uploaded_at'
    )

    list_filter = ('document_type', 'status')

    search_fields = ('employee_name', 'document_number')

admin.site.register(Document, DocumentAdmin)