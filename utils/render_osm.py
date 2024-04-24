import py7zr
import os
from tileclipper import TileClipper

folder = 'balka/'

base_url = "http://0.0.0.0:8080/tile/{z}/{x}/{y}.png"  # Replace with your tile>
bbox = [41.085434,46.289071,41.710281,46.527690]  # Replace with bounding box c>
max_workers = 10  # Optional: Set maximum workers for concurrent downloads

tileclipper = TileClipper(base_url, bbox, folder, max_workers)
tileclipper.download_tiles(1, 17)

for fname_z in os.listdir(folder):
    for fname_x in os.listdir(folder + fname_z):
        for fname_y in os.listdir(folder + fname_z + '/' + fname_x):
            os.rename(folder + fname_z + '/' + fname_x + '/' + fname_y,
                folder + f'osm_100-l-8-{fname_z}-{fname_x}-{fname_y}')
        os.rmdir(folder + fname_z + '/' + fname_x)
    os.rmdir(folder + fname_z)

with py7zr.SevenZipFile("balka.7z", 'w') as archive:
    archive.writeall("balka/")
    