import secrets
import os
from PIL import Image
from flask import url_for, current_app
from sewsocrafty.config import Config


def save_picture(form_picture, old_picture):
    random_hex = secrets.token_hex(10)
    # unused variable is defined with an '_'
    # this keeps editors from freaking out that the '_' variable wasn't used
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    # give the full path from root to where the file needs to
    # be stored, including the new filename.
    picture_path = os.path.join(
        current_app.root_path, 'static/images/admins', picture_fn)

    # resize image to 400x400
    output_size = (400, 400)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    # save actual resized image
    i.save(picture_path)
    old_pic = os.path.join(
        current_app.root_path, 'static/images/admins/', old_picture)

    # verify old_pic is not the default.png used as a default
    print(old_picture)
    if old_picture != 'default.png':
        # remove the old picture
        try:
            os.remove(old_pic)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))

    return picture_fn
