#!/usr/bin/env python3
import os
import sys
import time

import requests
from tqdm import tqdm

pid_file = f"/app/logs/{os.environ['ID']}.pid"
while True:
    if os.path.exists(pid_file):
        with open(pid_file) as fin:
            pid = int(fin.read())
            break
    else:
        time.sleep(3)
        print("wait process ok")
print(f"pid={pid}")
port = os.environ['FULL_SYNC_HTTP_PORT'] if os.environ['SYNC_MODE'] == 'full' else os.environ['FULL_SYNC_HTTP_PORT']
print(f"wait for 127.0.0.1:{port} active")
end = False
with tqdm(total=100, file=sys.stdout) as pbar:
    while not end:
        try:
            rsp = requests.get(f"http://127.0.0.1:{port}/progress").json()
            total_collection_number = rsp["total_collection_number"]
            wait_collection_number = rsp["wait_collection_number"]
            metric = rsp["collection_metric"]
            total = 0
            cur = 0
            waiting = False
            for k, v in metric.items():
                _, _, progress = v.rpartition(" ")
                if progress == "-":
                    if not waiting:
                        # 尚未有进度的
                        print(f"waiting [{k}]")
                        waiting = True
                        total += 10000
                else:
                    lh, _, rh = progress[1:-1].partition("/")
                    cur += int(lh)
                    total += int(rh)
            if total == cur and total > 0:
                print("end")
                end = True
            if pbar.n != cur or pbar.total != total:
                pbar.total = total
                pbar.n = cur
                pbar.refresh()
        except Exception as e:
            print(str(e))
            pass
        finally:
            time.sleep(3)
            sys.stdout.flush()
while os.path.exists(pid_file):
    time.sleep(3)
    print("wait process exit")
