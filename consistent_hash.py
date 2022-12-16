"""
This implementation uses the hashlib module to calculate a hash value
for each node and a set of virtual nodes, and then maps these hash 
values to the corresponding nodes using a dictionary. It then sorts 
the dictionary keys and selects the node corresponding to the first 
key that is greater than or equal to the hash value of the key being 
looked up. This ensures that keys are distributed evenly across the 
nodes in the cluster, with a minimal number of remapping operations when 
nodes are added or removed.

"""
import hashlib

def consistent_hash_ring(key, nodes, num_virtual_nodes):
    """
    Calculates the consistent hash value for a given key and set of 
    nodes on a ring with virtual nodes.
    """
    points = {}
    for node in nodes:
        for i in range(num_virtual_nodes):
            h = hashlib.md5(node + '-' + str(i)).hexdigest()
            points[int(h, 16)] = node
    sorted_points = sorted(points.keys())
    hash_value = int(hashlib.md5(key).hexdigest(), 16)
    for point in sorted_points:
        if hash_value <= point:
            return points[point]
    return points[sorted_points[0]]

# Example usage
nodes = ['node1', 'node2', 'node3']
key = 'some_key'
num_virtual_nodes = 10
selected_node = consistent_hash_ring(key, nodes, num_virtual_nodes)
print(selected_node)  # Outputs one of the nodes in the list
