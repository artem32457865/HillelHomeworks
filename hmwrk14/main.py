import time
import random
import threading


files = [
    "photo.jpg",
    "document.pdf",
    "video.mp4",
    "archive.zip",
    "music.mp3"
]


def download_file(file_name):
    print(f"Початок завантаження {file_name}...")

    time.sleep(random.randint(1, 3))

    print(f"Завершено: {file_name}")


start_time = time.perf_counter()

for file in files:
    download_file(file)

sequential_time = time.perf_counter() - start_time

print(f"\nПослідовне завантаження: {sequential_time:.2f} секунд")


start_time = time.perf_counter()

threads = []

for file in files:
    thread = threading.Thread(target=download_file, args=(file,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

parallel_time = time.perf_counter() - start_time

print(f"\nПаралельне завантаження: {parallel_time:.2f} секунд")


difference = sequential_time - parallel_time

print(f"Різниця: {difference:.2f} секунд")