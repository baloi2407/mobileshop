def paginate_data(queryset, page, items_per_page=10):
    total_items = queryset.count()
    total_pages = (total_items + items_per_page - 1) // items_per_page
    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page
    data = queryset[start_index:end_index]
    return data, total_pages