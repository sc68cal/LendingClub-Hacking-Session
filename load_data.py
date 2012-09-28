import csv
import redis
import sys

client = redis.Redis(host=sys.argv[2])


def process_row(pipe, row):
    if row:
        # Populate the Loan hash
        pipe.hmset("Loan::%s" % row['Loan ID'], row)

        # Add to the list of all user IDs
        pipe.sadd("Users::", row['Screen Name'])

        pipe.lpush("User::%s::Loans" % row['Screen Name'], row['Loan ID'])
        pipe.execute()

if __name__ == "__main__":
    with client.pipeline(transaction=False) as pipe:
        for row in csv.DictReader(open(sys.argv[1])):
            process_row(pipe, row)
