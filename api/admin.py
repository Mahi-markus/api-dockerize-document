from django.contrib import admin
from .models import HelloWorld

class HelloWorldAdmin(admin.ModelAdmin):
    # Display the 'id' and 'message' fields in the admin list view
    list_display = ('id', 'message')
    
    # Enable search functionality for the 'message' field
    search_fields = ('message',)
    
    # Enable filtering based on the 'message' field
    list_filter = ('message',)

# Register the HelloWorld model with the custom admin configuration
admin.site.register(HelloWorld, HelloWorldAdmin)
