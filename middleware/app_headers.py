# -*- coding: utf-8 -*-


class AppHeadersMiddleware(object):

    def process_request(self, request):

        if 'HTTP_AUTHORIZATION' in request.META:
            auth_elements = request.META['HTTP_AUTHORIZATION'].split()

            if len(auth_elements) == 2 and auth_elements[0].lower() == 'token':
                request.auth_token = auth_elements[1]
            else:
                request.auth_token = None
        else:
            request.auth_token = None

        if 'HTTP_APPLICATIONCONTEXT' in request.META:
            request.app_context = request.META['HTTP_APPLICATIONCONTEXT']
        else:
            request.app_context = None

        if 'HTTP_APPVERSION' in request.META:
            request.app_version = request.META['HTTP_APPVERSION']
        else:
            request.app_version = None

        if 'HTTP_DEVICETYPE' in request.META:
            request.device_type = request.META['HTTP_DEVICETYPE']
        else:
            request.device_type = None

        if 'HTTP_DEVICETOKEN' in request.META:
            request.device_token = request.META['HTTP_DEVICETOKEN']
        else:
            request.device_token = None

        if 'HTTP_BUILDCONFIG' in request.META:
            request.build_config = request.META['HTTP_BUILDCONFIG']
        else:
            request.build_config = None

        return None