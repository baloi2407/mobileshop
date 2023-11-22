from django.core.paginator import Paginator

def paginate_data(data, page_number=1):
    # Số lượng sản phẩm trên mỗi trang
    items_per_page = 10  # Bạn có thể thay đổi số này
    paginator = Paginator(data, items_per_page)
    page_obj = paginator.get_page(page_number)
    return page_obj