
provider "aws" {

}

resource "aws_dynamodb_table" "covidtable" {
  hash_key = "date"
  name = ""
  attribute {
    name = ""
    type = ""
  }
}