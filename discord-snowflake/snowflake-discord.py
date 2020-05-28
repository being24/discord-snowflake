# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime


class snowflake_convert:
    def snowflake2time(self, snowflake, timezone):
        timestamp_bin = bin(snowflake >> 22)
        timestamp_dec = int(timestamp_bin, 0)
        timestamp_unix = (timestamp_dec + 1420070400000) / 1000
        timestamp = datetime.fromtimestamp(timestamp_unix, timezone)
        return timestamp

    def snowflake2workerID(self, snowflake):
        internal_workerID_bin = bin((snowflake & 0x3E0000) >> 17)
        internal_workerID_dec = int(internal_workerID_bin, 0)

        return internal_workerID_dec

    def snowflake2processID(self, snowflake):
        internal_processID_bin = bin((snowflake & 0x1F000) >> 12)
        internal_processID_dec = int(internal_processID_bin, 0)

        return internal_processID_dec

    def snowflake2Increment(self, snowflake):
        increment_bin = bin(snowflake & 0xFFF)
        increment_dec = int(increment_bin, 0)

        return increment_dec
