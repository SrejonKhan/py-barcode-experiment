import argparse
from pyzbar.pyzbar import decode
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument("input", type=str)
args = parser.parse_args()

barcode_img = Image.open(args.input)

results = decode(barcode_img)

print(results[0].data)
