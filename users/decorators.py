from django.shortcuts import redirect


def login_refused(func):
    def wrapper(request):
        if request.user.is_authenticated:
            return redirect('dashboard')

        return func(request)

    return wrapper
