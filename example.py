# this script scrapes results from roll no 18AG1A0401 to 18AG1A0410

from jnturesultscrap import JNTUResult
import time
import json
from tqdm import tqdm
main_res_dict = {}


def rollify(int_num):
    if(int_num < 100):
        stringified = str(int_num)
        hexstr = stringified.zfill(2)
    else:
        hexstr = str(hex(int_num))[2:]
    rnopadded = "18AG1A04" + hexstr
    return rnopadded


for i in tqdm(range(1, 9)):
    result = JNTUResult(f"17AG1A04H{i}", 1463).JNTUResultAPI()
    main_res_dict[f"17AG1A04H{i}"] = result
    time.sleep(3)

print(main_res_dict)
