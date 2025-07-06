from rest_framework.views import exception_handler
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated, PermissionDenied, ValidationError
from rest_framework import status
from rest_framework.response import Response

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        custom_response_data = {
            'success': False,
            'message': '',
            'errorDetails': None,
            'data': None
        }

        if isinstance(exc, NotAuthenticated):
            custom_response_data['message'] = 'Unauthorized access.'
            custom_response_data['errorDetails'] = str(exc)

        elif isinstance(exc, AuthenticationFailed):
            custom_response_data['message'] = 'Authentication failed.'
            custom_response_data['errorDetails'] = str(exc)

        elif isinstance(exc, PermissionDenied):
            custom_response_data['message'] = 'Permission denied.'
            custom_response_data['errorDetails'] = str(exc)

        elif isinstance(exc, ValidationError):
            custom_response_data['message'] = 'Validation failed.'
            custom_response_data['errorDetails'] = response.data

        else:
            custom_response_data['message'] = 'An error occurred.'
            custom_response_data['errorDetails'] = str(exc)

        return Response(custom_response_data, status=response.status_code)

    # fallback if no response
    return Response({
        'success': False,
        'message': 'Internal server error.',
        'errorDetails': str(exc),
        'data': None
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
