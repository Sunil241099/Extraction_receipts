Receipt Data Extractor

Overview :
This Python script uses the Gemini AI model to automatically extract key information from receipt images. It processes multiple image files and generates a JSON output with structured receipt data.

Features :
- Supports JPEG and JPG image formats
- Extracts key receipt details:
  - Company Name
  - Address
  - Date
  - Total Amount
- Generates a comprehensive JSON output file
- Tracks processing time for each receipt


Prerequisites:

The vision model here we use is "gemini-1.5-flash-8b-exp-0924".

Dependencies
- Python 3.8+
- google-generativeai library
- pathlib
- json
- time



 Configuration

API Key:
- Replace API with your own Google Generative AI API key


Folder Path
- Set the folder path variable to the directory containing your receipt images
- Supported image formats: .jpg, .jpeg


Output
- Generated file: `receipts_final.json`
- JSON structure for each receipt:
  {
    "company_name": "###",
    "address": "####", 
    "date": "###",
    "total": "###",
    "file_name": "###",
    "processing_time": "###"
  }


Error Handling
- Script will continue processing if an individual image fails
- Errors are printed 
- Successfully processed receipts are saved


Performance
- Includes processing time tracking for each receipt
- Adds a small delay between image processing to manage API rate limits
