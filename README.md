# Robotic-Flower (HDSI Lab 3.0)

This project features an interactive robotic flower that blooms when you smile — blending computer vision, tensorflow, machine learning, and robotics into a real-time, expressive experience. Built using a Raspberry Pi, custom-trained CNN (Convolutional Neural Network) for facial expression recognition, and the HiWonder xArm 1S, the flower reacts to human emotion in a playful, artistic way. <br>

The project was developed at the UC San Diego HDSI Lab under the supervision of Saura Naderi and was designed to engage both technical and creative learners through a hands-on machine learning and hardware experience. <br>

**Note**: Before getting this project to work, please read the [requirements](#requirements) below. <br>

The concept of the project is fairly simple - honestly straightfoward - have your Raspberry Pi camera set up with **good** lighting. If one person is in the frame, smile. The facial recognition program will create a green box around your face, signifying that you are smiling. The program will have a red box around your face if it doesn't detect you smiling. If you are smiling, but a red box is still present, be sure to position your face to the camera more clearly (you might have to adjust lighting or the camera angle). When the box is green, the flower will bloom. When the box is red, the flower will wilt. **The key takeaway is: KEEP SMILING!!!** <br>

Supervisor: Saura Naderi - snaderi@ucsd.edu <br>
Main Contributor: Wan-Rong (Emma) Leung - https://www.linkedin.com/in/wan-rong-leung-228650271/ <br>
Other Contributors: <br>
Adrian Apsay - https://www.linkedin.com/in/adrianapsay/ <br>
Ethan Flores - https://www.linkedin.com/in/etflores1/ <br>

## 📚 Table of Contents

- [Project Overview](#robotic-flower-hdsi-lab-30)
- [📁 Code File Descriptions](#-code-file-descriptions)
- [🛠️ Requirements](#requirements)
  - [Hardware](#hardware)
  - [Other needed installation](#other-needed-installation)
- [🧪 Setting Up a Virtual Environment](#how-to-setup-a-virtual-enviroment)
- [🚀 How to Run the Code](#how-to-run-the-code)
- [💻 Allowing Code to Run on Startup](#allowing-code-to-run-on-startup)
- [📘 Curriculum](#curriculum)
- [🧯 Error You Might Run Into](#error-you-might-run-into)

### 📁 Code File Descriptions

| File Name                | Purpose                                                                 |
|-------------------------|--------------------------------------------------------------------------|
| `smile_training.py`      | Trains the custom CNN model for smile detection.                        |
| `test_train_model.py`    | Tests the trained model on example images.                              |
| `CameraTest.py`          | Verifies the camera is functioning correctly and displays real-time feed.|
| `smile_detection_robot.py` | Runs smile detection using the trained model and controls the xArm.    |
| `roboticflower.py`       | Contains high-level robotic flower behavior logic and servo positioning.|

## Requirements 
(if you want your own robotic flower) <br>
### Hardware 
1. Raspberry Pi 3 Board or Above
2. Webcam (USB A)
3. HiWonder xArm 1S** (any other robotic arm might not translate well <br>
with the code due to constraints and limitations of different robotic arms)
4. Monitor (of any kind that display output)
5. Mouse and Keyboard (optional)
6. USB Micro B Cable (to connect xArm to Raspberry Pi)

### Other needed installation 
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

## How to setup a virtual enviroment 
For this project due to the amount of packages, and imports, I personally strongly suggest doing this project in a virtural enviroment. <br>

### Setting Up a Virtual Environment on Raspberry Pi
(do this within the terminal)
1.    **Make sure your Raspberry Pi's package list is up-to-date:**
   ```bash
   sudo apt update
   sudo apt upgrade
   ```
2. **Install Python3 and venv** <br>
This will allow you to create your virtual enviroments.
```bash
sudo apt install python3 python3-venv
```
3.** Create and Navigating to Your Virtual Environment **<br>
Navigate to the directory that you want your project to me located in.
```bash
cd/path/to/project
python3 -m venv myenv
```
4. **Activate the Virtual Environment** <br>
Run the command:
```bash
source myenv/bin/activate
```
If you're already in your virtual environment directory file, you can just do:
```bash
source bin/activate
```
5. **Install Dependencies/Libraries** <br>
We've specified the required libraries [here](#setting-up-a-virtual-environment-on-raspberry-pi).
Install these within your virtual environment.
6. **Retrieve Source Code** <br>
Run the ``git clone`` command in terminal using this repository.
7. **Running the Code in Virtual Environment** <br>
Run the command ``python code.py`` (or whatever your .py file is named). <br>
**Note**: If you want to terminate your current run, you would have to close the terminal, then <br>
reopen and navigate to where your virtual environment is located. Then, run ``source bin/activate``. <br>

## How to run the code 

### ▶️ Step 1: Activate Virtual Environment

```bash
cd /path/to/your/project
source myenv/bin/activate
```

### ▶️ Step 2: Check Webcam (Optional)

```bash
python CameraTest.py
```
### ▶️ Step 3: Train the CNN Model

Make sure your dataset is prepared in two folders: `smile/` and `no_smile/`. <br>
When you run the code it will allow you to collect smiling and not smiling images through the webcam. <br>
Take atleast 100 photos for both smiling and not smiling photo <br>
##### Press s on the key board to capture a smiling photo <br>
##### Press n on the key board to capture a not smiling photo <br>
##### Press q when you finish taking photos, and it will start to train the model base on the pictures you just took

```bash
python smile_training.py
```
### ▶️ Step 4: Test the trained model (Optional) <br>
This step basically make sures that the model works as expected, before connecting it with the robotic flower. <br>
```bash
python test_train_model.py
```

### ▶️ Step 5: Run Smile Detection + Robotic Flower

Make sure: <br>
- Your xArm is connected via USB <br>
- Webcam has good lighting <br>
- You’re using the trained `smile_model` <br>

```bash
python smile_detection_robot.py
```

## Allowing Code to Run on Startup
Follow the steps in the powerpoint that can be found in the Automation Start Folder or click on this [link](https://docs.google.com/presentation/d/1AHJaK_VuXFnXBWXExjItuANiGQy02uty/edit?usp=sharing&ouid=114420282104442477740&rtpof=true&sd=true)

## Curriculum
[Assignment 1](https://docs.google.com/document/d/1uK2VAxS7jq1rQKJ1i32wXdaLqmttH0De3USxbChkj1w/edit?usp=sharing) : Learning to Control the Robotic Arm with Code <br>
[Assignment 2](https://docs.google.com/document/d/1iXz1Xtuj-O6ZBZWiGHLSpi1g6teHSNgaZH2Mlnd2ljo/edit?usp=sharing) : Controlling the Arm Using Code with Keyboard <br>
[Assignment 3](https://docs.google.com/document/d/1z-oLnOBRUbK3p9RE6ftoe_df_jse7aKJ989VX-nc7QY/edit?usp=sharing) : How to create your own Facial Recognition Model <br>
## Error You Might Run Into 
### Error : ModuleNotFoundError: No module named ‘hidapi’ <br>
Type this into the terminal:<br>
```bash
sudo nano /etc/udev/rules.d/99-usbarm.rules
``` 

##### Type the following code into the page: <br>
```bash
SUBSYSTEM=="usb", ATTR{idVendor}=="0483", ATTR{idProduct}=="5750", MODE="0666", GROUP="plugdev"
```

##### Control +S on keyboard to save and close the window <br>

Open the regular terminal again and type the following code: <br>
```bash
sudo udevadm control --reload-rules
```
```bash
sudo udevadm trigger
```

Next step is to install the api, so again type this in the terminal: <br>
```bash
pip install hidapi
``` 

Then after everything is installed we will reboot the raspberry pi, so in terminal type: <br>
```bash
sudo reboot
```

#### Other solutions to try
Verify Device Connection: <br>
Ensure that the device (arm/controller) is properly connected to the Raspberry Pi via USB. <br>
Use the command: <br>
``lsusb`` <br>






