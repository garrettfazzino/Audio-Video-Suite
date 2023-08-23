from moviepy.editor import ImageSequenceClip
import os

"""Takes a sequence of pictures (for timelapse) and creates a final video from them"""

# Define the directory where the images are located
image_folder = "PATH/TO/FOLDER/HERE"

# Get the names of all the jpeg images in the folder
image_files = [image_folder + file_name for file_name in os.listdir(image_folder) if file_name.endswith('.JPG')]

# Sort the images by name
x = list(sorted(image_files))
images_list = x[::2]

# Create a clip from the images
clip = ImageSequenceClip(images_list, fps=60)  # Change fps for frame per second rate

# Write the clip to a file
clip.write_videofile("NAME_OF_FILE_HERE.mp4", codec='libx264')

# Close the clip
clip.close()