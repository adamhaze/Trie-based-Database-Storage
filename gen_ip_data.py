#!/usr/bin/env python
# coding: utf-8

from random import randint, seed
import csv
import sys

seed(3)
population_size = sys.argv[1] if len(sys.argv) > 1 else 1e2
population_size = int(population_size)


def to_bin(ip):
    """
        Extends internal bin function to return 8 bit binary representation
        for a given number
        Example:
        bin(3) = 0b11
        to_bin(3)= 00000011
    """
    bit_str = str(bin(ip))[2:]
    pad_len = 8 - len(bit_str)
    bit_str = f"{pad_len*'0'}{bit_str}"

    return bit_str

def get_ip():
    ip_list = [randint(0, 255), randint(0, 255), randint(0, 255), randint(0, 255)]
    bit_vector = '.'.join(map(to_bin, ip_list))
    ip_addr = '.'.join(map(str, ip_list))

    return bit_vector, ip_addr

if __name__ ==  "__main__":
    with open('ip_list.csv', 'w', newline='') as csvfile:
        fieldnames = ['bit_str', 'ip_addr']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for _ in range(population_size):
            bit_str, ip_addr = get_ip()
            writer.writerow({"bit_str": bit_str, "ip_addr": ip_addr})

