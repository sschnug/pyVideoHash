import hashlib
import numpy as np
from moviepy.editor import VideoFileClip
from frame_hash import FrameHash
from db_model import Video, add_video


def generate_file_md5(filename, blocksize=2**20):
    m = hashlib.md5()
    with open(filename, "rb") as f:
        while True:
            buf = f.read(blocksize)
            if not buf:
                break
            m.update(buf)
    return m.hexdigest()


def hash_frame(frame):
    f_hasher = FrameHash(frame)
    f_hasher.calculate_hash()
    return f_hasher.get_result()


if __name__ == '__main__':
    filepath = "output.avi"
    clip = VideoFileClip(filepath)
    clip_file_hash = generate_file_md5(filepath)

    frame_hash_values = []
    for f in clip.iter_frames(progress_bar=True):
        frame_hash_values.append(hash_frame(f))
    frame_hash_values = np.ravel(np.array(frame_hash_values, dtype=bool))

    add_video(clip_file_hash, np.getbuffer(frame_hash_values))
