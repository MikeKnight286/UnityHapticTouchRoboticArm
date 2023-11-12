#!/usr/bin/env python
# coding: UTF-8
import rospy
from my_service.srv import MyService, MyServiceResponse


# リクエスト受信時に呼ばれる
def on_request(req):
    # レスポンスの生成
    srv = MyServiceResponse()
    srv.sum = req.a + req.b
    return srv


# メイン
def main():
    # ノードの初期化
    rospy.init_node("my_server_node")

    # サービスの生成
    rospy.Service("my_service", MyService, on_request)

    # ノード終了まで待機
    rospy.spin()


if __name__ == "__main__":
    main()
