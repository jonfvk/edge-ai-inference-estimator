def format_estimation_summary(
    model_memory_info,
    operations_info,
    inference_time_info,
    capability_result,
    device_summary=None
):
    """
    Format the estimation results as a readable summary string.

    Args:
        model_memory_info (dict): Output from estimate_model_memory_usage.
        operations_info (dict): Output from estimate_operations_required.
        inference_time_info (dict): Output from calculate_theoretical_inference_time.
        capability_result (dict): Output from compare_to_device_capabilities or compare_to_custom_device_capabilities.
        device_summary (dict, optional): Device summary info (from .hardware or .custom_device).

    Returns:
        str: Readable summary of the estimation and capability check.
    """
    lines = []
    if device_summary:
        lines.append(f"Device: {device_summary.get('name', 'Unknown')}")
        lines.append(f"  Memory: {device_summary.get('memory_mb', '?')} MB")
        lines.append(f"  Max TOPS: {device_summary.get('max_tops', '?')}")
        if device_summary.get('cpu'):
            lines.append(f"  CPU: {device_summary['cpu']}")
        if device_summary.get('gpu'):
            lines.append(f"  GPU: {device_summary['gpu']}")
        lines.append("")
    lines.append("=== Model & Data ===")
    lines.append(f"Model size: {model_memory_info['model_size_mb']:.1f} MB")
    lines.append(f"Input size per batch: {model_memory_info['input_total_mb']:.2f} MB")
    lines.append(f"Activation overhead: {model_memory_info['activation_overhead_mb']:.2f} MB")
    lines.append(f"Estimated total memory usage: {model_memory_info['total_usage_mb']:.2f} MB")
    lines.append("")
    lines.append("=== Operations ===")
    lines.append(f"Operations per inference: {operations_info['operations_per_inference']:.2f} billion")
    lines.append(f"Batch size: {operations_info['batch_size']}")
    lines.append(f"Total operations per batch: {operations_info['total_operations']:.2f} billion")
    lines.append(f"Total operations per batch: {operations_info['total_operations_tops']:.4f} TOPS")
    lines.append("")
    lines.append("=== Inference Time ===")
    lines.append(f"Estimated inference time per batch: {inference_time_info['inference_time_ms']:.2f} ms")
    lines.append("")
    lines.append("=== Capability Check ===")
    lines.append(f"Memory used: {capability_result['memory_used_mb']:.2f} MB / {capability_result['memory_limit_mb']:.0f} MB ({'OK' if capability_result['memory_ok'] else 'EXCEEDED'})")
    lines.append(f"Operations per batch: {capability_result['operations_per_batch_billion']:.2f}B / {capability_result['tops_limit']*1000:.0f}B ({'OK' if capability_result['operations_ok'] else 'EXCEEDED'})")
    lines.append(f"Inference time: {capability_result['inference_time_ms']:.2f} ms / 1000.00 ms ({'OK' if capability_result['inference_time_ok'] else 'EXCEEDED'})")
    lines.append("")
    lines.append("Details:")
    lines.append(f"  {capability_result['details']}")
    return "\n".join(lines)
