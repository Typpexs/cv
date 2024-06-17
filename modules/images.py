
from modules.image_data import ImageData
from modules.image_processor import ImageProcessor

python_logo_processor = ImageProcessor(image_path="./static/python_logo.png", right_pct=0.2, left_pct=0.2)
docker_logo_processor = ImageProcessor(image_path="./static/docker_logo.png", size=(120,100))
kube_logo_processor = ImageProcessor(image_path="./static/kube_logo.png")
ado_logo_processor = ImageProcessor(image_path="./static/ado_logo.png")

azureml_logo_processor = ImageProcessor(image_path="./static/azureml_logo.png", size=(50,50))
bash_logo_processor = ImageProcessor(image_path="./static/bash_logo.png", size=(50,50))
linux_logo_processor = ImageProcessor(image_path="./static/linux_logo.png", size=(50,50))
snowflake_logo_processor = ImageProcessor(image_path="./static/snowflake_logo.png", size=(50,50))
fastapi_logo_processor = ImageProcessor(image_path="./static/fastapi_logo.png", size=(50,50))

# git_logo_processor = ImageProcessor(image_path="./static/git_logo.png", size=(50,50))
formateur_logo_processor = ImageProcessor(image_path="./static/formateur_logo.png", size=(50,50))
helm_logo_processor = ImageProcessor(image_path="./static/helm_logo.png", size=(50,50))
streamlit_logo_processor = ImageProcessor(image_path="./static/streamlit_logo.png", size=(50,50))
jupyter_logo_processor = ImageProcessor(image_path="./static/jupyterhub_logo.png", size=(50,50))
mlflow_logo_processor = ImageProcessor(image_path="./static/mlflow_logo.png", size=(60,50), right_pct=0.05)

def display_images_with_captions(image_data: list[ImageData]) -> None:
    """Display images with captions in Streamlit columns.

    Args:
        images_data (list[ImageData]): List of ImageData instances containing image and its properties.
    """
    for data in image_data:
        data.column.image(data.image, caption=data.caption, **(data.kwargs or {}))
        data.column.markdown(data.custom_column, unsafe_allow_html=True)