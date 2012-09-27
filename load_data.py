import csv
import redis
import sys

client = redis.Redis()


def process_row(row):
    # Populate the Loan hash
    client.hmset("Loan::%s" % row['Loan ID'], row)

    # Add to the list of all user IDs
    client.sadd("Users::", row['Screen Name'])

    client.lpush("User::%s::Loans" % row['Screen Name'], row['Loan ID'])

if __name__ == "__main__":
    map(process_row, csv.DictReader(open(sys.argv[1])))
