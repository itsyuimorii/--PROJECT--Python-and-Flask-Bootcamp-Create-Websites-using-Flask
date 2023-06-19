#users/picture_handler.py

import os
from PIL import Image
from flask import url_for, current_app

def add_profile_pic(pic_upload, username):
    """_summary_: This function is used to add a profile picture for the user."""
    filename = pic_upload.filename
    # "mypicture.jpg" -> "jpg"
    ext_type = filename.split('.')[-1]

    storage_filename = str(username) + '.' + ext_type

    filepath = os.path.join(current_app.root_path, 'static\profile_pics', storage_filename)


