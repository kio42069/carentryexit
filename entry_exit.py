# Car entry-exit system : Managing entry and exit using MySql
# returns -1 when database cannot be reached, or any other kind of error occurs
# returns 1 when action has been successfully been performed
# returns 0 when action was deliberately not performed due to record already existing

# S.No        Car Number        Timestamp of entry        Gate of entry        status(bool)        Time of exit        gate of exit


import mysql.connector as msq
from datetime import datetime as dt
import time

db = msq.connect(
    host = "localhost",
    user = "root",
    password = "nikm",
    database = "carentryexit"
)

cur = db.cursor()

def enter(car_number, curr_time, entry_gate):
    status = check_status(car_number)
    if status == -1:
        return -1
    elif status == 1:
        return 0
    elif status == 0:
        try:
            command = f"insert into systum(car_number, timestamp_of_entry, status) values('{car_number}', '{curr_time}', {entry_gate});"
            cur.execute(command)
            db.commit()
            return 1
        except:
            return -1



def exit(car_number, curr_time, exit_gate):
    status = check_status(car_number)
    if status == -1:
        return -1
    elif status == 0:
        return 0
    elif status == 1:
        try:
            command = f"update systum set status = 0, timestamp_of_exit = '{curr_time}' where car_number = '{car_number} where gate_of_exit={exit_gate}'"
            cur.execute(command)
            db.commit()
            return 1
        except:
            return -1
    

def check_status(car_number):
    try:
        command = f"select status from systum where car_number = '{car_number}';"
        cur.execute(command)
        records = []
        for i in cur:
            records.append(i)
        if len(records) == 0:
            return 0
        elif records[-1][0] == 1:
            return 1
        else:
            return 0
    except:
        return -1
    

start = time.time()
enter("DL1CX2621", str(dt.now()),)
end = time.time()
print(end-start)

exit("DL1CX2621", str(dt.now()))
