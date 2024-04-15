import algorithms

def test_KK():
    A = [10,8,7,6,5]
    print(algorithms.karmarkar_karp(A))

def test_repeated_random():
    A = [10,8,7,6,5]
    print(algorithms.repeated_random(A,15))

if __name__ == "__main__":
    test_KK()
    test_repeated_random()

