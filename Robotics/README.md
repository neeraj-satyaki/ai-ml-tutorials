# Robotics

Embodied AI stack. Bridges `DL/ComputerVision/`, `RL/`, `ElectronicsCommunication_Embedded/`, `ComputerArchitecture/`.

## Fundamentals
Forward + inverse kinematics. Dynamics. Jacobians. URDF modeling. Coordinate frames (ROS TF2). Quaternions + rotation representations.

## Perception
- **LiDAR** processing (PCL, Open3D).
- **Stereo depth**, **visual odometry**.
- **SLAM**: ORB-SLAM3, LIO-SAM, RTAB-Map, Cartographer.
- **Semantic / 3D-Gaussian-Splatting SLAM** (2024).
- **Sensor fusion**: EKF, UKF, pose-graph SLAM (g2o, Ceres, GTSAM).
- **Place recognition**, calibration (intrinsic, extrinsic, hand-eye).

## Motion + Control
PID, LQR, MPC. IK solvers (IKFast, TracIK, BioIK). Trajectory optimization (CHOMP, STOMP, TrajOpt, KOMO). Whole-body control. Footstep planning. Impedance / force control.

## Planning
A*, Dijkstra, Hybrid A*. Sampling-based (RRT, RRT*, PRM, BIT*). Behavior trees (BehaviorTree.CPP, py_trees). HTN planning. **TAMP** (Task And Motion Planning).

## Manipulation
Grasp planning (GraspIt!, Dex-Net, Contact-GraspNet). Antipodal grasps. 6-DoF pose estimation (FoundationPose 2024). Affordance learning. In-hand manipulation, deformable manipulation.

## Mobile robotics
Differential drive, Ackermann, holonomic. Velocity obstacles, DWA, TEB. Nav2 (ROS 2 Navigation Stack). Multi-robot coordination (Open RMF).

## Learning-based
- **Imitation**: BC, DAgger, Diffusion Policy (2023), ACT.
- **RL**: SAC, PPO for control.
- **Sim2Real**: domain randomization, system identification, teacher-student.
- **VLA** (Vision-Language-Action): RT-1/2, OpenVLA, Octo, π0 (Physical Intelligence), RDT-1B, Gemini Robotics 2 (2025).
- **World Models**: Dreamer v3, Genie 2.

## Simulation
Gazebo Classic + Fortress, NVIDIA **Isaac Sim / Isaac Lab**, MuJoCo (now free, DeepMind), PyBullet, Drake (MIT/Toyota), Webots, Unity ML-Agents, CoppeliaSim.

## Stacks + Frameworks
- **ROS 2** (Humble / Iron / Jazzy). MoveIt 2, Nav2, micro-ROS, Cartographer.
- DDS / RTPS transport.
- Autonomous driving stacks: Apollo, Autoware, Openpilot (comma.ai).
- Legacy ROS 1 — still alive in industry.

## Safety + Standards
ISO 10218 (collaborative robots), ISO 13849 (machinery safety), ISO 26262 (automotive ASIL), SOTIF ISO 21448, fail-safe + redundancy, E-stop + watchdog.

## Books + refs
- *Modern Robotics* — Lynch & Park (free).
- *Probabilistic Robotics* — Thrun, Burgard, Fox.
- *Springer Handbook of Robotics*.
- *Real-Time Optimization by Extremum-Seeking Control* — Ariyur & Krstic.
- Russ Tedrake's *Underactuated Robotics* + *Robot Manipulation* course (MIT, free).
