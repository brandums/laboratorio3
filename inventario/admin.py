from django.contrib import admin
from . models import Categoria, Usuario
from . models import Producto
from . models import Pedido
from . models import PedidoProducto


class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "precio", "unidades")
    ordering = ["precio"]
    search_fields = ["nombre"]

admin.site.register(Categoria)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Pedido)
admin.site.register(PedidoProducto)
admin.site.register(Usuario)
# Register your models here.
