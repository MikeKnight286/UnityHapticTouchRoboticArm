#!/usr/bin/env python
# coding: UTF-8
import sys

import moveit_commander
import rospy


# メイン
def main():
    # moveit_commanderの初期化
    moveit_commander.roscpp_initialize(sys.argv)

    # ノードの初期化
    rospy.init_node("robot_info")

    # RobotCommanderの準備
    robot = moveit_commander.RobotCommander()

    # ロボット情報の取得
    print("==Robot Info==")
    print("[group_names]", robot.get_group_names())
    print("[current_state]", robot.get_current_state())
    print("")

    # MoveGroupCommanderの準備
    move_group = moveit_commander.MoveGroupCommander("my_robot_arm")

    # グループ情報
    print("==Group Info==")
    print("[name]", move_group.get_name())
    print("[planning_frame]", move_group.get_planning_frame())
    print("[interface_description]", move_group.get_interface_description())
    print("")

    # ジョイント情報
    print("==Joint Info==")
    print("[active_joints] ", move_group.get_active_joints())
    print("[joints]", move_group.get_joints())
    print("[current_joint_values]", move_group.get_current_joint_values())
    print("")

    # エンドエフェクタ情報
    print("==EndEffector Info==")
    print("[has_end_effector_link]", move_group.has_end_effector_link())
    print("[end_effector_link]", move_group.get_end_effector_link())
    print("[current_pose]", move_group.get_current_pose())
    print("[current_rpy]", move_group.get_current_rpy())
    print("")


if __name__ == "__main__":
    main()
