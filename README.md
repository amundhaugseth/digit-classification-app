# Handwritten Digit Classifier App

This repository contains a Streamlit application that uses a PyTorch model to classify handwritten digits. The app is containerized using Docker and can be deployed using Docker Compose.

## Getting Started

1. Clone the repository: `git clone https://github.com/username/digit-classifier-app.git`
2. Navigate to the project directory: `cd digit-classifier-app`
3. Build the Docker image: `docker-compose build`
4. Run the app: `docker-compose up`
5. Open the app on [127.0.0.1:8501](URL)

## Project Structure

- `.devcontainer`:
  - `dev-conda-environment.yaml`: This file specifies the Python environment for the development container.
    - `dev.Dockerfile`: This file contains the instructions for building the development container.
    - `devcontainer.json`: This file contains the configuration for the development container.
- `models/`: This directory contains the trained PyTorch model.
  - `model.pth`: This file contains the trained PyTorch model.
- `python/`: This directory contains the Python source code for the project.
  - `digit_classifier_app/`: This directory contains the source code for the Streamlit app.
    - `__init__.py`: This file is an empty file that tells Python that this directory should be treated as a package.
    - `app.py`: This file contains the source code for the Streamlit app.
    - `config.py`: This file contains the configuration details for the application.
  - `example_project/`: This directory contains an example Python project.
    - `__init__.py`: This file is an empty file that tells Python that this directory should be treated as a package.
    - `main.py`: This file contains the source code for the example project.
- `tests/`: This directory contains the unit tests for the application.
  - `images/`: This directory contains test images.
    - `test_image.jpg`: This file is a test image.
  - `__init__.py`: This file is an empty file that tells Python that this directory should be treated as a package.
  - `test_app.py`: This file contains the unit tests for the Streamlit app

- `conda-environment.yaml`: This file specifies the Python environment for the Docker container.
- `docker-compose.yaml`: This file is used for defining and running the Docker application.
- `Dockerfile`: This file contains the instructions for building the Docker image.
- `pyproject.toml`: This file contains the metadata for the Python package.
- `README.md`: This file contains the documentation for the project.

## Next Steps

### ~~1. Testing and Debugging~~
~~Status: Completed. Unit tests have been written and all tests pass.~~

### ~~2. Create a Docker Image~~
~~Status: Completed. The Docker image of the app has been created and can be built using the provided Dockerfile.~~

### ~~3. Containerization~~
~~Status: Completed. The application has been containerized using Docker and can be deployed using Docker Compose.~~

### 4. Optimize the model
Perform a model evaluation and cross-validation. Try using different model parameters, features, and algorithms to see if it can improve the performance of the machine learning model.

### 5. Push to Docker Hub
After testing the Docker image on a local machine, the Docker image can be pushed to Docker Hub or any other Docker registry. This will allow others to pull and use the app without needing to configure the environment.

### 6. Update Documentation
Ensure that the GitHub repository has updated documentation. The documentation should include information about the project, how to use it, and how to contribute.

### 7. Publish the App
Publish the app and share it with others. The app can be deployed to a public web server or a cloud-based app platform like Heroku, Google Cloud, or AWS.

### 8. Gather feedback and iterate
Once the app is live, gather feedback from users and make improvements based on that feedback.

### 9. Continuous Integration/Continuous Deployment (CI/CD)
Consider setting up a CI/CD pipeline for the project if it will be updated regularly. CI/CD can automate testing and deployment, which can save a lot of time in the long run. Services like GitHub Actions, Jenkins, or Travis can be used for this.
