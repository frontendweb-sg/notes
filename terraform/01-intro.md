# Terraform

`Terraform` is an infrastructure as a code tool that lets you build, change and version infrastructure safely and efficiently.

This includes low-level components like `compute instance`, `storage` and `networking`; and high-level components
like `DNS` entries and `SaaS` features.

<br />

**`How does terraform work`**

Terraform creates and manages resources on `cloud platforms` and other services through their application programming interfaces (APIs).

<br />

![image](./assets.avif)

The core terraform framework consists of three stages:

- `Write:`
  You define resources, which may be across multiple cloud providers and services

  `Example:`
  you might create a configuration to deploy an application on virtual machines in a Virtual Private Cloud (VPC) network with security groups and a load balancer.

- `Plan:`
  Terraform creates an execution plan describing the infrastructure it will create, update, or destroy based on the existing infrastructure and your configuration.

- `Apply:`
  On approval, Terraform performs the proposed operations in the correct order, respecting any resource dependencies.

![image-1](./image-1.avif)

<br />

**`Variables:`**

`Syntax:`

```terraform
# declare variable
variable variable_name {}
```
