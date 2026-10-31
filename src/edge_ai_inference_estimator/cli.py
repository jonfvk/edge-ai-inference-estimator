import argparse

def parse_args(args=None):
    parser = argparse.ArgumentParser(
        description="Estimate AI inference workloads for edge devices."
    )
    parser.add_argument(
        '--model-size',
        type=float,
        required=True,
        help='Model size in megabytes (MB).'
    )
    parser.add_argument(
        '--input-size',
        type=float,
        required=True,
        help='Input data size per inference in kilobytes (KB).'
    )
    parser.add_argument(
        '--operations',
        type=float,
        required=True,
        help='Estimated number of operations per inference (in billions, e.g., 1.5 for 1.5e9).'
    )
    parser.add_argument(
        '--batch-size',
        type=int,
        default=1,
        help='Batch size for inference (default: 1).'
    )
    return parser.parse_args(args)

def main():
    args = parse_args()
    print(f"Model size: {args.model_size} MB")
    print(f"Input size: {args.input_size} KB")
    print(f"Operations: {args.operations} billion")
    print(f"Batch size: {args.batch_size}")

if __name__ == "__main__":
    main()
