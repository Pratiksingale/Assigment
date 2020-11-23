import csv

emps = []


def read_records():
    global emps
    with open("emp.csv") as f:
        rows = csv.DictReader(f)
        emps = [x for x in rows]


def correct_types():
    for e in emps:
        e['age'] = int(e['age'])


# average employee age
def find_average_age():
    avg_age = sum([x['age'] for x in emps]) / len(emps)
    return avg_age


# TODO:: implement this
def find_average_age_for_dept(dept):
    return 0.0


def main():
    read_records()
    correct_types()
    print("Average emp age is:", find_average_age())

    print("Average emp age for dept d1:", find_average_age_for_dept("d1"))
    print("Average emp age for dept d2:", find_average_age_for_dept("d2"))

    # TODO: Do same thing with json file instead of csv file


if __name__ == "__main__":
    main()
