output "Vm-proxy" {
  value = aws_instance.vm_proxy.private_ip
}

output "Vm-proxy1" {
  value = aws_instance.vm_proxy.public_ip
}

output "Vm-app-1" {
  value = aws_instance.vm_app_1.private_ip
}

output "Vm-app" {
  value = aws_instance.vm_app_1.public_ip
}

output "Vm-apache-1" {
  value = aws_instance.vm_app_2.private_ip
}

output "Vm-apache" {
  value = aws_instance.vm_app_2.public_ip
}