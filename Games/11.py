import os

for i in range(1, 100):
    dir_path = f"Games/Day{i+1}"  # Proper string formatting
    if os.path.exists(dir_path) and os.path.isdir(dir_path):
        try:
            os.rmdir(dir_path)
            print(f"Removed: {dir_path}")
        except OSError as e:
            print(f"Error removing {dir_path}: {e}")
