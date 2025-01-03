## Python Virtual Environment

Python is the most popular language for data science, most projects today are written in it. It's considered best practice to create a virtual environment for each new Python project.


### The Pain of Python Open Sources

One of Python's key strengths is the widespread availability of open-source libraries. These libraries are free, easy to use, and often designed with efficient computational complexity. This is why we typically search for existing Python packages before deciding to build our own.

However, this flexibility comes with challenges. Every new package may have dependencies on other existing packages, and with so many open-source contributors, updates can happen frequently. As a result, when you install a new Python package, its dependencies might conflict with the versions of packages you’ve already installed.

For example, Lady H. had TensorFlow 2.4 installed, but when she tried to install the latest Keras Tuner, it required TensorFlow 2.6. She couldn’t simply upgrade to TensorFlow 2.6 because other packages relied on version 2.4 at the time.

Managing these conflicts when starting new projects can be frustrating. The solution? Create a separate virtual environment for each project!


### How to Create Python Virtual Environments

This method helps create python virtual environments regardless of your operating systems (OS). First of all, make sure you have:

* Downloaded and installed Anaconda for your OS: https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html
* Downloaded and installed PyCharm for your OS: https://www.jetbrains.com/pycharm/download/
  * Choose the "Community" version if you want to use it for free 😉

Follow the steps below each time when you want to create a virtual environment: 

1. Open PyCharm, go to `Preferences` or `Settings` --> `Project` --> `Python Interpreter`, find the little downward 
   triangle on the right, and click `Show All...`

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Rainbow_Moss_images/virtual_env/pycharm1.png" width="973" height="255" />
</p>

2. Click the `+` button

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Rainbow_Moss_images/virtual_env/pycharm2.png" width="556" height="137" />
</p>

3. Click `Conda Environment`, this will create a conda virtual environment for you. Edit `Location` to indicate where to store this new virtual environment and choose the `Python version`, then click `OK`.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Rainbow_Moss_images/virtual_env/pycharm3.png" width="822" height="232" />
</p>

4. (ONLY NEED ONCE) Type `conda info` in a PyCharm terminal, to find the path of the <b>base environment</b> of 
   Anaconda. Then go to `Preferences` or `Settings` --> `Tools` --> `Terminal`, fill in `Shell path` with `powershell.exe -ExecutionPolicy ByPass -NoExit -Command "& '[Your Anaconda base environment path]\shell\condabin\conda-hook.ps1'`, remember to change the anaconda path here. This setting will make sure your PyCharm terminal shares the same virtual environment as your project. Later, if you will set up multiple conda 
   virtual environments, <b>only need to do this setup once</b> ☝️.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Rainbow_Moss_images/virtual_env/pycharm5.0.png" width="975" height="393" />
</p>

5. Click `+` to start a new terminal, and you will see the created virtual environment name in both terminal and bottom right corner. If you check the python version, it should show the right version chosen for the virtual environment:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Rainbow_Moss_images/virtual_env/pycharm4.1.png" width="941" height="163" />
</p>

In some cases, if you still can't see the virtual environment appeared, type `conda activate {conda_virtual_env_name}` to activate the virtual environment.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Rainbow_Moss_images/notes/other_venv_install.png" width="866" height="99" />
</p>

To list all the virtual environments you have created, type `conda env list` through PyCharm terminal.

The created virtual environment might have some python libraries installed by default. Sometimes you want to remove all these existing libraries, to do this run `pip list --format=freeze >> requirements.txt` to dump these library names in "requirements.txt" file, then run `pip uninstall -r requirements.txt -y` to remove them all.

<b>Note:</b> The benefit of using `pip list --format=freeze` is that it records each package's version. By contrast, simply using `pip freeze` may show some packages' file paths on your own machine, which cannot be reinstalled on another machine.


### How to Install Requirements

`requirements.txt` is a file that lists all the Python packages needed for your environment. Each package often includes a specific version to ensure you can recreate the same setup later, even if newer versions of the packages have been released. [See example requirements.txt here >>][2]

To install all the libraries in requirements file, we can run command `pip install -r requirements.txt`. Besides, often times, there might be other commands to run in order to set up the environment, and we can put all the commands in the same bash file. The bash file is often named as `setup.sh`. [See example setup.sh here >>][3]

To execute all the commands in `setup.sh` file:
* If you're using Mac OS or Linux system, you can run `sh setup.sh` in your terminal directly.
* If you're using Windows, PyCharm's termial allows you to choose `Git Bash` terminal, where you can run `sh setup.sh` too.
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Rainbow_Moss_images/virtual_env/pycharm_bash_terminal.png" width="444" height="146" />
</p>


### How to Produce Jupyter Kernel for Created Virtual Environment

You might also want to use the created virtual environment in your Jupyter Lab or Jupyter Notebook. Here's how:

1. Make sure you have jupyter lab or jupyter notebook, as well as ipywidgets installed. You can run `pip install jupyterlab`, `pip install ipywidgets --user`.
2. In the PyCharm terminal, under your virtual environment, type `pip install ipykernel`. This step is only needed once for each virtual environment.
3. Type `python -m ipykernel install --user --name [your virtual env name] --display-name "[your virtual env name]"` 
   to add the virtual environment's kernel into Jupyter, (update `[your virtual env name]` with the kernel name you want) like this:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Rainbow_Moss_images/virtual_env/pycharm_jupyter2.png" width="1087" height="26" />
</p>

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Rainbow_Moss_images/notes/jupyter_kernels.png" width="866" height="99" />
</p>

4. If you type `jupyter kernelspec list`, it will show all the available kernels for Jupyter:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Rainbow_Moss_images/virtual_env/pycharm_jupyter.png" width="696" height="112" />
</p>

5. Now go to your Jupyer Lab or Jupyter Notebook, and you can choose the kernel to launch a new notebook:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Rainbow_Moss_images/virtual_env/pycharm_jupyter3.png" width="962" height="468" />
</p>

If you want to change the kernel of an existing notebook, click the top right kernel name of the notebook, and update the kernel option:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Rainbow_Moss_images/virtual_env/pycharm_jupyter4.png" width="300" height="312" />
</p>


### How to Delete Python Virtual Environments
1. Open PyCharm, go to `Preferences` or `Settings` --> `Project` --> `Python Interpreter`, find the little downward triangle on the right, and click `Show All...`

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Rainbow_Moss_images/virtual_env/pycharm1.png" width="973" height="255" />
</p>

2. Select the virtual environment you want to remove and click `-` button. This will remove the interpreter shown in PyCharm.
3. Type `conda env list` to find paths of all the virtual environments, then type `rm -r {env_path}` (change 
   `env_path` for your use case). This will remove the virtual environment installed.
4. Type `jupyter kernelspec list` to find the paths of all the kernels for jupyter, then type `rm -r {kernel_path}` (change `kernel_path` for your use case). This will remove the kernel from jupyter.


#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Back to Rainbow Moss Home >>][1]

 
[1]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Rainbow_Moss/rainbow_moss.md#data-science-environments
[2]:https://github.com/lady-h-world/My_Garden/blob/main/code/secret_guest/requirements.txt
[3]:https://github.com/lady-h-world/My_Garden/blob/main/code/secret_guest/setup.sh




