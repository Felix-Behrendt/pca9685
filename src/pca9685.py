import time

import Adafruit_PCA9685
import rospy

from std_msgs.msg import Int32


class PCA9685:
    """
    PWM motor controller using PCA9685 boards.
    This is used for most RC Cars
    """
    def __init__(self):
        # Initialise the PCA9685 using the default address (0x40).
        self.pwm = Adafruit_PCA9685.PCA9685()
        self.pwm.set_pwm_freq(60)

    def set_pwm(self, channel : int, pulse: int) -> None:
        """
        Sets a single PWM channel.
        """
        self.pwm.set_pwm(channel, 0, pulse)


class ROSPackage_PCA9685:
    def __init__(self):
        self.pca = PCA9685()

    def callback_00(self, data):
        self.pca.set_pwm(0, data.data)

    def callback_15(self, data):
        self.pca.set_pwm(15, data.data)

    @staticmethod
    def run():
        rospy.init_node('pca9685')
        rospy.Subscriber('channel_00', Int32, callback)
        rospy.Subscriber('channel_15', Int32, callback)
        rospy.spin()


if __name__ == '__main__':
    package = ROSPackage_PCA9685()
    package.run()
