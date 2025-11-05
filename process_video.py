# converts the videos to mp3
import os
import subprocess
files=os.listdir("videos")
for file in files:
    if "Tutorial #" in file:
        num = file.split("Tutorial #")[1].split(".")[0]
        name = file.split(" _ Sigma")[0]
        print(f"Tutorial #{num}: {name}")
    else:
        print("Other File:", file)
    subprocess.run(["ffmpeg", "-i", f"videos/{file}", f"audios/{num}_{name}.mp3"])