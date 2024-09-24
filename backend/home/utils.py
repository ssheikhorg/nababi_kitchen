from io import BytesIO
from PIL import Image
from django.core.files.base import ContentFile


def resize_image(image, w, h) -> None:
    # Open the uploaded image from storage
    img = Image.open(image)
    width, height = img.size

    # Resize image only if it's not already 100x100
    if width != 100 or height != 100:
        target_size = (w, h)
        img = img.resize(target_size)

        # Save the resized image to a BytesIO object
        img_io = BytesIO()
        img_format = img.format if img.format else 'JPEG'  # Set format if missing
        img.save(img_io, format=img_format)

        # Replace the image field with the resized image
        image.save(image.name, ContentFile(img_io.getvalue()), save=False)