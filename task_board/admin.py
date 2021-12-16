from django.contrib import admin

from .models import *


admin.site.register(UserList)
admin.site.register(UserLevel)
admin.site.register(Specialist)
admin.site.register(Contractor)
admin.site.register(MallList)
admin.site.register(UserMall)
admin.site.register(TaskInWork)

