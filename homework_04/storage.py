
class StorageBase:
    def save(self, file):
        pass

class LocalStorage(StorageBase):
    def save(self, file):
        print(f"{file.name} сохранён локально")

class CloudStorage(StorageBase):
    def save(self, file):
        print(f"{file.name} сохранён в облаке")

class RemoteStorage(StorageBase):
    def save(self, file):
        print(f"{file.name} сохранён на удалённом сервере S3")