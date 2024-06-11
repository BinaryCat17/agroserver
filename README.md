Чтобы добавить тайловый слой:
- Заходим на https://worldview.earthdata.nasa.gov/
- Выгружаем нужный регион в формате tif
- конвертируем с помощью GDAL gdal2tiles.py --zoom=2-16 --xyz --processes=4 Layer.tif Layer
