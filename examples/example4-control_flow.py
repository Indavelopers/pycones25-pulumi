"""A Google Cloud Python Pulumi program"""

import pulumi
import pulumi_gcp as gcp
from pulumi_random import RandomString

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

## Get stack config
config = pulumi.Config()
storage_class = config.get('gcs-storage-class', default='STANDARD')

## Use any Python module
import csv

with open('bucket_config.csv', 'r') as f:
    reader = csv.reader(f)
    bucket_configs = [(row[0], row[1]) for row in reader]

## Use Python std library
import datetime

current_year = datetime.datetime.now().year

## Use Python control flows
bucket_names = []
for i, (bucket_name, bucket_location) in enumerate(bucket_configs):
    # Create a random suffix for each bucket to ensure uniqueness.
    random_suffix = RandomString(f"bucket-suffix-{i}",
                                 length=4,
                                 lower=True,
                                 numeric=True,
                                 special=False,
                                 upper=False)

    # Construct the final bucket name as a Pulumi Output.
    final_bucket_name = pulumi.Output.concat(f"{bucket_name}-{i+1}-{storage_class.lower()}-{current_year}-", random_suffix.result)

    bucket = gcp.storage.Bucket(f"bucket-{i}", name=final_bucket_name, location=bucket_location, storage_class=storage_class)
    bucket_names.append(bucket.name)

# Export resource attributes
pulumi.export('vm_instance_name', vm_instance.name)
pulumi.export('bucket_names', bucket_names)
