from django.utils.html import format_html

class Mixins:
    
    
    def display_image(self, obj):
        if obj.image:
            image_url = obj.image.url
            return format_html('<img src="{}" style="max-width: 100px; max-height: 100px;" />', image_url)
        else:
            return "No image available"

    display_image.short_description = 'Image'

    def formatted_price(self, obj):
        price = obj.price
        formatted_price = f'{price}$'
        return formatted_price
    formatted_price.short_description = 'Price'

    def formatted_discount(self, obj):
        discount = obj.discount
        formatted_discount = f'{discount}%'
        return formatted_discount
    formatted_discount.short_description = 'Discount'

    def make_active(self, request, queryset):
        queryset.update(status='Active')
        for obj in queryset:
            obj.save()

    make_active.short_description = "Set selected brands as Active"

    def make_block(self, request, queryset):
        queryset.update(status='Block')
        for obj in queryset:
            obj.save()

    make_block.short_description = "Set selected brands as Block"
    