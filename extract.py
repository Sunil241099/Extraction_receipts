import google.generativeai as genai
from pathlib import Path
import json
import time
# mention the API key 
genai.configure(api_key="your API key")
# initializing the model
model = genai.GenerativeModel(
    model_name="models/gemini-1.5-flash-8b-exp-0924",
    generation_config={
        "temperature": 0.2,
        "top_p": 1,
        "top_k": 32,
        "max_output_tokens": 4096,
    }
)
# read Images
def read_image(image_path):
    img = Path(image_path)
    return [{
        "mime_type": "image/jpeg",
        "data": img.read_bytes()
    }]
# extract data from image by sending images to model and getting resp[onse from the model
# Also get the response in Json format. Also Add the processing time and image path in the final Json.
def extract_receipt_data(image_path):
    start_time = time.time()
    
    image = read_image(image_path)
    
    prompts = [
        "You are a specialist in comprehending receipts. Please extract information and return it in valid JSON format.",
        image[0],
        """Extract and return ONLY valid JSON with this format:
        {
            "company_name": "company name here",
            "address": "full address here", 
            "date": "date here",
            "total": "total amount here"
        }"""
    ]
    
    response = model.generate_content(prompts)
    
    text = response.text.strip()
    if "```" in text:
        text = text.split("```")[1]
        if text.startswith("json"):
            text = text[4:]
    
    data = json.loads(text)
    data["file_name"] = str(image_path)
    data["processing_time"] = f"{time.time() - start_time:.2f} seconds"
    
    return data
# get the images from the specific folder of img format jpg and jpeg. 
#
def process_folder(folder_path):
    folder = Path(folder_path)
    image_files = sorted(list(folder.glob("*.jpg")) + list(folder.glob("*.jpeg")))
    total_images = len(image_files)
    
    print(f"Found {total_images} images in {folder_path}")
    
    results = []
    for i, image_path in enumerate(image_files, 1):
        try:
            print(f"Processing image {i}/{total_images}: {image_path.name}")
            data = extract_receipt_data(image_path)
            results.append(data)
            print(f"Done! Took {data['processing_time']}")
            time.sleep(0.5)
        except Exception as e:
            print(f"Error with {image_path.name}: {e}")
    
    with open("receipts_final.json", "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"\nCompleted! Processed {len(results)} receipts successfully")
    print(f"Results saved to receipts_final.json")

folder_path = r"C:\Users\sunilkumar.m03\Downloads\img"
process_folder(folder_path)