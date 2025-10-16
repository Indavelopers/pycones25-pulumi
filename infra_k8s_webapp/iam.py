"""IAM configuration for the GKE cluster"""

import pulumi
import pulumi_gcp as gcp

# Stack config
project = gcp.config.project
config = pulumi.Config()
gke_admin_emails = config.get_object("gke_admin_emails")
gke_developer_groups = config.get_object("gke_developer_groups")

# --- IAM config ---
gke_admin_role = "roles/container.admin"
gke_developer_role = "roles/container.developer"

# Assigning GKE Admin role
for email in gke_admin_emails:
    user_iam_binding = gcp.projects.IAMMember(f"gke-admin-user-binding-{email}",
        project=project,
        role=gke_admin_role,
        member=f"user:{email}")

# Assign GKE developer roles
for group in gke_developer_groups:
    user_iam_binding = gcp.projects.IAMMember(f"gke-developer-group-binding-{group}",
        project=project,
        role=gke_developer_role,
        member=f"group:{group}")
