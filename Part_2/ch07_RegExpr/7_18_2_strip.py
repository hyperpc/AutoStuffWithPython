#! python3

# strip(argv1[, argv2])
# - trim space character, if argv2 not set
# - trim argv2 in argv1, if argv2 set

import re

def strip(argv1, argv2):
    if argv2 == None:
        return argv1.strip()
    if len(argv2) == 0:
        return argv1.strip()
    argv2Regex = re.compile(argv2)
    result = argv2Regex.sub('', argv1)
    return result
argv = strip('  Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.', 'Agent ')
print(argv)
argv = strip('  Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.', '')
print(argv)
argv = strip('  Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.', None)
print(argv)