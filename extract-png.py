# coding=utf-8
import os
import subprocess
import struct
import argparse
import numpy as np
from PIL import Image

parser = argparse.ArgumentParser(
    description='Embed and expand the AI model in a PNG file.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument('--file', metavar='PATH', type=str, required=True, help='Input file')
args = parser.parse_args()

if not args.file.lower().endswith('.png'):
    with open(args.file, mode='rb') as fin:
        ba = fin.read()
    a = np.array(list(ba), dtype=np.uint8)
    l = a.shape[0] + 4
    s = int(np.ceil(np.sqrt(l/3+1)))
    b = np.random.randint(0, 255, s*s*3).astype(np.uint8)
    b[0:4] = np.array(list(struct.pack('<I',l)), dtype=np.uint8)
    b[4:l] = a
    b = b.reshape((s,s,3))
    i = Image.fromarray(b)
    i.save("output.png", format="png")
else:
    i = Image.open(args.file)
    b = np.asarray(i).reshape(i.width*i.height*3)
    l = struct.unpack('i',bytearray(b[0:4]))[0]
    a = b[4:l]
    with open('tmp.tar.bz2', mode='wb') as fw:
        fw.write(a)
    subprocess.run(('tar','xvfj','tmp.tar.bz2'))
    os.remove('tmp.tar.bz2')
