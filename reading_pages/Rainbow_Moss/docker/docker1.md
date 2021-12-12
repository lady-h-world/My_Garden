## Docker Environment

Docker environment is a virtual environment too, while python virtual environment is often used locally, a docker environment makes your project portable to be used in other platforms. Therefore, it's becoming a trend now to use docker for production deployment.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Rainbow_Moss_images/notes/production_deployment.png" width="766" height="79" />
</p>


## An Example Project

This is a simple example to show the basic strusture of a python project that can be deployed to docker environment.

The core logic is stored in folder "core". In this example, it's just loading the data stored in folder "src", and print out the shape of the data.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Rainbow_Moss_images/docker/core.png" width="667" height="337" />
</p>

The key element is the dockerfile! The dockerfile contains all the instructions to build the docker image.

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Rainbow_Moss_images/notes/docker_image.png" width="766" height="79" />
</p>

In this dockerfile:

1. You need to specify the python version needed for your project, in this case, python3.9 was used.
2. `WORKDIR` indicates the project folder in the docker container, "/usr/src/" is often the root path, and "moss_example" will be the folder of this project in docker.
3. Then all the code in folder "core" will be copied to docker under path "/usr/src/moss_example/src"

<p align="left">
<img src="https://github.com/lady-h-world/My_Garden/blob/main/images/Rainbow_Moss_images/docker/dockerfile.png" width="576" height="536" />
</p>



[1]:https://github.com/lady-h-world/My_Garden/tree/main/code/rainbow_moss/docker_example/moss_example
