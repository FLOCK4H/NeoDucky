# detect_os.py
import os

def detect_os_by_files():
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