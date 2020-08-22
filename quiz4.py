#!/usr/bin/env python3.8

import re
def show_usercount(line):
    pattern = r"(^.*\d{2}:\d{2}:\d{2}).*\[(\d*)\]"
    result = re.search(pattern, line)
    if result != None:
        print(result.groups())
        return "{} pid:{}".format(result.group(1), result.group(2))
    return result

# print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440
# print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187
# print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187
# print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440
# print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807
# print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440
# print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:29440

usernames={}
def show_usercount(line):
    pattern = r"USER \((.*)\)"
    result = re.search(pattern, line)
    if result != None
        user = result.group(1)
        usernames[user] = usernames.get(user, 0) +1

show_usercount("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)") # Jul 6 14:01:23 pid:29440
show_usercount("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)") # Jul 6 14:02:08 pid:29187
show_usercount("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)") # Jul 6 14:02:09 pid:29187
show_usercount("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)") # Jul 6 14:03:01 pid:29440
show_usercount("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"") # Jul 6 14:03:40 pid:29807
show_usercount("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)") # Jul 6 14:04:01 pid:29440
show_usercount("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)") # Jul 6 14:05:01 pid:29440

print(usernames)
