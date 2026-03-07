from datetime import datetime

# Базовый класс медиафайлов

class MediaFile:
    def __init__(self, name: str, size: int, created_at: datetime, owner: str):
        self.name = name
        self.size = size
        self.created_at = created_at
        self.owner = owner
        print(f"{self.name} создан")

    def save(self, storage):
        storage.save(self)

    def delete(self):
        print(f"{self.name} удалён")

# Аудио

class AudioFile(MediaFile):
    def __init__(self, name, size, created_at, owner, duration: int, bitrate: int):
        super().__init__(name, size, created_at, owner)
        self.duration = duration
        self.bitrate = bitrate

    def convert_to_mp3(self):
        print(f"{self.name} конвертирован в mp3")

# Видео

class VideoFile(MediaFile):
    def __init__(self, name, size, created_at, owner, resolution: str, framerate: float):
        super().__init__(name, size, created_at, owner)
        self.resolution = resolution
        self.framerate = framerate

    def convert_to_mp4(self):
        print(f"{self.name} конвертирован в mp4")

# Картинка

class PhotoFile(MediaFile):
    def __init__(self, name, size, created_at, owner, dimensions: str, camera_model: str):
        super().__init__(name, size, created_at, owner)
        self.dimensions = dimensions
        self.camera_model = camera_model

    def apply_filter(self, filter_name: str):
        print(f"Фильтр {filter_name} применён к {self.name}")