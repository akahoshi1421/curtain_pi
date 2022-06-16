import json
import subprocess

a=open("/home/pi/ドキュメント/Python_tests/moter.json","r",encoding="utf-8")
cond=json.load(a)
if cond == 1:
    subprocess.call("python3 /home/pi/ドキュメント/Python_tests/moter3.py".split())

elif cond == 0:
    subprocess.call("python3 /home/pi/ドキュメント/Python_tests/moter2.py".split())

a.close()