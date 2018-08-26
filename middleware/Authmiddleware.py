from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin


class Authware(MiddlewareMixin):
    def process_request(self,request):
        auths = request.session.get('auths')
        path = request.path #
        print(auths)
        print(path)

        commstr = '/login/','/regist/','/yzcode/'



        shopcarstr = '/addshopcar/','/subshopcar/','/selshopcar/'

        name = request.session.get('mname')

        if (not name) and (path in shopcarstr):
            # return render(request,'login.html')
            return JsonResponse({'result':'0001'})

        if (not path in commstr) and (not path in auths):
            return HttpResponse('你没有权限')


