import os

"""Turns .m4a files into .mp3 files in comparable bitrates."""

def audio_lister(folder):
    items_list = os.listdir(folder)
    audio_list = [x for x in items_list if '.m4a' or '.M4A' in x]
    return audio_list
 
def convert_to_mp3(folderpath, audio_list):
    for file in audio_list:
        path = os.path.join(folderpath, file)
        outputpath = (str(path)).split(".")[0]
        os.system(f"ffmpeg -i {path} -c:v copy -c:a libmp3lame {outputpath}.mp3")
        print(f"{file} Converted to MP3")

def converter():
    home_directory = os.curdir
    folder_path = input("This app takes .m4a files and converts them to .mp3 files in batches. Paste the path to the folder here:   ")
    files = audio_lister(folder_path)
    convert_to_mp3(folder_path, files)
    print("Process Complete")

converter()