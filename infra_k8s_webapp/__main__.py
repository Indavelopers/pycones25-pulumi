"""A Google Cloud Python Pulumi program"""

import pulumi
import pulumi_gcp as gcp
import pulumi_random as random

# Import infra modules
import networking
import iam

# Stack config
region = gcp.config.region

# Create a Google Artifact Registry (GAR) Docker repository
webapp_container_repo = gcp.artifactregistry.Repository("webapp_container_repo",
    location=region,
    repository_id="webapp-container-repo",
    format="DOCKER",
    description="Container repository for the webapp application")

# --- SA & IAM for GKE cluster ---
# Create a dedicated service account for the GKE cluster nodes
gke_sa = gcp.serviceaccount.Account("gke-sa",
    account_id="gke-nodes-sa",
    display_name="GKE Node Service Account")

# Grant the service account permissions for logging and monitoring
gcp.projects.IAMMember("gke-sa-logging",
    project=gcp.config.project,
    role="roles/logging.logWriter",
    member=gke_sa.member)

gcp.projects.IAMMember("gke-sa-monitoring",
    project=gcp.config.project,
    role="roles/monitoring.metricWriter",
    member=gke_sa.member)

# Grant the service account permission to pull images from the Artifact Registry repo
gcp.artifactregistry.RepositoryIamMember("gke-sa-artifact-reader",
    project=webapp_container_repo.project,
    location=webapp_container_repo.location,
    repository=webapp_container_repo.name,
    role="roles/artifactregistry.reader",
    member=gke_sa.member)

# --- GKE Autopilot Cluster ---
gke_cluster = gcp.container.Cluster("gke-autopilot-cluster",
    name="gke-autopilot-cluster",
    location=region,
    enable_autopilot=True,
    network=networking.network.id,
    subnetwork=networking.subnet.id,
    node_config=gcp.container.ClusterNodeConfigArgs(
        service_account=gke_sa.email,
    ),
    description="GKE Autopilot cluster for the webapp",
    deletion_protection=False,
)

# --- GCS Bucket for application assets ---
app_bucket = gcp.storage.Bucket("app-assets-bucket",
    name=pulumi.Output.concat("app-assets-bucket", random.RandomString("bucket-suffix",
        length=8,
        special=False,
        upper=False).result),
    location=region,
    public_access_prevention="enforced",
    versioning=gcp.storage.BucketVersioningArgs(
        enabled=True,
    ))

# --- Secret Manager for DB Password ---
# Generate a random password for the database
db_password = random.RandomPassword("db-password",
    length=20,
    special=True)

# Create a secret to hold the database password
db_secret = gcp.secretmanager.Secret("db-secret",
    secret_id="db-password",
    replication=gcp.secretmanager.SecretReplicationArgs(
        auto={},
    ))

# Add the generated password as a version to the secret
db_secret_version = gcp.secretmanager.SecretVersion("db-secret-version",
    secret=db_secret.id,
    secret_data=db_password.result)

# --- Cloud SQL Instance (PostgreSQL) ---
# Set up VPC peering for the private SQL connection using Private Service Access
private_ip_address = gcp.compute.GlobalAddress("private-ip-address",
    name="private-ip-address",
    purpose="VPC_PEERING",
    address_type="INTERNAL",
    prefix_length=24,
    network=networking.network.id)

private_vpc_connection  = gcp.servicenetworking.Connection("psc-endpoint",
    network=networking.network.id,
    service="servicenetworking.googleapis.com",
    reserved_peering_ranges=[private_ip_address.name])

# Create the Cloud SQL instance
db_instance = gcp.sql.DatabaseInstance("db-instance",
    name="webapp-db",
    database_version="POSTGRES_17",
    region=region,
    settings={
        "tier": "db-f1-micro",
        "edition": "ENTERPRISE",
        "ip_configuration": {
            "ipv4_enabled": False,
            "private_network": networking.network.self_link,
            "enable_private_path_for_google_cloud_services": True,
        },
        "backup_configuration": {
            "enabled": True,
        },
    },
    root_password=db_secret_version.secret_data,
    # Ensure the SQL API and VPC peering are ready before creating the instance
    opts=pulumi.ResourceOptions(depends_on=[private_vpc_connection]))
