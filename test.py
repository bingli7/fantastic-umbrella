post_data = {
    "kind": "Project",
    "apiVersion": "v1",
    "metadata": {
        "name": 'bingli'
        },
    "spec": {
        "finalizers": [
            "openshift.io/origin",
            "kubernetes"
            ]
        }
    }

print post_data