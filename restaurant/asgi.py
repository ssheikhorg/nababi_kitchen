import os
from django.core.asgi import get_asgi_application
from dotenv import load_dotenv
from mangum import Mangum


load_dotenv()

DJANGO_SETTINGS_MODULE = os.getenv('DJANGO_SETTINGS_MODULE')


os.environ.setdefault('DJANGO_SETTINGS_MODULE', DJANGO_SETTINGS_MODULE)

application = get_asgi_application()
handler = Mangum(application)
