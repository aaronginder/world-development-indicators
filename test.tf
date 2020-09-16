provider "google" {
  project = "ace-digit-277918"
  region = "europe-west2"
  version = "2.20.0"
}

provider "google-beta" {
  project = "ace-digit-277918"
  region = "europe-west2"
  version = "2.20.0"
}



resource "google_bigquery_dataset" "test123456" {
  dataset_id = "test_ds123456"
  location = "europe-west2"

  access {
    role = "roles/viewer"
    user_by_email = "aaronginder@hotmail.co.uk"
  }
}