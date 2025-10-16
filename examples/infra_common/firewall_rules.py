import pulumi
import pulumi_gcp as gcp

"""Create default firewall rules"""

gcp.compute.Firewall("deny-ingress-ssh",
    network="default",
    allows=[gcp.compute.FirewallAllowArgs(protocol="tcp", ports=["22"])],
    direction="INGRESS",
    source_ranges=["0.0.0.0/0"],
    priority=100, # A high priority to ensure it takes precedence
    description="Deny incoming SSH traffic from all sources."
)

gcp.compute.Firewall("deny-ingress-rdp",
    network="default",
    allows=[gcp.compute.FirewallAllowArgs(protocol="tcp", ports=["3389"])],
    direction="INGRESS",
    source_ranges=["0.0.0.0/0"],
    priority=100, # A high priority to ensure it takes precedence
    description="Deny incoming RDP traffic from all sources."
)
