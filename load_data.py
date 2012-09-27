import csv
import redis
import sys

client = redis.Redis()
map(lambda x: client.hmset("LOAN::%s" % x['Loan ID'], x),
    csv.DictReader(open(sys.argv[1])))
