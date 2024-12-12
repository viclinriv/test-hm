# main.py
from google.cloud import storage
import os

def move_dicom_file(source_bucket_name, source_blob_name, destination_bucket_name, destination_blob_name):
    """Moves a DICOM file between buckets in Google Cloud Storage.

    Args:
        source_bucket_name: The name of the source bucket.
        source_blob_name: The name of the DICOM file in the source bucket.
        destination_bucket_name: The name of the destination bucket.
        destination_blob_name: The name of the DICOM file in the destination bucket.
    """

    storage_client = storage.Client()

    source_bucket = storage_client.bucket(source_bucket_name)
    source_blob = source_bucket.blob(source_blob_name)
    destination_bucket = storage_client.bucket(destination_bucket_name)

    # Copy the blob to the destination bucket
    new_blob = source_bucket.copy_blob(
        source_blob, destination_bucket, destination_blob_name
    )

    # Delete the original blob from the source bucket
    source_blob.delete()

    print(f"DICOM file {source_blob_name} moved from {source_bucket_name} to {destination_bucket_name}")


if __name__ == "__main__":
    move_dicom_file(os.environ.get('SOURCE_BUCKET'), os.environ.get('SOURCE_BLOB'), os.environ.get('DESTINATION_BUCKET'), os.environ.get('DESTINATION_BLOB'))
