import argparse
import hashlib
from barcode import Code128
from barcode.writer import ImageWriter

parser = argparse.ArgumentParser()
parser.add_argument("content", type=str)
parser.add_argument("output", type=str)
args = parser.parse_args()

hash_str = hashlib.md5(args.content.encode()).hexdigest()
print("Content- ", args.content)
print("Hash- ", hash_str)

barcode = Code128(hash_str, writer=ImageWriter())

with open(args.output, "wb") as f:
    barcode.write(f)
