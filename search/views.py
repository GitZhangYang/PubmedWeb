from django.shortcuts import render
from django.views.generic.base import View  # 基础的View类，让其他View继承于他，可以不用对POST或GET访问方式做判断


# def indexView(request):
#     return render(request, 'home.html')
class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')
