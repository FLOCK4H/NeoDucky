# detect_os.py
import os
import gc

def detect_os_by_sys():
    try:
        files = os.listdir("/")
        # macOS-specific files start with '_'
        mac_specific_files = [file for file in files if file.startswith('_')]
        
        if mac_specific_files:
            print("macOS detected based on filesystem artifacts.")
            return "macOS"
        else:
            print("Non-macOS OS detected or unable to determine OS from filesystem artifacts.")
            return "Other"
    except Exception as e:
        print(f"Exception caught: {e}")
        return "Other"
        
def load_payload_from_file():
    try:
        loaded = []
        tools_dir = os.listdir('tools')
        payloads = ["payload.txt", "payload_mac.txt"]
        
        for p in payloads:
            if p in tools_dir:
                with open(f'tools/{p}', 'r') as f:
                    processed_payload = ''
                    for line in f:
                        processed_line = line.strip().rstrip(';').replace('\\n', '\n').replace('\\t', '\t')
                        processed_payload += processed_line
                    loaded.append({p: processed_payload})
                    gc.collect()
            else:
                print(f"{p} is missing from the tools folder.")
                
        if not loaded:
            print("No payloads loaded. Ensure payload files are present in the tools folder.")
            
        return loaded
    except OSError as e:
        print(f"Failed to load payloads: {str(e)}")
        return []

