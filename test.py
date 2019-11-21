import os

safe_dir = os.path.dirname(os.path.realpath(__file__))
print(safe_dir)

local_request = "/test/test2/printthis.txt"
requested_path = safe_dir + local_request

if safe_dir not in requested_path:
    print("Bad user")
else:
    print("Good User")
    testFile = open(requested_path)
    print(testFile.read())
    testFile.close()
    