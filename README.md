# Robotic-Flower-
An interactive robotic flower that uses a custom CNN to recognize facial expressions and respond with servo movements, built with Raspberry Pi, TensorFlow, and XArm.
Supervisor: Saura Naderi - snaderi@ucsd.edu
Main Contributor: Wan-Rong (Emma) Leung - https://www.linkedin.com/in/wan-rong-leung-228650271/
Other Contributors:
Adrian Apsay - https://www.linkedin.com/in/adrianapsay/
Ethan Flores - https://www.linkedin.com/in/etflores1/

## How Does It Work?

**Note**: Before getting this project to work, please read the [requirements](#requirements) below.

The concept of the project is fairly simple - honestly straightfoward - have your Raspberry Pi camera set up with **good** lighting. If one person is in the frame, smile. The facial recognition program will create a green box around your face, signifying that you are smiling. The program will have a red box around your face if it doesn't detect you smiling. If you are smiling, but a red box is still present, be sure to position your face to the camera more clearly (you might have to adjust lighting or the camera angle). When the box is green, the flower will bloom. When the box is red, the flower will wilt. **The key takeaway is: KEEP SMILING!!!**

## Requirements<br>
(if you want your own robotic flower)
### Hardware
1. Raspberry Pi 3 Board or Above
2. Webcam (USB A)
3. HiWonder xArm 1S** (any other robotic arm might not translate well <br>
with the code due to constraints and limitations of different robotic arms)
4. Monitor (of any kind that display output)
5. Mouse and Keyboard (optional)
6. USB Micro B Cable (to connect xArm to Raspberry Pi)

### Other needed installation <br>
(Suggestion: use virtual enviroment)
1. Python <br>
``pip install python`` OR <br>
``pip install python3`` (dependent on your OS)
2.  OpenCV <br>
``pip install opencv-python``
3. xArm <br>
``pip install xarm``
4. Tensorflow <br>
``pip install tensorflow``
**Note**: Run these installs via the terminal, then import these packages on the text editor you are utilizing.


### Error You Might Run Into <br>
### Error 1: <br>
ModuleNotFoundError: No module named ‘hidapi’ <br>
Type this into the terminal:<br>
sudo nano /etc/udev/rules.d/99-usbarm.rules <br>

##### Type the following code into the page: <br>
``SUBSYSTEM=="usb", ATTR{idVendor}=="0483", ATTR{idProduct}=="5750", MODE="0666", GROUP="plugdev"``<br>

##### Control +S on keyboard to save and close the window <br>

Open the regular terminal again and type the following code: <br>
``sudo udevadm control --reload-rules`` <br>
``sudo udevadm trigger`` <br>

Next step is to install the api, so again type this in the terminal: <br>
``pip install hidapi`` <br>

Then after everything is installed we will reboot the raspberry pi, so in terminal type: <br>
``sudo reboot`` <br>





