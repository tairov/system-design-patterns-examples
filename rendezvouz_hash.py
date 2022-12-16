import hashlib

def rendezvous_hash(key, nodes):
    """
    Calculates the rendezvous hash value for a given key and set of nodes.
    """
    max_weight = -1
    selected_node = None
    for node in nodes:
        weight = int(hashlib.md5(key + node).hexdigest(), 16)
        if weight > max_weight:
            max_weight = weight
            selected_node = node
    return selected_node

# Example usage
nodes = ['node1', 'node2', 'node3']
key = 'some_key'
selected_node = rendezvous_hash(key, nodes)
print(selected_node)  # Outputs one of the nodes in the list