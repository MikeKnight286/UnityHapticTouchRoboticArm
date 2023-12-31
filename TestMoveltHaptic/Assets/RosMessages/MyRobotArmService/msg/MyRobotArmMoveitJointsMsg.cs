//Do not edit! This file was generated by Unity-ROS MessageGeneration.
using System;
using System.Linq;
using System.Collections.Generic;
using System.Text;
using Unity.Robotics.ROSTCPConnector.MessageGeneration;

namespace RosMessageTypes.MyRobotArmService
{
    [Serializable]
    public class MyRobotArmMoveitJointsMsg : Message
    {
        public const string k_RosMessageName = "my_robot_arm_service/MyRobotArmMoveitJoints";
        public override string RosMessageName => k_RosMessageName;

        public double[] joints;
        public Geometry.PoseMsg goal_pose;

        public MyRobotArmMoveitJointsMsg()
        {
            this.joints = new double[4];
            this.goal_pose = new Geometry.PoseMsg();
        }

        public MyRobotArmMoveitJointsMsg(double[] joints, Geometry.PoseMsg goal_pose)
        {
            this.joints = joints;
            this.goal_pose = goal_pose;
        }

        public static MyRobotArmMoveitJointsMsg Deserialize(MessageDeserializer deserializer) => new MyRobotArmMoveitJointsMsg(deserializer);

        private MyRobotArmMoveitJointsMsg(MessageDeserializer deserializer)
        {
            deserializer.Read(out this.joints, sizeof(double), 4);
            this.goal_pose = Geometry.PoseMsg.Deserialize(deserializer);
        }

        public override void SerializeTo(MessageSerializer serializer)
        {
            serializer.Write(this.joints);
            serializer.Write(this.goal_pose);
        }

        public override string ToString()
        {
            return "MyRobotArmMoveitJointsMsg: " +
            "\njoints: " + System.String.Join(", ", joints.ToList()) +
            "\ngoal_pose: " + goal_pose.ToString();
        }

#if UNITY_EDITOR
        [UnityEditor.InitializeOnLoadMethod]
#else
        [UnityEngine.RuntimeInitializeOnLoadMethod]
#endif
        public static void Register()
        {
            MessageRegistry.Register(k_RosMessageName, Deserialize);
        }
    }
}
