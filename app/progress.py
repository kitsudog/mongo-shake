#!/usr/bin/env python3
from tqdm import tqdm
import time
import requests
import os

port=os.environ['FULL_SYNC_HTTP_PORT'] if os.environ['SYNC_MODE'] == 'full' else os.environ['FULL_SYNC_HTTP_PORT'] 
print(f"wait for 127.0.0.1:{port} active")
end=False
with tqdm(total=100) as pbar:
    while not end:
        try:
            metric = requests.get(f"http://127.0.0.1:{port}/progress").json()["collection_metric"]
            total=0
            sum=0
            waiting=False
            for k,v in metric.items():
                _,_,progress=v.rpartition(" ")
                if not waiting and progress == "-":
                    print(f"waiting [{k}]")
                    waiting=True
                    continue
                lh,_,rh=progress[1:-1].partition("/")
                sum+=int(lh)
                total+=int(rh)
            if total==sum and total>0:
                print("end")
                end=True
            if pbar.n != sum or pbar.total != total:
                pbar.total=total
                pbar.n=sum
                pbar.refresh()
        except Exception as e:
            print(str(e))
            pass
        finally:
            time.sleep(3)