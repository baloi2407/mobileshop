# Trong file signals.py trong ứng dụng warehouse

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Warehouse_Payment, Warehouse_Product
from django.db import transaction
@receiver(post_save, sender=Warehouse_Payment)
def update_warehouse_product_quantity(sender, instance, created, **kwargs):
    if created:  # Chỉ thực hiện khi một đối tượng mới được tạo
        prod = instance.prod
        quantity = instance.quantity

        if prod:
            with transaction.atomic():
                # Cập nhật số lượng sản phẩm trong bảng Product
                prod.quantity += quantity
                prod.save()

                # Tạo mới các bản ghi trong bảng Warehouse_Product
                for _ in range(quantity):
                    Warehouse_Product.objects.create(
                        prod=prod,
                        supplier=instance.supplier,
                        note="New product added from warehouse payment",
                        paid='Not sell',
                        status='Active'
                    )
