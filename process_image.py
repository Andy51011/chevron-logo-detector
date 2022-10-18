import os
from google.cloud import vision
from PIL import Image


class ProcessImage:
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"/Users/andyyuen/Documents/chevron-logo-detection-23ba3ec01d06.json"
    client = vision.ImageAnnotatorClient()
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    chevron_logo_folder = os.path.join(BASE_DIR, "static", "images", "chevron_logo")
    undetected_logo_folder = os.path.join(BASE_DIR, "static", "images", "undetected_logo")
    failed_detection = os.path.join(BASE_DIR, "static", "images", "failed_detection")

    def __init__(self):
        super().__init__()
        self.processed_img_dict = {}
        self.chevron_logo_image_count = 0
        self.undetected_logo_image_count = 0
        self.failed_image_count = 0
        self.directory = None

    def filter_img(self):
        print(self.processed_img_dict, "test")
        for file, logos in self.processed_img_dict.items():
            file_path = os.path.join(self.directory, file)
            im = Image.open(file_path)
            im.thumbnail((1000, 1000))
            if not logos:
                im.save(f"{self.failed_detection}/{file}")
                self.failed_image_count += 1
            elif logos[0].description == "Chevron Corporation":
                im.save(f"{self.chevron_logo_folder}/{file}")
                self.chevron_logo_image_count += 1
            else:
                im.save(f"{self.undetected_logo_folder}/{file}")
                self.undetected_logo_image_count += 1

    def detect_logos(self):
        list_files = os.listdir(self.directory)
        for file in list_files:
            file_path = os.path.join(self.directory, file)
            with open(file_path, mode="rb") as image_stream:
                content = image_stream.read()
                image = vision.Image(content=content)
                response = self.client.logo_detection(image=image)
                logos = response.logo_annotations
                print(f"Searching Images for logos...{file}")
                self.processed_img_dict[file] = logos
