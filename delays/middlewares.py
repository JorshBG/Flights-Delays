from django.shortcuts import redirect


def authenticated(view):
    def wrapper(request, *args, **kwargs):
        if request.session.get("user"):
            return view(request, *args, **kwargs)

        return redirect('login')
    return wrapper

