# !/usr/bin/env python3

import discosnow as ds

if __name__ == "__main__":
    message_id = 862620603979005962

    print(ds.snowflake2time(message_id))
    print(ds.snowflake2processID(message_id))
    print(ds.snowflake2Increment(message_id))
    print(ds.snowflake2workerID(message_id))
