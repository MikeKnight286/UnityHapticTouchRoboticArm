#!/usr/bin/env python
# coding: UTF-8
import rospy
from my_custom_topic.msg import MyMessage


# サブスクライブ受信時に呼ばれる
def on_subscribe(msg):
    # ログ出力
    rospy.loginfo("Subscribe : " + str(msg.x) + ", " + str(msg.y))


# メイン
def main():
    # ノードの生成
    rospy.init_node("my_subscriber_node")

    # サブスクライバーの生成
    rospy.Subscriber("my_custom_topic", MyMessage, on_subscribe)

    # ノード終了まで待機
    rospy.spin()


if __name__ == "__main__":
    main()
