import os
import shutil

path = "/Users/Aashish/Desktop/Whitehat Jr/Python/InitialProjects"

days = 0
time.time(days)

if(os.path.exists(path)):
    os.walk(path)
    os.path.join()

    ctime = os.stat(path).st_ctime
    return ctime

    os.remove(path)

else:
    print("Not Found")


