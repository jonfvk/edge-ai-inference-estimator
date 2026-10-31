class JetsonOrinNano2Specs:
    """
    Hardware specification for NVIDIA Jetson Orin Nano 2.
    Reference: https://techgig.com/news/ai/nvidia-unveils-jetson-orin-nano-2-for-edge-ai-robotics/134930001 (retrieved 2024-06-10)
    """
    NAME = "Jetson Orin Nano 2"
    MEMORY_MB = 8192  # 8 GB LPDDR5
    MAX_TOPS = 40.0   # 40 TOPS (Tera Operations Per Second)
    CPU = "6-core ARM Cortex-A78AE v8.2 64-bit CPU"
    GPU = "NVIDIA Ampere architecture GPU with 1024 CUDA cores"
    MEMORY_TYPE = "LPDDR5"
    MEMORY_BANDWIDTH_GBPS = 68  # 68 GB/s
    STORAGE = "eMMC 5.1"
    POWER_WATT = 15  # Typical power consumption (approximate)

    @classmethod
    def summary(cls):
        return {
            "name": cls.NAME,
            "memory_mb": cls.MEMORY_MB,
            "max_tops": cls.MAX_TOPS,
            "cpu": cls.CPU,
            "gpu": cls.GPU,
            "memory_type": cls.MEMORY_TYPE,
            "memory_bandwidth_gbps": cls.MEMORY_BANDWIDTH_GBPS,
            "storage": cls.STORAGE,
            "power_watt": cls.POWER_WATT,
        }
