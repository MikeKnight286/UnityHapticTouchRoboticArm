#!/usr/bin/env python
# coding: UTF-8
import sys

import geometry_msgs.msg
import moveit_commander
import rospy
import tf
from geometry_msgs.msg import Quaternion, Vector3


def main():
    # moveit_commanderの初期化
    moveit_commander.roscpp_initialize(sys.argv)

    # ノードの生成
    rospy.init_node("pose_planner")

    # MoveGroupCommanderの準備
    move_group = moveit_commander.MoveGroupCommander("my_robot_arm")

    # エンドポイントの姿勢でゴール状態を指定
    pose_goal = geometry_msgs.msg.Pose()
    pose_goal.position = Vector3(0.7, 0.0, 0.7)
    q = tf.transformations.quaternion_from_euler(0, 0, 0)
    pose_goal.orientation = Quaternion(x=q[0], y=q[1], z=q[2], w=q[3])
    move_group.set_joint_value_target(pose_goal, True)

    # モーションプランの計画と実行
    move_group.go(wait=True)

    # 後処理
    move_group.stop()
    move_group.clear_pose_targets()


if __name__ == "__main__":
    main()
