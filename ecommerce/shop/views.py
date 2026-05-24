from django.shortcuts import render, redirect

default_products = [
    {
        'name': "Laptop",
        'price': 1299,
        'category': "Electronics",
        'rating': 4.5,
        'image': "https://picsum.photos/seed/laptop/400/300"
    },
    {
        'name': "Wireless Headphone",
        'price': 999,
        'category': "Electronics",
        'rating': 4.2,
        'image': "https://picsum.photos/seed/headphone/400/300"
    }
]

def home(request):
    session_products = request.session.get('products', [])
    products = default_products + session_products

    return render(request, "home.html", {
        'products': products
    })

def add_product(request):
    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        category = request.POST.get('category')
        rating = request.POST.get('rating')
        image = request.POST.get('image')

        new_product = {
            'name': name,
            'price': price,
            'category': category,
            'rating': rating,
            'image': image
        }

        session_products = request.session.get('products', [])
        session_products.append(new_product)

        request.session['products'] = session_products
        request.session.modified = True

        return redirect('home')

    return render(request, 'add_product.html')