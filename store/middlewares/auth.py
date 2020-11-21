from django.shortcuts import redirect

def auth_middleware(get_response):
    def middleware(request):
        print("middleware",request.GET.get('customer'))
        returnUrl = request.META['PATH_INFO']
        print(returnUrl)
        if not request.session.get('customer'):
            print("thies")
            return redirect(f'/login?return_url={returnUrl}')
        print("now")
        print(get_response(request))
        response = get_response(request)
        return response

    return middleware