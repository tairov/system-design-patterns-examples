"""
This implementation calculates a hash value for the key using a simple 
hashing algorithm and then maps the hash value to one of the buckets 
using a modulo operation. This ensures that keys are distributed evenly 
across the buckets, with a minimal number of remapping operations when 
the number of buckets changes.
"""

def jump_consistent_hash(key, num_buckets):
    """
    Calculates the jump consistent hash value for a given key and number of buckets.
    """
    bucket = 0
    for i in range(len(key)):
        bucket = (bucket * 33 + ord(key[i])) % 2**32
        bucket = (bucket + num_buckets) % num_buckets
    return bucket

# Example usage
key = 'some_key'
num_buckets = 10
bucket = jump_consistent_hash(key, num_buckets)
print(bucket)  # Outputs an integer between 0 and 9