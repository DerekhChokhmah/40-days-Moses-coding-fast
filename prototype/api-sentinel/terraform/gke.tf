resource "google_container_cluster" "api_sentinel" {
  name     = var.cluster_name
  location = var.zone

  network    = google_compute_network.api_sentinel_vpc.id
  subnetwork = google_compute_subnetwork.api_sentinel_subnet.id

  networking_mode = "VPC_NATIVE"

  initial_node_count = 0

  deletion_protection = true

  ip_allocation_policy {
    cluster_secondary_range_name  = "api-sentinel-pods"
    services_secondary_range_name = "api-sentinel-services"
  }
}

resource "google_container_node_pool" "api_sentinel_nodes" {
  name     = "api-sentinel-node-pool"
  location = var.zone
  cluster  = google_container_cluster.api_sentinel.name

  node_count = var.node_count

  node_config {
    machine_type = var.machine_type

    disk_size_gb = 30
    disk_type    = "pd-balanced"
    spot         = true

    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform"
    ]

    labels = {
      environment = var.environment
      application = "api-sentinel"
    }
  }
}