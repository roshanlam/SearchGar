from django.conf import settings


def dev_cors_middleware(get_response):
    """
    Adds CORS headers for local testing only to allow the frontend, which is served on
    settings.REACT_APP_URL, to access the API, which is served on localhost:8000.
    """
    def middleware(request):
        response = get_response(request)
        response['Access-Control-Allow-Origin'] = settings.REACT_APP_URL
        response['Access-Control-Allow-Methods'] = 'GET, POST, PUT, PATCH, OPTIONS, DELETE, HEAD'
        response['Access-Control-Allow-Headers'] = 'Content-Type, X-CSRFToken'
        response['Access-Control-Allow-Credentials'] = 'true'
        return response
    return middleware