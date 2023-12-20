from . generate import generate_random_filename

def upload_to_brand(instance, filename):
        return generate_random_filename(instance, filename, 'brand')
def upload_to_product(instance, filename):
        return generate_random_filename(instance, filename, 'product')
def upload_to_category(instance, filename):
        return generate_random_filename(instance, filename, 'category')
def upload_to_news(instance, filename):
        return generate_random_filename(instance, filename, 'news')
def upload_to_avatar(instance, filename):
        return generate_random_filename(instance, filename, 'avatar')
def upload_to_news_category(instance, filename):
        return generate_random_filename(instance, filename, 'news_category')
def upload_to_supplier(instance, filename):
        return generate_random_filename(instance, filename, 'supplier')
def upload_to_about(instance, filename):
        return generate_random_filename(instance, filename, 'about')
