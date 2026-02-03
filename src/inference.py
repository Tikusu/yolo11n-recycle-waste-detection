import argparse
import os
import sys
from ultralytics import YOLO
from PIL import Image

def run_inference(model_path, source, output, conf_threshold):
    """
    Loads a YOLO model and runs inference on a source (image, video, or directory).
    Saves the results with bounding boxes to the output directory.
    """
    
    if not os.path.exists(model_path):
        print(f"Error: Model not found at {model_path}")
        sys.exit(1)

    print(f"🔄 Loading model from: {model_path}...")
    try:
        model = YOLO(model_path)
    except Exception as e:
        print(f"Error loading model: {e}")
        sys.exit(1)

    print(f"🚀 Running inference on: {source}")
    print(f"⚙️ Confidence Threshold: {conf_threshold}")

    results = model.predict(
        source=source,
        conf=conf_threshold,
        save=True,
        project=None,
        name=output,
        verbose=True
    )

    save_path = os.path.join("runs/detect", output)
    print("-" * 50)
    print(f"✅ Inference complete!")
    print(f"📂 Results saved to: {os.path.abspath(save_path)}")
    print("-" * 50)

if __name__ == "__main__":
    # This block handles command-line arguments
    parser = argparse.ArgumentParser(description="Run YOLO11n Inference")
    
    parser.add_argument(
        "--model", 
        type=str,
        default="models/backbone-partial-freeze/best.pt",
        help="Path to the trained .pt model file (e.g., models/best.pt  default: models/backbone-partial-freeze/best.pt)"
    )
    
    parser.add_argument(
        "--source", 
        type=str, 
        required=True, 
        help="Path to an image, video, or directory of images"
    )
    
    parser.add_argument(
        "--output", 
        type=str, 
        default="predict", 
        help="Folder to save results (default: predict)"
    )
    
    parser.add_argument(
        "--conf", 
        type=float, 
        default=0.25, 
        help="Confidence threshold (0.0 to 1.0, default: 0.25)"
    )

    args = parser.parse_args()
    
    run_inference(args.model, args.source, args.output, args.conf)