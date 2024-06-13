from modules.images import (
        python_logo_processor, docker_logo_processor, 
        kube_logo_processor, azureml_logo_processor, 
        ado_logo_processor, bash_logo_processor,
        linux_logo_processor, snowflake_logo_processor,
        fastapi_logo_processor, formateur_logo_processor,
        helm_logo_processor, streamlit_logo_processor,
        jupyter_logo_processor, mlflow_logo_processor
    )

PYTHON_LOGO = python_logo_processor.get_image()
DOCKER_LOGO = docker_logo_processor.get_image()
KUBE_LOGO = kube_logo_processor.get_image()
ADO_LOGO = ado_logo_processor.get_image()

AZUREML_LOGO = azureml_logo_processor.get_image()
BASH_LOGO = bash_logo_processor.get_image()
LINUX_LOGO = linux_logo_processor.get_image()
SNOWFLAKE_LOGO = snowflake_logo_processor.get_image()
FASTAPI_LOGO = fastapi_logo_processor.get_image()

# GIT_LOGO = git_logo_processor.get_image()
FORMATEUR_LOGO = formateur_logo_processor.get_image()
HELM_LOGO = helm_logo_processor.get_image()
STREAMLIT_LOGO = streamlit_logo_processor.get_image()
JUPYTER_LOGO = jupyter_logo_processor.get_image()
MLFLOW_LOGO = mlflow_logo_processor.get_image()