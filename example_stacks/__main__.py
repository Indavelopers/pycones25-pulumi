"""A Google Cloud Python Pulumi program"""

import pulumi
import pulumi_gcp as gcp

# Get stack config
config = pulumi.Config()
stack_name = pulumi.get_stack()
num_instances = config.get_int('num_instances', default=1)

# Create VM instances
for i in range(1, num_instances + 1):
    vm_instance = gcp.compute.Instance(f"vm-instance-{stack_name}-{i}",
        network_interfaces=[{
            "access_configs": [{}],
            "network": "default",
        }],
        name=f"vm-instance-{stack_name}-{i}",
        machine_type="e2-micro",
        boot_disk={
            "initialize_params": {
                "image": "debian-cloud/debian-13"
            },
        })
