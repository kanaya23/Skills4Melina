import argparse
import os

# Configuration
OUTPUT_FILE = "compiled_codebase.txt"

# Only these top-level directories will be processed
ALLOWED_DIRS = {'persona', 'skills', 'tools', 'requirements'}

def compile_directory(surface_only=False):
    # Open the output file in write mode
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as outfile:
        
        # os.walk explores the current directory ('.') and all subdirectories
        for root, dirs, files in os.walk('.'):
            
            # If we are at the root level, restrict the directories we walk into
            if root == '.':
                dirs[:] = [d for d in dirs if d in ALLOWED_DIRS]
            
            # Format the folder path nicely to match your requested output
            rel_path = os.path.relpath(root, '.')
            folder_name = '/root' if rel_path == '.' else f"/{rel_path.replace(os.sep, '/')}"
            
            folder_printed = False

            for file in files:
                # Prevent the script from reading its own output file in an infinite loop
                if file == OUTPUT_FILE:
                    continue
                
                file_path = os.path.join(root, file)

                if surface_only:
                    # In surface mode, list file names only (no file contents).
                    if not folder_printed:
                        outfile.write(f"{folder_name}\n")
                        folder_printed = True
                    outfile.write(f"  {file}\n")
                    continue

                try:
                    # Attempt to read the file as standard text
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        content = infile.read()
                    
                    # Only print the folder name if we actually found a readable file inside it
                    if not folder_printed:
                        outfile.write(f"{folder_name}\n")
                        folder_printed = True
                    
                    # Write the filename with a 2-space indent
                    outfile.write(f"  {file}:\n")
                    
                    # Write the content with a 4-space indent
                    for line in content.splitlines():
                        outfile.write(f"    {line}\n")
                        
                    # Add a blank line between files for readability
                    outfile.write("\n")
                    
                except UnicodeDecodeError:
                    # If it's a binary file (images, compiled files, etc.), it will fail to decode. 
                    # We just skip it and move to the next file.
                    continue

            if surface_only and folder_printed:
                outfile.write("\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Compile selected folders into a single text output."
    )
    parser.add_argument(
        "--surface",
        action="store_true",
        help="Output only folder and file names without file contents.",
    )
    args = parser.parse_args()

    compile_directory(surface_only=args.surface)
    print(f"Done! Your codebase has been compiled into '{OUTPUT_FILE}'.")
