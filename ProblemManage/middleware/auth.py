from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect, render

class AuthMiddleWare(MiddlewareMixin):
    """中间键1"""
    def process_request(self, request):
        # 如果没有返回值，则可以继续往后走
        # 如果有返回值，则去到返回值的网站(一般默认返回值都是一个网站)
        obj = request.session.get("info")
        # if not obj:
        # 会发现如果返回登陆界面，则会陷入死循环，需要加特判
        # return redirect("/account/login/")

        # 排除那些不需要登录就能访问的页面
        if request.path_info in ["/account/login/", "/account/img/", ]:
            return
        else:
            if not obj:
                return redirect("/account/login/")
            else:
                return


    def process_response(self, request, response):
        # print("M1 out")
        return response

