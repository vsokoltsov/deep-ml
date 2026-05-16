def calculate_brightness(img):
    if len(img) == 0:
        return -1

    row_len = len(img[0])
    pxls_sum = 0

    for row in img:
        if row_len != len(row):
            return -1
        for pxl in row:
            if pxl < 0 or pxl > 255:
                return -1
            pxls_sum += pxl

    return pxls_sum / (row_len * len(img))


if __name__ == '__main__':
    print(calculate_brightness([]), -1)
    print(calculate_brightness([
        [100, 200],
        [50, 150]
    ]), 125.0)
    print(calculate_brightness([[100, 300]]), -1)
    print(calculate_brightness([[128]]), 128.0)
