from django.shortcuts import render

posts = [
    {'id': 1, 'title': 'First Post', 'content': 'Hello World!'},
    {'id': 2, 'title': 'Second Post', 'content': 'Learning Django!'}
]


def index(request):
    return render(request, 'index.html', {'posts': posts})



def post_detail(request, id):
    post = next(
        (post for post in posts if post['id'] == id),
        None
    )
    return render(request, 'detail.html', {'post': post})


def category_posts(request, category_slug):
    return render(request, 'category.html', {'category_slug': category_slug})
