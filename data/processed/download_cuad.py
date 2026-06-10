"""Download the full CUAD dataset from the official Atticus Project repository.

The full CUAD_v1.json (~39 MB) is NOT committed to this repo. Run this script
once to fetch and extract it into the data/ folder.

    python data/download_cuad.py

Source: https://github.com/TheAtticusProject/cuad  (Apache-2.0 licensed)
Mirror: https://zenodo.org/record/4595826
"""
import os
import urllib.request
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
ZIP_URL = "https://github.com/TheAtticusProject/cuad/raw/main/data.zip"
ZIP_PATH = os.path.join(HERE, "data.zip")


def main():
    print(f"Downloading CUAD data.zip from {ZIP_URL} ...")
    urllib.request.urlretrieve(ZIP_URL, ZIP_PATH)
    print("Extracting ...")
    with zipfile.ZipFile(ZIP_PATH) as z:
        z.extractall(HERE)
    os.remove(ZIP_PATH)
    print("Done. Files now in data/:")
    for f in sorted(os.listdir(HERE)):
        print("  -", f)


if __name__ == "__main__":
    main()
