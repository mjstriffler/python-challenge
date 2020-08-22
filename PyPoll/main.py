# Import modules
import os
import csv

# Define variables
voters_candidates = []
votes_per_candidate = []

# Open and read csv
election_data = os.path.join("resources", "election_data.csv")


# Open and read csv
with open(election_data, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

# Read the header row first
    csv_header = next(csvfile)

print(f"Header: {csv_header}")