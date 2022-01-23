from django.http import HttpResponse
from django.views import View


class Index(View):
    def get(self, request):
        print(self, request)
        return HttpResponse("hello GET request...")

    def post(self, request):
        print(self, request)
        return HttpResponse("hello POST request...")

    def put(self, request):
        print(self, request)
        return HttpResponse("hello PUT request...")

    def delete(self, request):
        print(self, request)
        return HttpResponse("hello delete request...")
