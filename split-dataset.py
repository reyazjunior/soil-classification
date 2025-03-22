import os
import shutil
from sklearn.model_selection import train_test_split

# Define the paths
dataset_dir = r"C:\Users\Danyal Reyaz\Documents\RUDRA\Soil Analysis Model\Soil types"
output_dir = r"C:\Users\Danyal Reyaz\Documents\RUDRA\Soil Analysis Model\dataset"

# Define the ratios
train_ratio = 0.7
val_ratio = 0.15
test_ratio = 0.15

# Create output directories if they don't exist
for split in ['train', 'val', 'test']:
    os.makedirs(os.path.join(output_dir, split), exist_ok=True)

# Loop through each class in the dataset
for class_name in os.listdir(dataset_dir):
    class_dir = os.path.join(dataset_dir, class_name)
    
    # Get the list of all images in the class folder
    images = os.listdir(class_dir)
    
    # Split images into train, val, and test
    train_images, test_images = train_test_split(images, test_size=(1 - train_ratio))
    val_images, test_images = train_test_split(test_images, test_size=(test_ratio / (val_ratio + test_ratio)))
    
    # Create class subdirectories in train, val, and test folders
    os.makedirs(os.path.join(output_dir, 'train', class_name), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'val', class_name), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'test', class_name), exist_ok=True)
    
    # Copy the images to the corresponding directories
    for image in train_images:
        shutil.copy(os.path.join(class_dir, image), os.path.join(output_dir, 'train', class_name, image))
        
    for image in val_images:
        shutil.copy(os.path.join(class_dir, image), os.path.join(output_dir, 'val', class_name, image))
        
    for image in test_images:
        shutil.copy(os.path.join(class_dir, image), os.path.join(output_dir, 'test', class_name, image))

print("Dataset split into train, val, and test successfully.")
