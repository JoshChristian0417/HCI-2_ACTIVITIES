import qrcode
from qrcode.constants import ERROR_CORRECT_H
from itertools import permutations, zip_longest


# Part 1 — QR Code Generator

student_info = "Pareno, Christian Joshua — BSIT 3A"

qr = qrcode.QRCode(
    version=1,
    error_correction=ERROR_CORRECT_H,
    box_size=12,
    border=4,
)

qr.add_data(student_info)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("my_qr.png")

print("=== Part 1: QR Code Generator ===")
print("Student Info:", student_info)
print("QR code saved as 'my_qr.png'\n")


# Part 2 — itertools Permutations

items = ["Touch", "Sound", "Vision", "Motion"]

all_permutations = list(permutations(items))

print("=== Part 2: itertools Permutations ===")
print("Total number of permutations:", len(all_permutations))
print("First 5 permutations:")

for permutation in all_permutations[:5]:
    print(permutation)

print()


# Part 3 — Itertools Chunker

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


modules = list(range(1, 8))

print("=== Part 3: Itertools Chunker ===")
print("Modules:", modules)
print("Chunks:")

for chunk in grouper(modules, 3):
    print(chunk)