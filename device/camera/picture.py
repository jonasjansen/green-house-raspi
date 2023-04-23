import time
from datetime import datetime
from pathlib import Path

from picamera2 import Picamera2

from config_provider import config


class Picture:

    def __init__(self):
        self.picam2 = Picamera2()
        self.file_name = ""
        self.folder_name = ""

    def take(self):
        self.picam2.start_and_capture_file(self.get_file_path(), show_preview=False)

    def get_file_path(self):
        # create file in patter PICTURE_PATH/YYYY-DD-MM/YYYY-DD-MM__hh-mm-ss_picture.jpg
        now = datetime.now()
        self.folder_name = '/'.join((config.get_config('DATA/PATH/PICTURE'), now.strftime("%Y-%m-%d")))
        self.file_name = '_'.join((now.strftime("%Y-%m-%d__%H-%M-%S"), '_picture.jpg'))

        # create folder if it does not exist
        Path(self.folder_name).mkdir(parents=True, exist_ok=True)

        return '/'.join((self.folder_name, self.file_name))


picture = Picture()
