from django.core.wsgi import get_wsgi_application


def lambda_handler(event, context):
    # Create WSGI application
    application = get_wsgi_application()

    # Pass the event (request) to Django's WSGI handler
    return application(event, context)
