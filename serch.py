import sys
import os
cz = 1
zz = 10000000000000000000000000000000000000000000000000000000000000000000000000
ci = 0
da = input("请输入你想让计算机二分查找的数：")
try:
    da = int(da)
except ValueError:
    print("？？？别输一些奇奇怪怪的东西")
    os.system("pause")
    sys.exit()
else:
    if da < cz or da > zz:
        print("？？？输一个1-1000000的整数")
        os.system("pause")
        sys.exit()
while cz <= zz:
    ci += 1
    cai = (cz+zz)//2
    if cai == da:
        print("猜第", ci, "次，猜", cai, "，猜对了！")
        break
    elif da < cai:
        print("猜第", ci, "次，猜", cai, "，猜大了")
        zz = cai - 1
    else:
        print("猜第", ci, "次，猜", cai, "，猜小了")
        cz = cai + 1
os.system("pause")
