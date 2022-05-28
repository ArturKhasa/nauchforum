from django.test import TestCase
from PIL import Image
from models import Profile
class ModelsTestCase(TestCase):
    def profile_img_test(self):
        img = Image.open("app/media/profile_pics/images.png")
        if img.height > 300 or img.width > 300:
            img.thumbnail((300, 300))
            Profile.save(self.image.path)



