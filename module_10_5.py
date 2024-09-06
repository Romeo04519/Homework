import datetime
import multiprocessing
#
def read_info(name):
    all_data = []
    with open(name, 'r') as fl:
        data = fl.readline()
        while data:
            data = fl.readline()
            all_data.append(data[0:-1])


filenames = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':
    start = datetime.datetime.now()
    for name in filenames:
        read_info(name)
    end = datetime.datetime.now()
    print(end - start)

    start = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(end-start)






