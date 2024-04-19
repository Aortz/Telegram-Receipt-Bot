from google.cloud import storage
from flask import abort, send_file
import os

def upload_excel_to_gcs(bucket_name, local_file_path, gcs_file_name):
    # Initialize GCS client
    client = storage.Client()

    # Get bucket
    bucket = client.bucket(bucket_name)

    # Upload local file to GCS
    blob = bucket.blob(gcs_file_name)
    blob.upload_from_filename(local_file_path)

    print(f"File {local_file_path} uploaded to {gcs_file_name} in bucket {bucket_name}")

def fetch_excel_from_gcs(request):
    # Set the name of the GCS bucket and the file to fetch
    bucket_name = "your_bucket_name"
    gcs_file_name = "your_file.xlsx"

    # Initialize GCS client
    client = storage.Client()

    # Get bucket
    bucket = client.bucket(bucket_name)

    # Get blob (file) from bucket
    blob = bucket.blob(gcs_file_name)

    # Check if the file exists
    if not blob.exists():
        abort(404, f"File {gcs_file_name} not found in bucket {bucket_name}")

    # Download the file to a temporary location
    temp_file_path = "/tmp/downloaded_file.xlsx"  # Use a temporary directory for Cloud Functions
    blob.download_to_filename(temp_file_path)

    # Send the file as a response
    return send_file(temp_file_path, as_attachment=True, attachment_filename=gcs_file_name)

