from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render

# request: HttpRequest
def index(request):
    request.session.set_test_cookie()
    category_list = Category.objects   
    page_list = Page.objects
    context_dict = {'categories': category_list, 'pages': page_list}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    print(request.session['visits'])
    response = render(request, 'orchestra/index.html', context = context_dict)
    return response

def about(request):
    return HttpResponse("Here is an about page.")