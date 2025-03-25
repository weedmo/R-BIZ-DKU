# R-BIZ Challenge 2024 - Dilly Robot Delivery
![image](https://github.com/user-attachments/assets/25ba1de1-075f-4b59-8e73-aed1e1d05bd9)
This repository contains the source code for our participation in the **2024 International Robot Contest - R-BIZ Challenge**, specifically the **Dilly Robot Delivery Challenge** hosted by Woowa Brothers (Baemin).  
The goal of the competition was to autonomously deliver items in both indoor and outdoor environments using various sensors and simulation tools.

---

## 🤖 Robot Platform & Sensors

- **Robot**: Dilly (Autonomous delivery robot by Baemin)
- **Sensors**:
  - 3D LiDAR × 2
  - Camera × 1
  - IMU
  - GPS

---

## 🧰 Development Environment

- **OS**: Ubuntu 20.04
- **ROS**:
  - Initially attempted: ROS2 Foxy + NAV2 (via ros1_bridge)
  - Final implementation: ROS1 Noetic + `move_base`
- **Simulator**: MORAI SIM
- **Languages**: Python

---

## ⚙️ Key Features

- 3D LiDAR-based obstacle detection and mapping
- GPS-based outdoor localization
- Camera-based detection of pickup/drop zones
- Global & local path planning using `move_base`
- Simulation and debugging in MORAI SIM

---

## ⚠️ Code Status

> The current codebase was recovered from a backup after the competition.  
> As a result, the file structure may be inconsistent, and some files may be incomplete or missing.

- The project includes core files organized in the following folders:
  - `src/` – Main scripts and ROS nodes
  - `launch/` – Launch files for simulation and navigation
  - `rviz/` – RViz configuration files
  - `msg/` – Custom message definitions (if any)
  - `json/` – Mission and waypoint files for MORAI SIM

Code cleanup and documentation will be updated progressively.

---

## 🧪 Lessons Learned

This was a team project with 4 members: 3 graduate students and myself as the only undergraduate.  
Though I’ve often worked as a team lead, in this project I focused on learning and contributing as a strong follower.

We initially aimed to use ROS2 and the NAV2 stack for more advanced navigation, but due to integration issues with MORAI SIM and unexpected time sync errors, we reverted to ROS1 Noetic and `move_base` in the final week before the competition.

## 📸 Demo Video

[![Watch the video](https://img.youtube.com/vi/Tmpl5__fc7o/0.jpg)](https://www.youtube.com/live/Tmpl5__fc7o?si=nchNzFDPd7hwx6pJ&t=4205)

> 📍 Click the image to watch the robot demo at the delivery section (starts at 1:10:05).

