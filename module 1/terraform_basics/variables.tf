variable "credentials" {
  description = "Path to service account key"
  default     = "./keys/credentials.json"
}

variable "project" {
  default     = "terraform-demo-413122"
  description = "Google Cloud Project ID"
}

variable "region" {
  description = "Google Cloud Region"
  default     = "us-west1"
}

variable "bucket_name" {
  description = "Name of Google Cloud Storage Bucket"
  default     = "terraform-demo-413122-demo-bucket"
}

variable "location" {
  default     = "US"
  description = "Location where resource needs to be created"
}
variable "bq_dataset_name" {
  description = "BigQuery Dataset name"
  default     = "terraform_demo_dataset"
}
