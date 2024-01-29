variable "credentials" {
  description = "My Credentials"
  default     = "/workspaces/de-zoomcamp/module1/terraform/keys/my-creds.json.json"
}


variable "project" {
  description = "Project"
  default     = "de-zoomcamp24"
}

variable "region" {
  description = "Region"
  default     = "us-central1"
}

variable "location" {
  description = "Project Location"
  default     = "US"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "ny_taxi_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "de-zoomcamp24-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}