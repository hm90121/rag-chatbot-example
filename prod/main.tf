
terraform {                                      
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

resource "aws_instance" "web" {        
    ami = "ami-0822295a729d2a28e"
    instance_type = "t2.micro"

    tags = {
        Name = "Helloworld"
    }

}
// digger apply
