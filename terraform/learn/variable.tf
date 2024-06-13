variable "name" {
  type = string

}

variable "age" {
  type = number
}

variable "skills" {
  type    = list(string)
  default = ["html", "js", "css"]
}


variable "post" {
  type = object({
    title       = string
    description = string
  })
}
