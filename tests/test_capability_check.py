import unittest
from edge_ai_inference_estimator.capability_check import compare_to_device_capabilities

class TestCapabilityCheck(unittest.TestCase):
    def test_all_within_limits(self):
        # Well within Jetson Orin Nano 2 specs
        memory_usage_mb = 4000  # 4 GB
        total_operations_billion = 1000  # 1 trillion ops (1 TOPS)
        inference_time_ms = 100  # 0.1 sec
        result = compare_to_device_capabilities(memory_usage_mb, total_operations_billion, inference_time_ms)
        self.assertTrue(result['memory_ok'])
        self.assertTrue(result['operations_ok'])
        self.assertTrue(result['inference_time_ok'])
        self.assertIn('All estimates are within device capabilities.', result['details'])

    def test_memory_exceeded(self):
        # Exceed memory
        memory_usage_mb = 9000  # 9 GB
        total_operations_billion = 1000
        inference_time_ms = 100
        result = compare_to_device_capabilities(memory_usage_mb, total_operations_billion, inference_time_ms)
        self.assertFalse(result['memory_ok'])
        self.assertTrue(result['operations_ok'])
        self.assertTrue(result['inference_time_ok'])
        self.assertIn('Memory usage', result['details'])
        self.assertIn('exceeds device limit', result['details'])

    def test_operations_exceeded(self):
        # Exceed operations per batch (device can do 40 TOPS = 40000 billion/sec)
        memory_usage_mb = 4000
        total_operations_billion = 50000  # 50,000 billion (50 TOPS)
        inference_time_ms = 100
        result = compare_to_device_capabilities(memory_usage_mb, total_operations_billion, inference_time_ms)
        self.assertTrue(result['memory_ok'])
        self.assertFalse(result['operations_ok'])
        self.assertTrue(result['inference_time_ok'])
        self.assertIn('Operations per batch', result['details'])
        self.assertIn('exceeds device throughput', result['details'])

    def test_inference_time_exceeded(self):
        # Exceed inference time
        memory_usage_mb = 4000
        total_operations_billion = 1000
        inference_time_ms = 1500  # 1.5 sec
        result = compare_to_device_capabilities(memory_usage_mb, total_operations_billion, inference_time_ms)
        self.assertTrue(result['memory_ok'])
        self.assertTrue(result['operations_ok'])
        self.assertFalse(result['inference_time_ok'])
        self.assertIn('Estimated inference time', result['details'])
        self.assertIn('exceeds 1 second', result['details'])

    def test_multiple_limits_exceeded(self):
        # Exceed all
        memory_usage_mb = 9000
        total_operations_billion = 50000
        inference_time_ms = 1500
        result = compare_to_device_capabilities(memory_usage_mb, total_operations_billion, inference_time_ms)
        self.assertFalse(result['memory_ok'])
        self.assertFalse(result['operations_ok'])
        self.assertFalse(result['inference_time_ok'])
        self.assertIn('Memory usage', result['details'])
        self.assertIn('Operations per batch', result['details'])
        self.assertIn('Estimated inference time', result['details'])

if __name__ == '__main__':
    unittest.main()
