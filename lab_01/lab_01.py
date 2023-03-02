# Zad1
int_one = 5
int_two = int(0b100101)
print(int_one, int_two)
float_one = 3.1
float_two = float(-0b110100)
print(float_one, float_two)

# Zad2
int_bit = [1, 3]
float_ii = [3.2, 8.0]

for x in int_bit:
    if (n := x.bit_count()) > 1: #Python 3.10+
    #if (n := bin(x).count("1")) > 1:  # Python 3.9-
        print("Variable with value \"" + str(x) + "\" has more than 1 bit. Variable has " + str(n) + " bits.")
for x in float_ii:
    if x.is_integer():
        print("Variable with value \"" + str(x) + "\" could be an integer.")

# Zad3
bit_one = 0b1
bit_eight = 0b1000
print(bit_one, bit_one << 2)
print(bit_eight, bit_eight >> 3)
print(~bit_one, ~~bit_eight)
print(0b0 & 0b1, 0b1 & 0b1)
