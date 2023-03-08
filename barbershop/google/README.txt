# Enable CORS for the google bucket
# Per - https://medium.com/swlh/preparing-your-django-application-for-google-cloud-run-7c8cb7b7464b
gsutil cors set cors.json gs://<STATIC_BUCKET_NAME>