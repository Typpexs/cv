from dataclasses import dataclass
from PIL import Image
from typing import Optional
from streamlit.delta_generator import DeltaGenerator

@dataclass
class ImageData:
    column: DeltaGenerator
    image: Image.Image
    caption: str
    custom_column: str
    kwargs: Optional[dict] = None