resource "google_compute_network" "api_sentinel_vpc" {
  name                    = var.network_name
  auto_create_subnetworks = false
  routing_mode            = "REGIONAL"
}

resource "google_compute_subnetwork" "api_sentinel_subnet" {
  name          = var.subnet_name
  ip_cidr_range = var.subnet_cidr
  region        = var.region
  network       = google_compute_network.api_sentinel_vpc.id

  secondary_ip_range {
    range_name    = "api-sentinel-pods"
    ip_cidr_range = var.pods_cidr
  }

  secondary_ip_range {
    range_name    = "api-sentinel-services"
    ip_cidr_range = var.services_cidr
  }
}