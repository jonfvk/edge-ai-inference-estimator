class DeviceSpecs:
    """
    Generic hardware specification for a custom edge device.
    """
    def __init__(self, name, memory_mb, max_tops, cpu=None, gpu=None, memory_type=None,
                 memory_bandwidth_gbps=None, storage=None, power_watt=None):
        self.name = name
        self.memory_mb = memory_mb
        self.max_tops = max_tops
        self.cpu = cpu
        self.gpu = gpu
        self.memory_type = memory_type
        self.memory_bandwidth_gbps = memory_bandwidth_gbps
        self.storage = storage
        self.power_watt = power_watt

    def summary(self):
        return {
            "name": self.name,
            "memory_mb": self.memory_mb,
            "max_tops": self.max_tops,
            "cpu": self.cpu,
            "gpu": self.gpu,
            "memory_type": self.memory_type,
            "memory_bandwidth_gbps": self.memory_bandwidth_gbps,
            "storage": self.storage,
            "power_watt": self.power_watt,
        }


def compare_to_custom_device_capabilities(memory_usage_mb, total_operations_billion, inference_time_ms, device_specs):
    """
    Compare estimated memory usage and inference time to custom device capabilities.

    Args:
        memory_usage_mb (float): Estimated total memory usage in MB.
        total_operations_billion (float): Total operations per batch (in billions).
        inference_time_ms (float): Estimated inference time per batch (ms).
        device_specs (DeviceSpecs): Custom device specs instance.

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
    memory_ok = memory_usage_mb <= device_specs.memory_mb
    max_ops_per_sec_billion = device_specs.max_tops * 1000  # 1 TOPS = 1000 billion ops/sec
    operations_ok = total_operations_billion <= max_ops_per_sec_billion
    inference_time_ok = inference_time_ms <= 1000.0
    details = []
    if not memory_ok:
        details.append(f"Memory usage ({memory_usage_mb:.1f} MB) exceeds device limit ({device_specs.memory_mb} MB).")
    if not operations_ok:
        details.append(f"Operations per batch ({total_operations_billion:.1f}B) exceeds device throughput per second ({max_ops_per_sec_billion:.1f}B).")
    if not inference_time_ok:
        details.append(f"Estimated inference time ({inference_time_ms:.1f} ms) exceeds 1 second per batch.")
    if not details:
        details.append("All estimates are within device capabilities.")
    return {
        'memory_ok': memory_ok,
        'memory_used_mb': memory_usage_mb,
        'memory_limit_mb': device_specs.memory_mb,
        'operations_ok': operations_ok,
        'operations_per_batch_billion': total_operations_billion,
        'tops_limit': device_specs.max_tops,
        'inference_time_ms': inference_time_ms,
        'inference_time_ok': inference_time_ok,
        'details': " ".join(details)
    }
