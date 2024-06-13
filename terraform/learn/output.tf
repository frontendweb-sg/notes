output "user-name" {
  value = "Hello World! ${var.name}"
}

output "user-age" {
  value = var.age
}

output "user-skills" {
  description = "user skills"
  depends_on  = [var.name]
  precondition {
    condition     = var.name != "pradeep"
    error_message = "Pradeep can not be the name"
  }
  value = var.skills[0]
}


output "post" {
  value = var.post
}
