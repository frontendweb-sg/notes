
resource "github_repository" "tf-first-repo" {
  # repo name
  name        = "first-repo-from-tf"
  description = "my first repo"

  # repo visibility (public)
  visibility = "public"

  # auto initialize
  auto_init = true
}
