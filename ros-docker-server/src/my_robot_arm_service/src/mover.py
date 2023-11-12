#!/usr/bin/env python
# coding: UTF-8

import sys

import geometry_msgs.msg
import moveit_commander
import rospy
from moveit_msgs.msg import RobotState
from my_robot_arm_service.srv import MoverService, MoverServiceResponse
from sensor_msgs.msg import JointState


# サーバーのリクエスト受信時に呼ばれる
def receive_request(req):
    # MoveGroupの生成
    move_group = moveit_commander.MoveGroupCommander("my_robot_arm")

    # モーションプランの計画
    plan = plan_trajectory(
        move_group, req.joints_input.goal_pose, req.joints_input.joints
    )

    # 後処理
    move_group.stop()
    move_group.clear_pose_targets()

    # レスポンスを返す
    response = MoverServiceResponse()
    if plan.joint_trajectory.points:
        print("success")
        response.trajectory = plan
    else:
        print("fail")
    return response

# モーションプランの計画
def plan_trajectory(move_group, pose_target, start_joints):
    # スタート状態の指定
    joint_state = JointState()
    joint_state.name = ["hip", "shoulder", "elbow", "wrist"]
    joint_state.position = start_joints
    robot_state = RobotState()
    robot_state.joint_state = joint_state
    move_group.set_start_state(robot_state)

    # ゴール状態の指定
    pose_goal = geometry_msgs.msg.Pose()
    pose_goal.position = pose_target.position
    pose_goal.orientation = pose_target.orientation
    move_group.set_joint_value_target(pose_goal, True)

    # モーションプランの計画
    return move_group.plan()[1]


# メイン
def main():
    # MoveItの初期化
    moveit_commander.roscpp_initialize(sys.argv)

    # ノードの生成
    rospy.init_node("mover")

    # サーバーの生成
    rospy.Service("my_robot_arm_server", MoverService, receive_request)
    print("Ready to plan")

    # ノード終了まで待機
    rospy.spin()


if __name__ == "__main__":
    main()
