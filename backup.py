# Backup docker volume

from pathlib import Path
from zipfile import ZipFile


result = list(Path(".").rglob("*"))
result = [str(item) for item in result if item.parts[0].startswith('coffeemachine')]

with ZipFile('volumes.zip', 'w') as myzip:
    [myzip.write(file) for file in result]
