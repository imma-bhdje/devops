# vpc

resource "aws_vpc" "my_vpc" {
  cidr_block = "10.0.0.0/16"

}

#internet gateway

resource "aws_internet_gateway" "internet_gateway" {
  vpc_id = aws_vpc.my_vpc.id

  tags = {
    Name = "int_gateway"
  }

}

resource "aws_route_table" "public_routetable" {
  vpc_id = aws_vpc.my_vpc.id
  tags = {
    Name = "public_routetable_imma"
  }
}

resource "aws_route" "public_route" {
  route_table_id         = aws_route_table.public_routetable.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.internet_gateway.id
}

# subnet public

resource "aws_subnet" "public_subnet" {
  vpc_id                  = aws_vpc.my_vpc.id
  cidr_block              = "10.0.0.0/24"
  map_public_ip_on_launch = true
  tags = {
    Name = "public_subnet_"
  }
}

resource "aws_route_table_association" "public_subnet_a" {
  subnet_id      = aws_subnet.public_subnet.id
  route_table_id = aws_route_table.public_routetable.id
}

# instances

resource "aws_instance" "vm_proxy" {
  ami                         = "ami-091b1c4aa02ba6400"
  instance_type               = "t2.micro"
  subnet_id                   = aws_subnet.public_subnet.id
  associate_public_ip_address = true
  vpc_security_group_ids      = [aws_security_group.main.id]
  key_name                    = data.aws_key_pair.pro_key.key_name
  user_data                   = file("file.yml")
  # iam_instance_profile = aws_iam_instance_profile.project_profile.name

  tags = {
    Name = "public_vm"
  }
}



resource "aws_instance" "vm_app_1" {
  ami                         = "ami-091b1c4aa02ba6400"
  instance_type               = "t2.micro"
  subnet_id                   = aws_subnet.public_subnet.id
  vpc_security_group_ids      = [aws_security_group.main.id]
  key_name                    = data.aws_key_pair.pro_key.key_name
  associate_public_ip_address = true
  user_data                   = file("file.yml")

  tags = {
    Name = "private_vm1"
    User = "imma"
  }
}

resource "aws_instance" "vm_app_2" {
  ami                         = "ami-091b1c4aa02ba6400"
  instance_type               = "t2.micro"
  subnet_id                   = aws_subnet.public_subnet.id
  associate_public_ip_address = true
  vpc_security_group_ids      = [aws_security_group.main.id]
  key_name                    = data.aws_key_pair.pro_key.key_name
  user_data                   = file("file.yml")
  tags = {
    Name = "private_vm2"
    User = "imma"
  }
}

# paire de clé

resource "aws_key_pair" "admin" {
  key_name   = "infra_git"
  public_key = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIB7Xg/AGmQuoeV+9Ud8PzRZV7/54+kjJ/L0nqYeQP2ah immabhd@gmail.com"
  tags = {
    Name = "infra_key"
  }
}


# security group

# resource "aws_security_group" "proxy" {
#   description = "infrastructure security proxy"
#   vpc_id      = aws_vpc.my_vpc.id

#   egress {
#     from_port   = 80
#     to_port     = 80
#     protocol    = "tcp"
#     cidr_blocks = ["0.0.0.0/0"]

#   }

#   egress {
#     from_port   = "443"
#     to_port     = "443"
#     protocol    = "tcp"
#     cidr_blocks = ["0.0.0.0/0"]

#   }
# }

resource "aws_security_group" "main" {
  description = "infrastructure"
  vpc_id      = aws_vpc.my_vpc.id


  ingress {
    from_port   = 20022
    to_port     = 20022
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]

  }


  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }


  egress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]

  }

  egress {
    from_port   = "443"
    to_port     = "443"
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]

  }

}


