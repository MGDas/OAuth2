from django.shortcuts import render
import vk


def index(request):

    context = {}
    if request.user.is_authenticated:
        social = request.user.social_auth.get(provider='vk-oauth2')
        access_token = social.extra_data.get('access_token')
        session = vk.Session(access_token=access_token)
        vkapi = vk.API(session)

        friends = vkapi.friends.get(
            order='random',
            count=5,
            fields=[
                'domain', 'first_name', 'last_name'
                ], v=92
            )
            context.update({'friends': friends})
    return render(request, 'vkauth/index.html', context)
