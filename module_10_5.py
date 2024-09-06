import datetime
import multiprocessing
#
def read_info(name):
    all_data = []
    with open(name, 'r') as fl:
        while fl.readline() != '':
            s = fl.readline()
            all_data.append(s)
#
# start = datetime.datetime.now()
filenames = [f'./file {number}.txt' for number in range(1, 5)]
# for name in filenames:
#     read_info(name)
# end = datetime.datetime.now()
# print(end-start)


if __name__ == '__main_':
    start = datetime.datetime.now()
    with multiprocessing.Pool(processes=2) as pool:
        filenames = [f'./file {number}.txt' for number in range(1, 5)]
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(end-start)

