import torch

def calculate_brightness(img):
    if len(img) == 0:
        return -1

    row_len = len(img[0])
    if row_len == 0:
        return -1

    for row in img:
        if len(row) != row_len:
            return -1

    pixels = torch.tensor(img, dtype=torch.float32)

    if torch.any(pixels < 0) or torch.any(pixels > 255):
        return -1

    return round(pixels.mean().item(), 2)

if __name__ == '__main__':
    print(calculate_brightness([]), -1)
    print(calculate_brightness([
        [100, 200],
        [50, 150]
    ]), 125.0)
    print(calculate_brightness([[100, 300]]), -1)
    print(calculate_brightness([[128]]), 128.0)