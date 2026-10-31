def calculate_theoretical_inference_time(total_operations_billion, device_tops):
    """
    Calculate the theoretical inference time (in milliseconds) for a batch.

    Args:
        total_operations_billion (float): Total operations per batch (in billions).
        device_tops (float): Device throughput in TOPS (Tera Operations Per Second).

    Returns:
        dict: {
            'total_operations_billion': float,
            'device_tops': float,
            'inference_time_ms': float
        }
    """
    # 1 TOPS = 1e12 operations/sec
    # 1 billion = 1e9 operations
    # Time (sec) = (total_ops * 1e9) / (device_tops * 1e12)
    # Time (ms) = Time (sec) * 1000
    total_ops = float(total_operations_billion) * 1e9
    device_tops = float(device_tops)
    if device_tops <= 0:
        raise ValueError("Device TOPS must be positive.")
    time_sec = total_ops / (device_tops * 1e12)
    inference_time_ms = time_sec * 1000.0
    return {
        'total_operations_billion': total_operations_billion,
        'device_tops': device_tops,
        'inference_time_ms': inference_time_ms
    }
