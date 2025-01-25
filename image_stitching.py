import cv2
import glob
import os

# Load all images from the specified folder
folder_path = r"/home/edhitha/Downloads/Runway/"
image_paths = sorted(glob.glob(os.path.join(folder_path, "*.jpg")))[:2]  # Use first 2 images

# Print paths found
print(f"🖼️ Found {len(image_paths)} images")
print(image_paths)  # Print the file paths to check if they exist

# Check if at least 2 images are found
if len(image_paths) < 2:
    print("❌ Error: Need at least 2 images for stitching!")
    print("📂 Directory Content:", os.listdir(folder_path))  # Print directory content for debugging
    exit()

# Load images
images = []
for img_path in image_paths:
    img = cv2.imread(img_path)
    if img is None:
        print(f"❌ Error: Image {img_path} not loaded! Skipping...")
        continue
    print(f"✅ Loaded: {img_path} | Shape: {img.shape}")
    images.append(img)

# Check if we have enough valid images
if len(images) < 2:
    print("❌ Error: Not enough valid images for stitching.")
    exit()

# Resize images to prevent memory issues
print("🔄 Resizing images...")
images = [cv2.resize(img, (800, 600)) for img in images]

# Create Stitcher object
stitcher = cv2.Stitcher_create()

# Perform stitching
print("🛠️ Stitching images...")
status, panorama = stitcher.stitch(images)

# Check if stitching was successful
if status == cv2.Stitcher_OK:
    print("✅ Stitching successful! Saving output...")
    cv2.imwrite("stitched_output.jpg", panorama)
    cv2.imshow("Stitched Image", panorama)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print(f"❌ Error: Stitching failed with status code {status}")
