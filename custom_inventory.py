#!/usr/bin/env python3
import json
import sys

# This is a simple example of a dynamic inventory script
# In production, this would query an API, database, or other source

inventory = {
    "all": {
        "hosts": ["server1", "server2", "server3", "server4"],
    },
    "copenhagen": {
        "hosts": ["server1", "server2"],
        "vars": {
            "datacenter": "denmark",
            "timezone": "Europe/Copenhagen"
        }
    },
    "stockholm": {
        "hosts": ["server3", "server4"],
        "vars": {
            "datacenter": "sweden",
            "timezone": "Europe/Stockholm"
        }
    },
    "nordics": {
        "children": ["copenhagen", "stockholm"],
        "vars": {
            "region": "northern_europe"
        }
    },
    "_meta": {
        "hostvars": {
            "server1": {
                "role": "web",
                "env_type": "production"
            },
            "server2": {
                "role": "db",
                "env_type": "staging"
            },
            "server3": {
                "role": "web",
                "env_type": "production"
            },
            "server4": {
                "role": "db",
                "env_type": "development"
            }
        }
    }
}

# Dynamic inventory scripts must support --list and --host arguments
if len(sys.argv) == 2 and sys.argv[1] == '--list':
    print(json.dumps(inventory, indent=2))
elif len(sys.argv) == 3 and sys.argv[1] == '--host':
    # Return specific host vars (or empty if using _meta)
    print(json.dumps({}))
else:
    print("Usage: {} --list or --host <hostname>".format(sys.argv[0]))
    sys.exit(1)
