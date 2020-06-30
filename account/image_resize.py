from io import BytesIO
from django.core.files import File
from PIL import Image


def resize(image, size=(100, 100)):

    im = Image.open(image)

    im.convert('RGB')  # convert mode

    im.thumbnail(size)  # resize image

    thumb_io = BytesIO()  # create a BytesIO object
    thumb_extension = im.format.lower()

    if thumb_extension in ['jpg', 'jpeg']:
        FTYPE = 'JPEG'
    elif thumb_extension == 'gif':
        FTYPE = 'GIF'
    elif thumb_extension == 'png':
        FTYPE = 'PNG'

    im.save(thumb_io, FTYPE, quality=99)  # save image to BytesIO object

    # create a django friendly File object
    thumbnail = File(thumb_io, name=image.name)

    return thumbnail
