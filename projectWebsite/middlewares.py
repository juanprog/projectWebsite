from django.http.response import HttpResponseForbidden


class FiltraIPMiddleware:
    """ Middleware IP filter"""

    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # Authorized IP list
        ips_autorizados = ["127.0.0.1"]

        # User IP
        ip_usuario = request.META.get("REMOTE_ADDR")

        # Checks if it is an authorized IP
        if ip_usuario not in ips_autorizados:
            # If the user is not authorized > HTTP 403 (Unauthorized)
            return HttpResponseForbidden("IP não autorizado")

        # If it's an authorized IP, we don't do anything
        return None
