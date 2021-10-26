from barcode import EAN13
from barcode.writer import ImageWriter

with open(r'E:/barcode.png','wb') as f:
    EAN13('0123456789', writer=ImageWriter()).writer(f)
