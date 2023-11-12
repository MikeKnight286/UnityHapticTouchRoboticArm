using System;
using System.Collections;
using RosMessageTypes.Geometry;
using RosMessageTypes.MyRobotArmService;
using RosMessageTypes.Trajectory;
using RosMessageTypes.Std;
using Unity.Robotics.ROSTCPConnector;
using Unity.Robotics.ROSTCPConnector.ROSGeometry;
using Unity.Robotics.UrdfImporter;
using UnityEngine;

public class TrajectoryPlanner : MonoBehaviour
{
	// Constants
	private static readonly string ServiceName = "/my_robot_arm_server";
	private static readonly Quaternion PickOrientation = Quaternion.Euler(90, 90, 0);

	// Variables
	public ArticulationBody[] jointArticulationBodies; // Joints
	public GameObject goal; // Goal
	private ROSConnection rc; // ROSConnection

	// Start
	void Start()
	{
		rc = ROSConnection.GetOrCreateInstance();
		rc.RegisterRosService<MoverServiceRequest, MoverServiceResponse>(ServiceName);

    }

	// ROS server request method
	public void Publish()
	{
        MoverServiceRequest request = new MoverServiceRequest();

		MyRobotArmMoveitJointsMsg joints = new MyRobotArmMoveitJointsMsg();
		for (int i = 0; i < jointArticulationBodies.Length; i++)
		{
			joints.joints[i] = jointArticulationBodies[i].jointPosition[0];
		}
		request.joints_input = joints;

		request.joints_input.goal_pose = new PoseMsg
		{
			position = goal.transform.position.To<FLU>(),
			orientation = Quaternion.Euler(Mathf.PI, 0, 0).To<FLU>()
		};

		rc.SendServiceMessage<MoverServiceResponse>(ServiceName, request, TrajectoryResponse);

	}
	////Coroutine to publish every second
	//IEnumerator PublishCoroutine()
	//{
	//	while (true)
	//	{
	//		// Publish the goal
	//		Publish();
	//
	//		yield return new WaitForSeconds(1f); // Wait for 1 second
	//	}
	//}

	// Callback for ROS service response
	void TrajectoryResponse(MoverServiceResponse response)
	{
		if (response.trajectory != null && response.trajectory.joint_trajectory.points.Length > 0)
		{
			print("Success!");
            // Start the coroutine to publish every second
            //StartCoroutine("PublishCoroutine"); //move here
            StartCoroutine(ExecuteTrajectories(response));
		}
		else
		{
			print("Failed!");
		}
	}

	// Execute motion planning
	IEnumerator ExecuteTrajectories(MoverServiceResponse response)
	{
		foreach (JointTrajectoryPointMsg t in response.trajectory.joint_trajectory.points)
		{
			float[] result = new float[4];
			for (int i = 0; i < t.positions.Length; i++)
			{
				result[i] = (float)t.positions[i] * Mathf.Rad2Deg;
			}
			for (int i = 0; i < jointArticulationBodies.Length; i++)
			{
				ArticulationDrive drive = jointArticulationBodies[i].xDrive;
				drive.target = result[i];
				jointArticulationBodies[i].xDrive = drive;
			}

			yield return new WaitForSeconds(0.1f);
		}

		yield return new WaitForSeconds(0.1f);
	}
}
