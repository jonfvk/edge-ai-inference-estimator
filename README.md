# Edge AI Inference Estimator

Estimate and compare AI inference workloads for edge devices using user-supplied model and data parameters, focusing on performance and efficiency.

## Project Overview

**Problem:**
Developers need a quick way to estimate if their AI models will run efficiently on new edge hardware like Jetson Orin Nano 2, given constraints on performance and memory.

**Approach:**
Build a CLI tool that takes model size, input data size, and expected operations, then estimates inference time and memory usage based on device specs.

## Features
- Estimates memory usage for model and input data
- Calculates total operations per batch
- Computes theoretical inference time based on device throughput (TOPS)
- Compares estimates to device capabilities (Jetson Orin Nano 2 or custom specs)
- Outputs warnings if limits are exceeded
- Supports custom device specifications
- Formats results as a readable summary

## Supported Devices
- NVIDIA Jetson Orin Nano 2 (default)
- Custom edge device (user-supplied specs)

## Installation

Clone the repository and ensure you have Python 3.7+.

```
python -m pip install .
```

Or, for development:

```
python -m pip install -e .
```

## Usage

Run the estimator from the command line:

```
python -m edge_ai_inference_estimator.cli \
    --model-size 120 \
    --input-size 256 \
    --operations 3.2 \
    --batch-size 4
```

**Arguments:**
- `--model-size`: Model size in megabytes (MB). Required.
- `--input-size`: Input data size per inference in kilobytes (KB). Required.
- `--operations`: Estimated number of operations per inference (in billions, e.g., 1.5 for 1.5e9). Required.
- `--batch-size`: Batch size for inference (default: 1).

**Example Output:**
```
Device: Jetson Orin Nano 2
  Memory: 8192 MB
  Max TOPS: 40.0
  CPU: 6-core ARM Cortex-A78AE v8.2 64-bit CPU
  GPU: NVIDIA Ampere architecture GPU with 1024 CUDA cores

=== Model & Data ===
Model size: 120.0 MB
Input size per batch: 1.00 MB
Activation overhead: 60.00 MB
Estimated total memory usage: 181.00 MB

=== Operations ===
Operations per inference: 3.20 billion
Batch size: 4
Total operations per batch: 12.80 billion
Total operations per batch: 0.0128 TOPS

=== Inference Time ===
Estimated inference time per batch: 0.32 ms

=== Capability Check ===
Memory used: 181.00 MB / 8192 MB (OK)
Operations per batch: 12.80B / 40000B (OK)
Inference time: 0.32 ms / 1000.00 ms (OK)

Details:
  All estimates are within device capabilities.
```

## Custom Device Support

You can use the Python API to estimate for custom devices:

```python
from edge_ai_inference_estimator.custom_device import DeviceSpecs, compare_to_custom_device_capabilities
from edge_ai_inference_estimator.estimation import estimate_model_memory_usage
from edge_ai_inference_estimator.operations import estimate_operations_required
from edge_ai_inference_estimator.inference_time import calculate_theoretical_inference_time
from edge_ai_inference_estimator.summary import format_estimation_summary

# Define your device
my_device = DeviceSpecs(
    name="My Edge Device",
    memory_mb=4096,
    max_tops=8.0,
    cpu="Quad-core ARM",
    gpu="Custom GPU",
    memory_type="LPDDR4",
    memory_bandwidth_gbps=32,
    storage="eMMC",
    power_watt=10
)

# Estimate
model_info = estimate_model_memory_usage(120, 256, batch_size=4)
ops_info = estimate_operations_required(3.2, batch_size=4)
time_info = calculate_theoretical_inference_time(ops_info['total_operations'], my_device.max_tops)
cap_result = compare_to_custom_device_capabilities(
    model_info['total_usage_mb'],
    ops_info['total_operations'],
    time_info['inference_time_ms'],
    my_device
)
summary = format_estimation_summary(model_info, ops_info, time_info, cap_result, my_device.summary())
print(summary)
```

## Testing

Run all tests with:

```
python -m unittest discover tests
```

## Source URLs
- https://techgig.com/news/ai/nvidia-unveils-jetson-orin-nano-2-for-edge-ai-robotics/134930001 (retrieved 2024-06-10)

## License
MIT License
