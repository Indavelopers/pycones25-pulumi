import pulumi_gcp as gcp

"""Module for common networking infrastructure"""

# --- Networking config ---
# Create a custom mode network and subnets
network = gcp.compute.Network("vpc-network", auto_create_subnetworks=False)

subnet = gcp.compute.Subnetwork("subnet-webapp",
    ip_cidr_range="10.10.0.0/20",
    region=gcp.config.region,
    network=network.id,
    description="Application subnet in Madrid region")

# Firewall rule to allow web traffic (HTTP and HTTPS)
gcp.compute.Firewall("allow-http-https",
    network=network.self_link,
    allows=[
        gcp.compute.FirewallAllowArgs(protocol="tcp", ports=["80"]),
        gcp.compute.FirewallAllowArgs(protocol="tcp", ports=["443"]),
    ],
    source_ranges=["0.0.0.0/0"],
    description="Allow incoming HTTP and HTTPS traffic")

# Firewall rule to allow health checks from Google Cloud
gcp.compute.Firewall("allow-health-checks",
    network=network.self_link,
    allows=[gcp.compute.FirewallAllowArgs(protocol="tcp", ports=["80", "443", "8080"])],
    source_ranges=["35.191.0.0/16", "130.211.0.0/22"],
    description="Allow health checks from Google Cloud Load Balancers")
