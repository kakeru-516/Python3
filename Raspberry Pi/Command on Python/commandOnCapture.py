import subprocess
import time
# 処理前の時刻
t1 = time.time()

# 計測したい処理
subprocess.run(['raspistill', '-vf', '-hf', '-t', '2000', '-tl', '200', '-o', 'test%02d.jpg'])

# 処理後の時刻
t2 = time.time()

# 経過時間を表示
elapsed_time = t2-t1
print(f"経過時間：{elapsed_time}")


