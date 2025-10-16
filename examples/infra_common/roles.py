import pulumi
import pulumi_gcp as gcp

"""Assign default roles policy"""

# info@indavelopers.com --> Viewer
project_viewer_binding = gcp.projects.IAMMember("role_binding-mmog-viewer",
    project=gcp.config.project,
    role="roles/viewer",
    member="user:info@indavelopers.com"
)

# info@indavelopers.com --> Compute Engine - Instance user
project_viewer_binding = gcp.projects.IAMMember("role_binding-mmog-instance_admin",
    project=gcp.config.project,
    role="roles/compute.instanceAdmin",
    member="user:info@indavelopers.com"
)

# info@indavelopers.com --> Cloud Storage - Bucket Admin
project_viewer_binding = gcp.projects.IAMMember("role_binding-mmog-bucket_admin",
    project=gcp.config.project,
    role="roles/storage.objectAdmin",
    member="user:info@indavelopers.com"
)
