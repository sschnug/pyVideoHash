from peewee import *

custom_db = SqliteDatabase('data.db')
custom_db.connect()


class BaseModel(Model):
    class Meta:
        database = custom_db


class Video(BaseModel):
    id = IntegerField(unique=True)

    file_hash = CharField()
    perceptual_hash = BlobField()


def iterate_videos():
    return Video.select()


def count_videos():
    return Video.select().count()


def add_video(file_hash, perceptual_hash):
    n_queries_before = count_videos()
    video = Video.create(id=n_queries_before, file_hash=file_hash, perceptual_hash=perceptual_hash)