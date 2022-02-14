from django.views import View
from django.http import HttpResponse, JsonResponse
import json
from django.contrib.auth.models import User

# Create your views here.
class santri(View):
    def post(self, request):
        body_request = request.body.decode('utf-8')
        print(request.body)
        body = json.loads(body_request)
        username = body["username"]
        password = body["password"]
        data = {
            "username":username,
            "password":password
        }
        return JsonResponse(data)
        
    
    def get(self, request):
        return HttpResponse('halo santri')
    
class homeview(View):
    def get(self, request):
        return HttpResponse('homeview')
        

