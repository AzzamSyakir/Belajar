from django.http import JsonResponse
from django.shortcuts import render
from django.template import RequestContext
from httplib2 import Response
from app.models import user, book
import json
from django.views.decorators.csrf import csrf_exempt

class User:

        @csrf_exempt
        def register(request):
                try:
                        data = request.POST
                        mydata=json.loads(request.body)
                        name = mydata.get("username")
                        model = user.objects.create(username=name)
                        return JsonResponse({"status":name}, safe=False)
                except:
                        return JsonResponse({"error" : "error"}, safe=False)

        @csrf_exempt
        def getdata(request):
                try:
                        data = request.GET
                        model= user.objects.all()
                        return JsonResponse({"success":model}, safe=False)
                except:
                        return JsonResponse({"error":"error"}, safe=False);

        @csrf_exempt
        def login(request):
                try:
                        request.POST
                        data=json.loads(request.body)
                        name=data
                        model = user.objects.filter('username')
                        if name == model:
                                return JsonResponse({"success":"login berhasil"}, safe=False)
                        else:
                                return JsonResponse({"error":"name is wrong check again"}, safe=False)

                except:
                                return JsonResponse({"error":"error"}, safe=False)

class book:
        
        @csrf_exempt
        def addbook(request):
                try:
                        data = request.POST
                        mydata=json.loads(request.body)
                        name = mydata.get("book name")
                        model = book.objects.create(bookname=name)
                        return JsonResponse({"success":"add book"}, safe=False)
                except:
                        return JsonResponse({"error":"error"}, safe=False); 
        
        @csrf_exempt
        def deletebook (request):
                try:
                        data = request.POST
                        mydata=json.loads(request.body)
                        name = mydata.get("book name")
                        model = book.get(bookname=name)
                        model.delete()
                        return JsonResponse({"success":"delete book"}, safe=False)
                except:
                        return JsonResponse({"error":"error"}, safe=False); 
