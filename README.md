# Django MinIO uploader

![minio](static/MINIO.png)

### A simple django interface for upload files in [MinIO](https://min.io).

---

## Get Started

- Create a directory and run `python -m virtualenv venv` within the directory to create a virtual environment.
- Activate virtual environment using `./venv/scripts/activate`.
- Create a git repository using `git init`
- Get files with `git clone https://github.com/mrsins02/minio_uploader.git`.
- Run `pip install -r requirements.txt` to install requirements of project.
- Run with local server using `python manage.py runserver`.

---

❗ The project runs with MinIO's test and public server configs.
To change the configs go to [`/minio_uploader/upload_func.py`](minio_uploader/upload_func.py)