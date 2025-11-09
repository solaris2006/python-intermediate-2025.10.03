# practice with data 2

# task:
# să vedem pe fiecare oră traficul total

import re
import gzip
import csv
from datetime import datetime


_log_line_re = r'\[(?P<date>[^\]]+)\] "(?P<request>[^"]+)" (?P<status>[0-9]+) (?P<size>[0-9]+|-)'
log_line_re = re.compile(_log_line_re)


def process_log(iterable):
    prev_hour = None
    total_size = 0

    for line in iterable:
        # spargem primele câmpuri după spațiu 

        ip, _ident, _user, reminder = line.split(" ", 3)

        # și următoarele după regexp


        match = log_line_re.match(reminder)

        if not match:
            # problem here, we would normally log the line
            # because either problem with our code,
            # or with the data
            # 
            print("warning, bad data", line)

            continue

        fields = match.groupdict()

        if fields['size'] == '-':
            # for some reason, empty size
            continue

        dt = datetime.strptime(fields['date'], "%d/%b/%Y:%H:%M:%S %z")

        size = int(fields['size'])

        current_hour = (
            dt.date(),
            dt.time().replace(minute=0, second=0)
        )

        if prev_hour != current_hour:
            if prev_hour is not None:
                yield (
                    datetime.combine(*current_hour),
                    total_size
                )

            prev_hour = current_hour
            # we re-initialize the size counter
            total_size = size

    # don't forget about the final data

    yield (
        datetime.combine(*current_hour),
        total_size
    )


with gzip.open("data/httpd.access.log.gz", "rt") as logf, \
     open("access_report.csv", "w") as csvf:
    writer = csv.writer(csvf)

    for data in process_log(logf):
        writer.writerow(data)

