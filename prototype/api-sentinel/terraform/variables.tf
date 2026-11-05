variable "project_id" {
  description = "Google Cloud project ID"
  type        = string
}

variable "region" {
  description = "Google Cloud region for API Sentinel infrastructure"
  type        = string

}

variable "cluster_name" {
  description = "Name of the GKE cluster for API Sentinel"
  type        = string
}

variable "node_count" {
  description = "Initial number of nodes in the GKE node pool"
  type        = number
}

variable "machine_type" {
  description = "Machine type used by the GKE worker nodes"
  type        = string
}

variable "network_name" {
  description = "Name of the VPC network for API Sentinel"
  type        = string
}

variable "subnet_name" {
  description = "Name of the subnet for the API Sentinel GKE cluster"
  type        = string
}

variable "subnet_cidr" {
  description = "IP address range assigned to the GKE subnet"
  type        = string
}

variable "pods_cidr" {
  description = "Secondary IP address range allocated to Kubernetes Pods"
  type        = string
}

variable "services_cidr" {
  description = "Secondary IP address range allocated to Kubernetes Services"
  type        = string
}

variable "environment" {
  description = "Deployment environment for API Sentinel"
  type        = string
}