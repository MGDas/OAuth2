from django.shortcuts import render
# import vk


def index_oauth(request):
    return render(request, 'vkauth/index.html')
