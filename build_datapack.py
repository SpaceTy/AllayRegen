#!/usr/bin/env python3
"""
Allay Regeneration Datapack Builder
Creates a zip file of the datapack for easy distribution
"""

import os
import zipfile
import shutil
from pathlib import Path

def build_datapack():
    """Build the allay regeneration datapack into a zip file"""
    
    # Configuration
    datapack_name = "allayregen"
    output_zip = f"{datapack_name}_datapack.zip"
    
    # Files and directories to include
    files_to_include = [
        "pack.mcmeta",
        "data/allayregen/functions/tick.mcfunction",
        "data/allayregen/functions/regenerate_allays.mcfunction", 
        "data/allayregen/functions/load.mcfunction",
        "data/minecraft/tags/functions/tick.json",
        "data/minecraft/tags/functions/load.json"
    ]
    
    print(f"🎮 Building {datapack_name} datapack...")
    
    # Create zip file
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        
        for file_path in files_to_include:
            if os.path.exists(file_path):
                # Add file to zip with relative path structure
                zipf.write(file_path, file_path)
                print(f"  ✅ Added: {file_path}")
            else:
                print(f"  ❌ Missing: {file_path}")
    
    # Get file size
    zip_size = os.path.getsize(output_zip)
    zip_size_mb = zip_size / (1024 * 1024)
    
    print(f"\n🎉 Datapack built successfully!")
    print(f"📦 Output: {output_zip}")
    print(f"📏 Size: {zip_size_mb:.2f} MB")
    print(f"\n📋 Installation:")
    print(f"1. Extract {output_zip} to your world's datapacks folder")
    print(f"2. Run /reload in-game")
    print(f"3. Enjoy your regenerating allays! ✨")

if __name__ == "__main__":
    build_datapack() 