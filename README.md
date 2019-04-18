### PCA9685

## About
The node is responsible ofr the receiving signals and precessing them in the PCA9685 board.
In the setup of the car, PCA9685 is responsible to receive values for the engine and steering controllers.

## How to start
In order to start the node, use the following commands
```
git clone git@github.com:project-omicron/pca9685.git
sudo pip3 install -r requirements.txt
roslaunch launch/pca9685.launch
```

## Limitations
Current node depends on the libary ```Adafruit_PCA9685``` that is available for Raspberry Pi, for example, but it will not run on x86 systems.
