### 신기하다

```
root@DESKTOP-CLSFCGH:~/ir# ls
LICENSE  README.md  build  install  log  readme.md  src
root@DESKTOP-CLSFCGH:~/ir# cd src/01_basics
root@DESKTOP-CLSFCGH:~/ir/src/01_basics# ls
README.md  basics  launch  package.xml  resource  setup.cfg  setup.py
root@DESKTOP-CLSFCGH:~/ir/src/01_basics# cd basic
bash: cd: basic: No such file or directory
root@DESKTOP-CLSFCGH:~/ir/src/01_basics# cd basics
root@DESKTOP-CLSFCGH:~/ir/src/01_basics/basics# cd ir
bash: cd: ir: No such file or directory
root@DESKTOP-CLSFCGH:~/ir/src/01_basics/basics# cd ../../..
root@DESKTOP-CLSFCGH:~/ir# ls
LICENSE  README.md  build  install  log  readme.md  src
root@DESKTOP-CLSFCGH:~/ir# colcon build
Starting >>> basics  
Starting >>> my_first_pkg
Finished <<< basics [1.87s]                                            
Finished <<< my_first_pkg [2.29s]          

Summary: 2 packages finished [2.93s]
root@DESKTOP-CLSFCGH:~/ir# source install/setup.bash
root@DESKTOP-CLSFCGH:~/ir# ros2 run basics
usage: ros2 run [-h] [--prefix PREFIX] package_name executable_name ...
ros2 run: error: the following arguments are required: executable_name, argv
root@DESKTOP-CLSFCGH:~/ir# ros2 run basics 
--prefix  listener  talker    
root@DESKTOP-CLSFCGH:~/ir# ros2 run basics 
--prefix  listener  talker    
root@DESKTOP-CLSFCGH:~/ir# ros2 run basics 
--prefix  listener  talker    
root@DESKTOP-CLSFCGH:~/ir# ros2 run basics 
--prefix  listener  talker    
root@DESKTOP-CLSFCGH:~/ir# ros2 run basics talker
[INFO] [1775442916.237382961] [talker]: Publishing: "Hello World: 0"
[INFO] [1775442916.721491571] [talker]: Publishing: "Hello World: 1"
[INFO] [1775442917.221394356] [talker]: Publishing: "Hello World: 2"
[INFO] [1775442917.722498065] [talker]: Publishing: "Hello World: 3"
[INFO] [1775442918.221347266] [talker]: Publishing: "Hello World: 4"
[INFO] [1775442918.721337564] [talker]: Publishing: "Hello World: 5"
[INFO] [1775442919.222095053] [talker]: Publishing: "Hello World: 6"
[INFO] [1775442919.721175125] [talker]: Publishing: "Hello World: 7"
[INFO] [1775442920.221608593] [talker]: Publishing: "Hello World: 8"
[INFO] [1775442920.721585896] [talker]: Publishing: "Hello World: 9"

[INFO] [1775442921.221154404] [talker]: Publishing: "Hello World: 10"
^CTraceback (most recent call last):
  File "/root/ir/install/basics/lib/basics/talker", line 33, in <module>
    sys.exit(load_entry_point('basics==0.0.0', 'console_scripts', 'talker')())
  File "/root/ir/install/basics/lib/python3.10/site-packages/basics/talker.py", line 40, in main
    rclpy.spin(node)
  File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/__init__.py", line 229, in spin
    executor.spin_once()
  File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/executors.py", line 776, in spin_once
    self._spin_once_impl(timeout_sec)
  File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/executors.py", line 765, in _spin_once_impl
    handler, entity, node = self.wait_for_ready_callbacks(timeout_sec=timeout_sec)
  File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/executors.py", line 748, in wait_for_ready_callbacks
    return next(self._cb_iter)
  File "/opt/ros/humble/local/lib/python3.10/dist-packages/rclpy/executors.py", line 645, in _wait_for_ready_callbacks
    wait_set.wait(timeout_nsec)
KeyboardInterrupt
[ros2run]: Interrupt
root@DESKTOP-CLSFCGH:~/ir# 
root@DESKTOP-CLSFCGH:~/ir# 
```

### 환경변수
gedit ~/.bashrc
source ~/bashrc
- 학번 뒷 세자리로 .. Bashrc에 설정하였음
- RQT 그래프로 구성확인할 수 있음

### 빌드 ~!! 
colcon build --symlink-install
즉 src/ 안에서 파일 수정하면 rebuild 없이 바로 반영됨.