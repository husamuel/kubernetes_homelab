from kubernetes import client, config

def get_cluster_info():
    config.load_kube_config()

    v1 = client.CoreV1Api()
    nodes = v1.list_node().items

    info = []
    for node in nodes:
        info.append({
            "name": node.metadata.name,
            "cpu": node.status.capacity["cpu"],
            "memory": node.status.capacity["memory"]
        })
    return info
