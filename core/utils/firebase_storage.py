from firebase_admin import storage
import uuid

def upload_to_firebase(file, filename):
  bucket = storage.bucket()
  blob = bucket.blob(filename)
  blob.upload_from_file(file)
  blob.make_public()
  
  return blob.public_url