# Image Uploader Project

This project is developed using Python 3.9 and allows users to upload images, requiring certain setup steps before use.

## Prerequisites

Ensure you have the following installed:
- Python 3.9
- pip
- Docker (for Docker installation)

## Traditional Installation

Follow these steps for a traditional installation:

1. **Install dependencies**

    ```
    pip install -r requirements.txt
    ```

2. **Apply Database Migrations**

    ```
    python manage.py migrate
    ```

3. **Create Basic Tier Objects**

    Before running the project, execute the following to create basic tier objects:

    ```
    python manage.py create_basic_tiers
    ```

4. **Linting**

    - Make the lint script executable:

    ```
    chmod +x ./formats 
    ```
    
    - Run the lints:

    ```
    ./formats lint
    ```

## Docker Installation

To set up using Docker, follow these steps:

1. **Build the Docker Images**

    ```
    docker-compose build
    ```
    
2. **Start the Docker Containers**

    ```
    docker-compose up
    ```
    
3. **Apply Database Migrations**

    ```
    docker exec -it image_uploader python manage.py migrate
    ```
    
4. **Create Superuser**

    ```
    docker exec -it image_uploader python manage.py createsuperuser
    ```
    
5. **Create Basic Tier Objects**

    ```
    docker exec -it image_uploader python manage.py create_basic_tiers
    ```
    
## Post Installation Steps

After creating a superuser and basic tiers, navigate to the Admin panel and assign a Tier to the user to enable image uploading capabilities.