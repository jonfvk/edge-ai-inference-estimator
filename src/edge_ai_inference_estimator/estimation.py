def estimate_model_memory_usage(model_size_mb, input_size_kb, batch_size=1):
    """
    Estimate total memory usage for inference on an edge device.

    Args:
        model_size_mb (float): Size of the model in megabytes (MB).
        input_size_kb (float): Size of input data per inference in kilobytes (KB).
        batch_size (int): Number of inputs processed in a batch.

    Returns:
        dict: {
            'model_size_mb': float,
            'input_total_mb': float,
            'total_usage_mb': float
        }
    """
    # Model weights are loaded once
    model_size_mb = float(model_size_mb)
    # Input data is loaded per batch
    input_total_mb = (float(input_size_kb) * batch_size) / 1024.0
    # For estimation, assume activations and intermediate buffers ~ model size
    # (This is a simplification; real usage may be higher for large models)
    activation_overhead_mb = model_size_mb * 0.5  # 50% of model size as overhead
    total_usage_mb = model_size_mb + input_total_mb + activation_overhead_mb
    return {
        'model_size_mb': model_size_mb,
        'input_total_mb': input_total_mb,
        'activation_overhead_mb': activation_overhead_mb,
        'total_usage_mb': total_usage_mb
    }
