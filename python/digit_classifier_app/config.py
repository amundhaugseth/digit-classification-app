from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent  # Go up three levels to the project root

MODEL_PATH = BASE_DIR / "models" / "model.pth"
TEST_IMAGE_PATH = BASE_DIR / "tests" / "images" / "test_image.jpg"
