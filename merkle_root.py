import hashlib


def sha256(data):
    """Return hex-encoded SHA-256 of the given string data."""
    return hashlib.sha256(data.encode()).hexdigest()


def merkle_root(leaves):
    if not leaves:
        return None

    hashes = [sha256(x) for x in leaves]
    while len(hashes) > 1:
        if len(hashes) % 2 == 1:
            hashes.append(hashes[-1])

        hashes = [sha256(hashes[i] + hashes[i + 1]) for i in range(0, len(hashes), 2)]

    return hashes[0]


transactions = ["Tx1", "Tx2", "Tx3", "Tx4"]
print("Merkle Root:", merkle_root(transactions))
