def estimate_operations_required(operations_billion, batch_size=1):
    """
    Estimate the total number of operations required per inference batch.

    Args:
        operations_billion (float): Number of operations per inference (in billions).
        batch_size (int): Number of inputs processed in a batch.

    Returns:
        dict: {
            'operations_per_inference': float,  # in billions
            'batch_size': int,
            'total_operations': float,         # in billions
            'total_operations_tops': float     # in tera operations (TOPS)
        }
    """
    operations_per_inference = float(operations_billion)
    batch_size = int(batch_size)
    total_operations = operations_per_inference * batch_size
    total_operations_tops = total_operations / 1000.0  # 1 TOPS = 1e12 ops, 1 billion = 1e9
    return {
        'operations_per_inference': operations_per_inference,
        'batch_size': batch_size,
        'total_operations': total_operations,
        'total_operations_tops': total_operations_tops
    }
