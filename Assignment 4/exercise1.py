"""
    CRC collision detector
"""


def get_input():
    try:
        divisor = input("Divisor (bits): ").strip()
        data = input("Data (bits): ").strip()
        if not all(c in '01' for c in divisor + data):
            raise ValueError
    except ValueError:
        raise ValueError("Input must be binary strings.")
    return divisor, data


def xor(a, b):
    return ''.join('0' if a[i] == b[i] else '1' for i in range(len(a)))


def crc(data, divisor):
    padded = data + '0' * (len(divisor) - 1)
    remainder = padded[:len(divisor)]

    for bit in padded[len(divisor):]:
        if remainder[0] == '1':
            remainder = xor(remainder, divisor)
        remainder = remainder[1:] + bit

    if remainder[0] == '1':
        remainder = xor(remainder, divisor)

    return remainder


def find_collisions(target_data, divisor, n=2):
    target_crc = crc(target_data, divisor)
    collisions = []
    for i in range(2**len(target_data)):
        candidate = format(i, f'0{len(target_data)}b')
        if candidate != target_data and crc(candidate, divisor) == target_crc:
            collisions.append(candidate)
        #if len(collisions) == n:
        #   break
    return collisions


if __name__ == "__main__":
    divisor, data = get_input()
    checksum = crc(data, divisor)
    print(f"CRC checksum: {checksum}")
    collisions = find_collisions(data, divisor)
    print(f"Collisions: {collisions}")