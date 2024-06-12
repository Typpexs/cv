from dataclasses import dataclass, field
from PIL import Image
from typing import Tuple, Optional

@dataclass
class ImageProcessor:
    image_path: str
    size: Tuple[int, int] = (100, 100)
    top_pct: float = 0.0
    right_pct: float = 0.0
    bottom_pct: float = 0.0
    left_pct: float = 0.0
    image: Optional[Image.Image] = field(default=None, init=False)

    def __post_init__(self) -> None:
        """Load the image after the dataclass is initialized."""
        self.process_image()

    def load_image(self) -> Image.Image:
        """Load the image from the image path.

        Returns:
            Image.Image: The loaded image.
        """
        self.image = Image.open(self.image_path)

    def resize_image(self) -> Image.Image:
        """Resize the stored image to the specified size.

        Returns:
            Image.Image: The resized image.
        """
        self.image = self.image.resize(self.size, Image.Resampling.LANCZOS)

    def crop_image_by_percentage(self) -> Image.Image:
        """Crop the stored image by the specified percentages from each side.

        Returns:
            Image.Image: The cropped image.
        """
        width, height = self.image.size
        left = int(self.left_pct * width)
        top = int(self.top_pct * height)
        right = width - int(self.right_pct * width)
        bottom = height - int(self.bottom_pct * height)
        self.image = self.image.crop((left, top, right, bottom))


    def process_image(self) -> Image.Image:
        """Reload image, Crop and resize the image according to the specified parameters.

        Returns:
            Image.Image: The processed image.
        """
        self.load_image()
        self.crop_image_by_percentage()
        self.resize_image()
    
    def get_image(self) -> Image.Image:
        """Return the processed image."""
        return self.image