import os
from moviepy.editor import VideoFileClip

"""Creates a 1080x1920 video cut from a horizontally formatted video. Output resolution depends on input resolution."""

def video_lister(folder):
    items_list = os.listdir(folder)
    videos_list = [x for x in items_list if '.MP4' or '.mp4' in x]
    return videos_list

def cut_crop_resize(filename, folder, output_folder):
    video_path = os.path.join(folder, filename)
    video = VideoFileClip(video_path)
    w, h = video.size
    ratio = w/h
    new_w = round(h/ratio, 1)
    x = round((w/2) - (new_w/2), 1)
    outputpath = os.path.join(output_folder, filename)
    # Correctly takes a 1080p background video cuts it to time length, then crops and resizes it to proper dimensions for upload
    os.system(f"""ffmpeg -stats -i {video_path} -vf "crop={new_w}:{h}:{x}:0,scale=1080:1920" {outputpath}""")
    return outputpath

def video_editor():
    home_dir = os.curdir
    folderpath = input("Welcome to video CutCropResize, place the full path to the folder you'd like to cut here:  ")
    if folderpath:
        os.chdir(folderpath)
    else:
        raise FileNotFoundError
    
    try:
        videos_list = video_lister(folderpath)
        cuts_folder = os.mkdir("vertical_cuts")
        output_folder = f"{folderpath}/vertical_cuts"
        
        for video in videos_list:
            cut_crop_resize(video, folderpath, output_folder)
        
        os.chdir(home_dir)
        print("All videos cut and resized.")

    except Exception as e:
        print(e)
        os.chdir(home_dir)


video_editor()