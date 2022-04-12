import random
import csv


def sample():
    needed = 2000 / 32000

    selected_rows = []

    with open("spotify_songs.csv") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if random.random() > needed:
                continue

            row["decade"] = row["track_album_release_date"][:2] + "00"
            selected_rows.append(row)

    keys = selected_rows[0].keys()
    with open("spotify_sample.csv", "w", newline="") as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(selected_rows)


if __name__ == "__main__":
    sample()
