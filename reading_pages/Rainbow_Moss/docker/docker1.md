## Docker Environment

A Docker environment is also a virtual environment, but unlike Python virtual environments, which are typically used locally, Docker makes your project portable across different platforms. As a result, Docker has become increasingly popular for production deployment.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Rainbow_Moss_images/notes/production_deployment.png" width="766" height="79" />
</p>


### An Example Project

This is a simple example to show the basic strusture of a python project that can be deployed to docker environment.

The core logic is stored in folder "core". In this example, it's just loading the data stored in folder "core", and print out the shape of the data.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Rainbow_Moss_images/docker/core_logic.png" width="628" height="317" />
</p>

The key element is the dockerfile! The dockerfile contains all the instructions to build the docker image.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Rainbow_Moss_images/notes/docker_image.png" width="766" height="79" />
</p>

In the dockerfile below:

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Rainbow_Moss_images/docker/docker-file.png" width="474" height="427" />
</p>

1. You need to specify the python version needed for your project, in this case, python3.9 was used.
2. `WORKDIR` indicates the project folder in the docker container, "/usr/src/" is often the root path, and "moss_example" will be the folder of this project in docker.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Rainbow_Moss_images/notes/docker_container.png" width="766" height="79" />
</p>

3. All the code in folder "core" will be copied to docker, under path "/usr/src/moss_example/core/". Suggest to have the source and destination folders share the same name in this copy command, so that your code can run both locally and run in docker.

🌻 [Check Moss Example code repo >>][1]


### How to Setup Docker

1. Download and install docker desktop
* To install docker on Windows: https://hub.docker.com/editions/community/docker-ce-desktop-windows
* To install docker on Mac: https://hub.docker.com/editions/community/docker-ce-desktop-mac
2. Open a terminal, `cd` to your project folder where dockerfile locates
3. Build the docker image by running `docker build -t [image_name] .`, in this example, let's call our docker image as "moss_image"
4. To run the docker image, type `docker run -d -p 8000:8000 [image_name]`

The execution process looks as below, but you can't tell whether the core logic had been successfully executed.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Rainbow_Moss_images/docker/docker_commands.png" width="1000" height="400" />
</p>

To check Moss Example's output, you can open the Docker Desktop, click on the container that contains your image and check its log. If the execution failed, you can also find errors in this log.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Rainbow_Moss_images/docker/docker1.png" width="1000" height="300" />
</p>

As shown above, Moss Example had been executed successfully. From here, you can develop more complex application running in the docker environment!

What's more, let's see some other commonly used commands:
* The container names are randomly generated each time, you can type `docker ps -a` to list all the contianers.
* `docker stop [container_name]` can stop a running container.
* `docker system prune` can remove all the stopped containers and dangling images. Sometimes your docker environment will show weird errors, such as a certain dependency is not available even though everything is correct. Then this command can be useful to give your docker environment a fresh start by cleaning up those misleading items.

#
<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/follow_us.png" width="120" height="50" />
</p>

[Back to Rainbow Moss Home >>][2]

[1]:https://github.com/lady-h-world/My_Garden/tree/main/code/rainbow_moss/docker_example/moss_example
[2]:https://github.com/lady-h-world/My_Garden/blob/main/reading_pages/Rainbow_Moss/rainbow_moss.md#data-science-environments
