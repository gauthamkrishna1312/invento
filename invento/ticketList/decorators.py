#Custom User Decorator

from functools import wraps
from django.shortcuts import redirect

def restrict_to_user(username):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.username == username:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('invento_login')  # Redirect to login page
        return _wrapped_view
    return decorator