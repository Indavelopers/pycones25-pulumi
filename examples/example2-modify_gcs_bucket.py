"""A Google Cloud Python Pulumi program"""

import pulumi
import pulumi_gcp as gcp

# Create a GCP resource
vm_instance = gcp.compute.Instance("my-instance",
    network_interfaces=[{
        "access_configs": [{}],
        "network": "default",
    }],
    name="my-instance",
    machine_type="e2-micro",
    zone="europe-southwest1-a",
    boot_disk={
        "initialize_params": {
            "image": "debian-cloud/debian-13"
        },
    })

# Create a GCS bucket
bucket = gcp.storage.Bucket("my-bucket", location="EU", storage_class="NEARLINE")

# Export resource attributes
pulumi.export('vm_instance_name', vm_instance.name)
pulumi.export('bucket_storage_class', bucket.storage_class)
