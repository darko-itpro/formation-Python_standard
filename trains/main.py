from pathlib import Path

working_file = Path(__file__).parent.parent / "assets" / "SNCF" / "comptage-voyageurs-trains-transilien.csv"

def csv_file_loader(file_path):
    with open(file_path) as train_file:
        train_file.readline()

        for line in train_file:
            station, station_code, day_type, year, count_date, train_line, day_time, count = line.split(';')

            yield station, station_code, day_type, int(float(year)), count_date, train_line, day_time, int(count)

info_lines = {}

for data in csv_file_loader(working_file):
    train_line = data[5]
    if train_line not in info_lines:
        info_lines[train_line] = []

    info_lines[train_line].append(data)

for train_line, data in info_lines.items():
    print(train_line, len(data))
    stations = [info[0] for info in data]
    for station in list(set(stations)):
        print(f"    - {station}")