# robot_description

URDF models and launch files for Intelligent Robotics.

## Contents

| File | Description |
|---|---|
| `urdf/two_r_robot.urdf` | 2R planar robot arm (upright, 2 revolute joints) |
| `urdf/mobile_robot.urdf` | Differential drive mobile robot with LiDAR |
| `launch/display_two_r_robot.launch.py` | Launch 2R robot in RViz |
| `launch/display_mobile_robot.launch.py` | Launch mobile robot in RViz |
| `rviz/two_r_robot.rviz` | RViz config for 2R robot |
| `rviz/mobile_robot.rviz` | RViz config for mobile robot |

## Dependencies

Install all dependencies automatically:

```bash
rosdep install --from-paths src --ignore-src -r -y
```

## Build

```bash
colcon build --packages-select robot_description --symlink-install
source install/setup.bash
```

## Run

### 2R Robot
```bash
ros2 launch robot_description display_two_r_robot.launch.py
```

### Mobile Robot
```bash
ros2 launch robot_description display_mobile_robot.launch.py
```

## Inspect

```bash
ros2 topic echo /joint_states
ros2 topic echo /tf
ros2 run tf2_tools view_frames
```