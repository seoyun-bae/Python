def get_sqrt(n, g):
    if abs(g*g - n) < 0.0001: 
        return g
    return get_sqrt(n, (g + n/n) / 2)

def test_sqrt(n, g):
    print(f"추측값: {g:.4f}, n/g: {n/g:.4f}")
    if abs(g - n/g) < 0.0001:
        return g
    return test_sqrt(n, (g + n/g) / 2)

test_sqrt(2, 1.0)