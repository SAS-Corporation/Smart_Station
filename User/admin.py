from django.contrib import admin
from User import models as user_models


# Registering the CustomUser model in the admin panel
admin.site.register(user_models.CustomUser)
admin.site.register(user_models.EmailVerification)