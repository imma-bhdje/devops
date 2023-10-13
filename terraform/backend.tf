terraform {
  backend "s3" {
    region         = "us-east-1"
    bucket         = "imma-bucket"
    key            = "epita/imma/infra.tfstate"
    dynamodb_table = "imma-tab"
  }
}
