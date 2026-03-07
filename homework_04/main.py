from datetime import datetime
from media_file import AudioFile, VideoFile, PhotoFile
from storage import LocalStorage, CloudStorage, RemoteStorage

now = datetime.now()

audio = AudioFile("song.wav", 5000, now, "Liza", duration=180, bitrate=320)
video = VideoFile("movie.mkv", 200000, now, "Ivan", resolution="1920x1080", framerate=30.0)
photo = PhotoFile("photo.jpg", 3000, now, "Ivan", dimensions="4000x3000", camera_model="Canon EOS 550D")

local = LocalStorage()
cloud = CloudStorage()
remote = RemoteStorage()

audio.save(local)
video.save(cloud)
photo.save(remote)

audio.convert_to_mp3()
video.convert_to_mp4()
photo.apply_filter("monochrome")