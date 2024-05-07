# count num's 1 bit
def count_bits(num):
    count = 0
    while num:
        count += num & 1 # check whether num's lowest bit is 1
        num >>= 1 # shift num over right
    return count

X = int(input())
print(count_bits(X))