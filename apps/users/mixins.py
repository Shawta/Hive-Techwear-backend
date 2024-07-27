from rest_framework import status
import datetime
from config.helpers.error_response import error_response
from .models import User

#add this mixin to the login required class
class CustomLoginRequiredMixin():
    
    def dispatch(self,request, *args, **kwargs):
        if 'Authorization' not in request.headers:
            return error_response('Please set Auth-Token.', status.HTTP_401_UNAUTHORIZED)
        
        
        token = request.hearders['Authorization']
        now = datetime.datetime.now()
        login_user = User.objects.filter(token=token, token_expires_at__gt=now)
        if len(login_user) == 0:
            return error_response('The token is invalid or expired.', status.HTTP_401_UNAUTHORIZED)
        
        request.login_user = login_user[0]
        return super().dispatch(request, *args, **kwargs)
            
        