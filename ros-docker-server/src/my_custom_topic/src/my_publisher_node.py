#!/usr/bin/env python
# coding: UTF-8
import rospy
from my_custom_topic.msg import MyMessage


# メイン
def main():
    # ノードの生成
    rospy.init_node("my_publisher_node")

    # パブリッシャーの生成
    pub = rospy.Publisher("my_custom_topic", MyMessage, queue_size=10)

    r = rospy.Rate(1)  # 1Hz
    while not rospy.is_shutdown():
        # メッセージの生成
        msg = MyMessage()
        msg.x = 10
        msg.y = 20

        # メッセージのパブリッシュ
        pub.publish(msg)

        # ログ出力
        rospy.loginfo("Publish : " + str(msg.x) + ", " + str(msg.y))

        # スリープ
        r.sleep()


if __name__ == "__main__":
    main()
