import cv2

from tqdm import tqdm

def generate_frames():
    FPS = 30
    count = 0
    vidcap = cv2.VideoCapture("data/video.mp4")
    total_frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

    for i in tqdm(range(total_frames)):
        vidcap.set(cv2.CAP_PROP_POS_MSEC, (count * 1000))

        _, image = vidcap.read()
        cv2.imwrite(f"data/frames/bmp/frame_{i}.bmp", image)

        count += 1 / FPS


if __name__ == "__main__":
    generate_frames()
