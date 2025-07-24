def cart_count(request):
    count = 0
    if request.user.is_authenticated:
        cart = getattr(request.user, 'cart', None)
        if cart:
            count = cart.items.count()
    return {'cart_count': count}