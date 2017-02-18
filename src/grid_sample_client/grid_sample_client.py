import rospy
import actionlib

from graspit_interface.msg import Grasp
from grid_sample_plugin.msg import GridSampleAction, GridSampleGoal

class GridSampleClient(object): 
    """
    Python interface for interacting with GraspIt
    """

    ROS_NODE_NAME = "GridSampleClient"
    GRASPIT_NODE_NAME = "/graspit/"

    @classmethod
    def getSamples(cls, resolution=2):
                   
        try:
            rospy.init_node(cls.ROS_NODE_NAME, anonymous=True)
        except ROSException:
            pass

        client = actionlib.SimpleActionClient(GridSampleClient.GRASPIT_NODE_NAME + 'gridSample', GridSampleAction)
        
        client.wait_for_server(timeout=rospy.Duration(1.0))
        goal = GridSampleGoal(resolution)

        client.send_goal_and_wait(goal)

        return client.get_result()

  
