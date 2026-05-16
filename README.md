# Four-Wheeled Mobile Robot

A ROS 2 and Gazebo-based four-wheeled mobile robot project.

---

## Features

* Differential drive mobile robot
* ROS 2 integration
* Gazebo simulation
* Motor control
* Sensor integration
* Custom robot description using URDF/Xacro

---

## Technologies Used

* ROS 2
* Gazebo
* Python
* URDF/Xacro
* Linux (Ubuntu)

---

## Project Structure

```bash
mobile_robot/
├── launch/
├── urdf/
├── worlds/
├── meshes/
├── scripts/
├── config/
├── package.xml
├── setup.py
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Nick542k/Four-wheeled-mobile-robot.git
```

Go to workspace:

```bash
cd ~/ws_mobile
```

Build the workspace:

```bash
colcon build
```

Source the workspace:

```bash
source install/setup.bash
```

---

## Running the Simulation

```bash
ros2 launch mobile_robot gazebo_model.launch.py
```

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
---

---

## Future Improvements

* Add autonomous navigation
* Add SLAM
* Add obstacle avoidance
* Integrate sensors and camera
* Improve robot control system

---

## Author

Nithish Kumar

GitHub: [https://github.com/Nick542k](https://github.com/Nick542k)
