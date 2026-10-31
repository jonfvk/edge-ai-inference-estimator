from .hardware import JetsonOrinNano2Specs

def compare_to_device_capabilities(memory_usage_mb, total_operations_billion, inference_time_ms):
    """
    Compare estimated memory usage and inference time to Jetson Orin Nano 2 capabilities.

    Args:
        memory_usage_mb (float): Estimated total memory usage in MB.
        total_operations_billion (float): Total operations per batch (in billions).
        inference_time_ms (float): Estimated inference time per batch (ms).

    Returns:
        dict: {
            'memory_ok': bool,
            'memory_used_mb': float,
            'memory_limit_mb': float,
            'operations_ok': bool,
            'operations_per_batch_billion': float,
            'tops_limit': float,
            'inference_time_ms': float,
            'inference_time_ok': bool,
            'details': str
        }
    """
    specs = JetsonOrinNano2Specs
    memory_ok = memory_usage_mb <= specs.MEMORY_MB
    # The device can process up to MAX_TOPS in 1 second (1e12 ops/sec)
    # For a single batch, if the theoretical time is > 1000 ms, it's over the limit
    # But we also check if the per-batch operation count exceeds what can be done in 1 sec
    max_ops_per_sec_billion = specs.MAX_TOPS * 1000  # 1 TOPS = 1000 billion ops/sec
    operations_ok = total_operations_billion <= max_ops_per_sec_billion
    # If inference time is more than 1 second, warn
    inference_time_ok = inference_time_ms <= 1000.0
    details = []
    if not memory_ok:
        details.append(f"Memory usage ({memory_usage_mb:.1f} MB) exceeds device limit ({specs.MEMORY_MB} MB).")
    if not operations_ok:
        details.append(f"Operations per batch ({total_operations_billion:.1f}B) exceeds device throughput per second ({max_ops_per_sec_billion:.1f}B).")
    if not inference_time_ok:
        details.append(f"Estimated inference time ({inference_time_ms:.1f} ms) exceeds 1 second per batch.")
    if not details:
        details.append("All estimates are within device capabilities.")
    return {
        'memory_ok': memory_ok,
        'memory_used_mb': memory_usage_mb,
        'memory_limit_mb': specs.MEMORY_MB,
        'operations_ok': operations_ok,
        'operations_per_batch_billion': total_operations_billion,
        'tops_limit': specs.MAX_TOPS,
        'inference_time_ms': inference_time_ms,
        'inference_time_ok': inference_time_ok,
        'details': " ".join(details)
    }
