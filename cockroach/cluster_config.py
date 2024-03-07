# Config sample for CockroachDB cluster with 3 nodes

DEPLOY_PATH = "/opt/cockroach"
DEPLOY_TMP_PATH = "/var/tmp"

HA_PROXY_HOSTS = None
HA_PROXY_SETUP_PATH = ""


class Region:
    def __init__(self, name, hosts):
        self.Name = name
        self.Hosts = hosts


Regions = [
    Region("us-west-1", ["ydb-001.net", ]),
    Region("us-west-2", ["ydb-002.net", ]),
    Region("us-west-3", ["ydb-003.net", ]),
]

LISTEN_PORT = 26257
HTTP_PORT = 8080

Disks = [
    "/dev/nvme0n1p2",
    "/dev/nvme1n1p2",
    "/dev/nvme2n1p2",
    "/dev/nvme3n1p2",
]
INIT_PER_DISK = 1

# per host
Cores = 128
CacheSizeGB = 150
SqlMemorySizeGB = 150
