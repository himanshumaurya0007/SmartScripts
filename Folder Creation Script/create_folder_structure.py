import os

def create_folder_structure():
    base_folder = 'sem8'
    sub_folders = ['aai', 'aifba', 'rs', 'pm']
    inner_folders = ['m1', 'm2', 'm3', 'm4', 'm5', 'm6']
    
    # Create the base folder if it doesn't exist
    if not os.path.exists(base_folder):
        os.makedirs(base_folder)
    
    # Create subfolders and inner folders
    for sub in sub_folders:
        sub_path = os.path.join(base_folder, sub)
        os.makedirs(sub_path, exist_ok=True)
        
        for inner in inner_folders:
            inner_path = os.path.join(sub_path, inner)
            os.makedirs(inner_path, exist_ok=True)
    
    print("Folder structure created successfully!")

if __name__ == "__main__":
    create_folder_structure()