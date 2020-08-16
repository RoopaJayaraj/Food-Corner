from  menu.models import Category

def get_category_to_context(request):
    category = Category.objects.all()
    return({'category':category})
