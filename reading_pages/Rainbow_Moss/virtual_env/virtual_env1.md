## Python Virtual Environment

As python is the most popular data science language, most data science projects are written in python nowadays. It is a better practice to create a virtual environment for each new python project. 

### The Pain of Python Open Sources

One of python's strengths is the popularity of open sources. They are free, easy to use, and most are implemented with efficient computing complexity, which is also why we often look for existing python packages before building by ourselves.

However, such flexibility and freedom brings in headaches too. Every new package might depend on some existing packages. Meanwhile, having so many open source developers, every package might get updated quickly. Then when you are installing a new python package, its dependencies might have conflicting versions with the packages you have already installed.

For example, Lady H. had Tensorflow 2.4 installed, but when she was installeing the latest Keras Tuner, it required Tensorflow 2.6. She could not simply upgrade to Tensorflow 2.6 because there are other packages depending on version 2.4 at the time.

It is painful to break the dependencies of packages whenever you need to install something new for a new project. Creating a separate virtual environment will solve the problem!

### How to Create Python Virtual Environments

This method helps create python virtual environments regardless of your operating systems (OS).

1. Download and install Anaconda for your OS: https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html
2. Download and install PyCharm for your OS: https://www.jetbrains.com/pycharm/download/
  * Choose the "Community" version if you want the free one
3. Open PyCharm, go to `Preferences` or `Settings` --> `Project` --> `Python Interpreter`, find the little downward triangle on the right, and click `Show All...`

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Rainbow_Moss_images/virtual_env/pycharm1.png" width="973" height="255" />
</p>

4. Click the `+` button

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Rainbow_Moss_images/virtual_env/pycharm2.png" width="556" height="137" />
</p>

5. Click `Conda Environment`, this will create a conda virtual environment for you. Therefore, here you need to choose the python version needed for the new environment, and update the "Location" to indicate where do you want to store this new virtual environment.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Rainbow_Moss_images/virtual_env/pycharm3.png" width="822" height="232" />
</p>

6. Go to `Preferences` or `Settings` --> `Tools` --> `Terminal`, fill in `Shell path` with `powershell.exe -ExecutionPolicy ByPass -NoExit -Command "& '[Your Anaconda Location]\anaconda3\shell\condabin\conda-hook.ps1'`, remember to change the anaconda path here. This settings will make sure your PyCharm terminal shares the same virtual environment as your project.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Rainbow_Moss_images/virtual_env/pycharm5.0.png" width="975" height="393" />
</p>

7. Restart PyCharm, in PyCharm's terminal as well as the bottom right corner, you will see the virtial environment name. If you check the python version, it should show the right version chosen for the virtual environment:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Rainbow_Moss_images/virtual_env/pycharm4.0.png" width="936" height="161" />
</p>

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Rainbow_Moss_images/notes/other_venv_install.png" width="866" height="99" />
</p>

To list all the virtual environments you have created, type `conda env list` through PyCharm terminal.

### How to use Created Virtual Environments on Jupyter

You might also want to use the created virtual environment in your Jupyter Lab or Jupyter Notebook. Here's how:

1. In the PyCharm terminal, under your virtual environment, type `pip install ipykernel`. This step is only needed once for each virtual environment.
2. Type `python -m ipykernel install --user --name [your virtual env name] --display-name "[your virtual env name]"` to add the virtual environment's kernel into Jupyter, (update `[your virtual env name]` with the kernel name you want) like this:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Rainbow_Moss_images/virtual_env/pycharm_jupyter2.png" width="1087" height="26" />
</p>

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Rainbow_Moss_images/notes/jupyter_kernels.png" width="866" height="99" />
</p>

3. If you type `jupyter kernelspec list`, it will show all the available kernels for Jupyter:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Rainbow_Moss_images/virtual_env/pycharm_jupyter.png" width="696" height="112" />
</p>

To remove a certain kernel, you can type `jupyter kernelspec uninstall [kernel_name]` (update `[kernel_name]` with the kernel name you want to remove).

4. Now go to your Jupyer Lab or Jupyter Notebook, and you can choose the kernel to launch a new notebook:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Rainbow_Moss_images/virtual_env/pycharm_jupyter3.png" width="962" height="468" />
</p>

If you want to change the kernel of an existing noteook, click the top right kernel name of the notebook, and update the kernel option:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Rainbow_Moss_images/virtual_env/pycharm_jupyter4.png" width="300" height="312" />
</p>

#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Back to Rainbow Moss Home >>][1]

 
[1]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Rainbow_Moss/rainbow_moss.md#data-science-environments




