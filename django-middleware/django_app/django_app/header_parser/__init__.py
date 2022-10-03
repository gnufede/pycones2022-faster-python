from django_app.header_parser.find_headers import get_user_agent


def header_parser(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = get_response(request)

        user_agent = get_user_agent(request.META)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware
