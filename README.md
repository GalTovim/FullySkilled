![](https://raw.githubusercontent.com/GalTovim/FullySkilled/master/FullySkilled.png)
## Menu
For Running the Project, You need to have \ install:
1. Linux Operation System. (You can use VirtualBox)
2. Install libraries required to run the Project. (VirtualBox)
3. MongoDB Database.

## Linux Operation System Installation (VirtualBox)
                    
					
Follow those steps:
1. Download [VirtulBox](https://www.virtualbox.org/wiki/Downloads "VirtulBox"),
Under VirtulBox platform packages.
2. Download [Ubuntu](https://ubuntu.com/download/desktop "Ubuntu").
3. Run the VirtulBox with the ubuntu iso.
4. Press install when the Operation System is running and then next until it finishes.
                    
					
## Install libraries required to run the Project (VirtualBox)
                    
					
| Ubuntu | Description                    |
| ------------- | ------------------------------ |
|`sudo apt-get install cmake`|CMake is an extensible, open-source system that manages the build process in an operating system and in a compiler-independent manner.|
|`sudo apt-get update`|used to download package information from all configured sources.|
|`sudo apt-get install build-essential cmake`|As root, install all dependencies for 'packagename' so that I can build it|
|`sudo apt-get install libopenblas-dev liblapack-dev`|OpenBLAS is an open source implementation of the BLAS (Basic Linear Algebra Subprograms) API with many hand-crafted optimizations for specific processor types.|
|`sudo apt-get install libx11-dev libgtk-3-dev`|We are installing GTK and X11 for GUI functionality inside dlib, These libraries can be skipped if you do not care about the GUI functionality, saving you 100-200MB in space.|
|`sudo apt-get install python3 python3-dev python3-pip`|Install Python Version 3.X.X .|
|`pip3 install numpy`|NumPy is a package in Python used for Scientific Computing, NumPy package is used to perform different operations.|
|`pip3 install dlib`|a set of independent software components.|
|`sudo apt update`|Install Visual Studio Code for running the Project.|
|`sudo apt install software-properties-common apt-transport-https wget`|Like Above.|
|`wget -q https://packages.microsoft.com/keys/microsoft.asc -O- (לעשות שיפט עם בק-סלייש) sudo apt-key add -`|Like Above.|
|`sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"`|Like Above.|
|`sudo apt update`|Like Above.|
|`sudo apt install code`|Like Above.|
|`sudo apt install git`|Install Github.|
|`git clone https://github.com/GalTovim/FullySkilled.git`|Inside the Visual Studio code, write this command.|
|`pip3 install -r requirements.txt`|You need to enter the folder FullySkilled and then enter the folder backend, there you will run this command.|
|`sudo apt install npm`|You need to enter the folder FullySkilled and then enter the folder frontend, there you will run this command.|
|`install npm`|You need to enter the folder FullySkilled and then enter the folder frontend, there you will run this command.|
                    
					
## MongoDB Database
                    
					
Follow those steps:
1. Enter your MongoDB [User](https://cloud.mongodb.com/user#/atlas/login "User") , or [Register](https://cloud.mongodb.com/user#/atlas/register/accountProfile "Register").
2. Open new Cluster. (Database)
