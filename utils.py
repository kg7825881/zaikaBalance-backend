import os
import urllib.request
import zipfile

def download_and_extract_models():
    models_dir = 'models'
    zip_path = 'models.zip'
    file_id = '1Zv1lGC2HKGin3N1JFx3FU1A-KvG4eju-'
    gdrive_url = f'https://drive.google.com/uc?export=download&id={file_id}'

    if not os.path.exists(models_dir):
        print("Downloading model zip...")
        urllib.request.urlretrieve(gdrive_url, zip_path)
        print("Extracting...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(models_dir)
        os.remove(zip_path)
        print("Models ready.")

# Call this before loading any models
download_and_extract_models()
