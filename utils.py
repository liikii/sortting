from random import sample

def get_random_array():
    # length = 10
    return sample(range(1, 100), 10)



if __name__ == '__main__':
    print(get_random_array())
