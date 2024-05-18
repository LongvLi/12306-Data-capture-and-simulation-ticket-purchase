from book_ticket import book_tickets
from get_train_info import getTrainInfo


def main():
    start_station = input("初始站:")
    end_station = input("终点站:")
    start_date = input("出发时间:")

    train_dict = getTrainInfo(start_station, end_station, start_date)

    book_tickets(start_station, end_station, start_date)


if __name__ == "__main__":
    main()