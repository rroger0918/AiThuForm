from django.contrib import admin
from .models import student

# Register your models here.
class studentAdmin(admin.ModelAdmin):
    # 第三種方式，加入 ModelAdmin 類別，定義顯示欄位、欄位過濾資料、搜尋和排序
	list_display=('id','cName','cPhone','cAddr')
	list_filter=('cName','cPhone')
	search_fields=('cName',)
	ordering=('id',)
	
admin.site.register(student,studentAdmin)