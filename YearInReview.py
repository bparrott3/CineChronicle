import time


def main():
    while True:
        with open('start_file.txt', 'r') as infile:
            line_start = infile.readline()
            if line_start != "":
                break
        time.sleep(1)

    count = 0
    with open('movie_log.txt', 'r') as infile:
        for line in infile:
            data = line.strip().split(',')
            title, rating, date = data
            year = date.split('/')[-1]
            if year == line_start:
                count += 1
    with open('start_file.txt', 'w') as outfile:
        outfile.write(str(count))


if __name__ == "__main__":
    main()
