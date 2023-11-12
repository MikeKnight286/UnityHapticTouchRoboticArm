#!/usr/bin/env python
# coding: UTF-8
import rospy
from my_service.srv import MyService


# メイン
def main():
    # ノードの初期化
    rospy.init_node("my_server_client")

    # サービスが利用可能になるまで待機
    rospy.wait_for_service("my_service")

    try:
        # サービスプロクシの生成
        proxy = rospy.ServiceProxy("my_service", MyService)

        # リクエストの送信
        result = proxy(1, 2)

        # ログ出力
        rospy.loginfo("Result : " + str(result.sum))
    except rospy.ServiceException as e:
        rospy.loginfo("ServiceException : %s" % e)

    # ノード終了まで待機
    rospy.spin()


if __name__ == "__main__":
    main()
