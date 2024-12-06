from django.contrib import admin
from agriapp.models import Contact, Admin, Register_courses, Farmers, Customers, ImageModel

# Register your models here.
admin.site.register(Contact)
admin.site.register(Admin)
admin.site.register(Register_courses)
admin.site.register(Farmers)
admin.site.register(Customers)
admin.site.register(ImageModel)


