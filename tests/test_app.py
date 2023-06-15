import unittest

import torch
from PIL import Image
from torchvision import transforms

# Importing the configuration
import digit_classifier_app.config as config


class TestDigitClassifier(unittest.TestCase):
    def setUp(self):
        self.transform = transforms.Compose(
            [
                transforms.Grayscale(),
                transforms.Resize((28, 28)),
                transforms.ToTensor(),
                transforms.Normalize((0.5,), (0.5,)),
            ]
        )

    def test_model_load(self):
        model = torch.load(config.MODEL_PATH, map_location="cpu")
        model.eval()
        self.assertIsNotNone(model, "Model failed to load")

    def test_model_eval(self):
        model = torch.load(config.MODEL_PATH, map_location="cpu")
        model.eval()
        self.assertEqual(model.training, False, "Model is not in eval mode")

    def test_image_transformation(self):
        img = Image.open(config.TEST_IMAGE_PATH)
        transformed_image = self.transform(img)
        self.assertIsNotNone(transformed_image, "Image transformation failed")
        self.assertEqual(
            transformed_image.size(),
            (1, 28, 28),
            "Image transformation didn't result in correct size",
        )

    def test_image_unsqueeze(self):
        img = Image.open(config.TEST_IMAGE_PATH)
        transformed_image = self.transform(img)
        unsqueezed_image = transformed_image.unsqueeze(0)
        self.assertEqual(
            unsqueezed_image.size(),
            (1, 1, 28, 28),
            "Unsqueeze operation didn't result in correct size",
        )

    def test_model_prediction(self):
        model = torch.load(config.MODEL_PATH, map_location="cpu")
        img = Image.open(config.TEST_IMAGE_PATH)
        transformed_image = self.transform(img)
        unsqueezed_image = transformed_image.unsqueeze(0)
        image_flatten = unsqueezed_image.view(unsqueezed_image.size(0), -1)
        with torch.no_grad():
            output = model(image_flatten)
            _, predicted = torch.max(output.data, 1)
        self.assertIsInstance(predicted.item(), int, "Model prediction failed")


if __name__ == "__main__":
    unittest.main()
