import math

print("각도\tsin값\tcos값")
for deg in range(0, 91, 10):
    rad = deg * (math.pi / 180)
    s = math.sin(rad)
    c = math.cos(rad)
    print(f"{deg}\t{s:.3f}\t{c:.3f}")