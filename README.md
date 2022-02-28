<!-- header -->
<div align="center">
    <p>
    <!-- Header -->
        <img width="100px" src="./static/images/readme_logo.png"  alt="bestbot" />
        <h2>BestBot</h2>
        <p><i>Get a GPU!</i></p>
    </p>
    <p>
    <!-- Shields -->
        <a href="https://github.com/armck-hub/bestbot/LICENSE">
            <img alt="License" src="https://img.shields.io/github/license/armck-hub/bestbot.svg" />
        </a>
        <a href="https://github.com/armck-hub/bestbot/actions">
            <img alt="Tests Passing" src="https://github.com/armck-hub/bestbot/workflows/CI/badge.svg" />
        </a>
        <a href="https://codecov.io/gh/armck-hub/bestbot">
            <img alt="Code Coverage" src="https://codecov.io/gh/armck-hub/bestbot/branch/master/graph/badge.svg" />
        </a>
        <a href="https://github.com/armck-hub/bestbot/issues">
            <img alt="Issues" src="https://img.shields.io/github/issues/armck-hub/bestbot" />
        </a>
        <a href="https://github.com/armck-hub/bestbot/pulls">
            <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/armck-hub/bestbot" />
        </a>
        <a href="https://stackshare.io/armck-hub/bestbot">
            <img alt="StackShare.io" src="http://img.shields.io/badge/tech-stack-0690fa.svg?label=StackShare.io">
        </a>
    </p>
    <p>
    <!-- Links -->
        <a href="#demo">View Demo</a>
        ·
        <a href="https://github.com/armck-hub/bestbot/issues/new/choose">Report Bug</a>
        ·
        <a href="https://github.com/armck-hub/bestbot/issues/new/choose">Request Feature</a>
    </p>
</div>
<br>
<br>

<!-- Description -->
# BestBot
A hastily written Webscan Bot that notifies when a product is in stock on a webstore.



### Quick Start

0. ###### Setup & Configure the project:
A sample configuration is provided at `/config/config.example.json`. This file should be updated to desired configuration and renamed to `/config/config.json`.

1. ###### Start a Docker Container:
Start an associated container built from the `./.devcontainer/Dockerfile` in this project.
The container can be started after being built via the `docker start <container_name>` command.

2. ###### Start the Script:
Start the application by executing the script with python inside of the container, as such: `docker exec -it <container_name> poetry run python bestbot.py`. Note that poetry is the virtual environment that the script runs in.

### Usage

##### Logs:
Logs can be viewed in runtime via executing the `rlog.py` script, which follows the stdout output from the bestbot script. `docker exec -it <container_name> poetry run python rlog.py`.

Alternatively logs can be printed via executing the `plog.py` script, which simply prints their contents. `docker exec -it <container_name> poetry run python plog.py`.

##### Configuration:
Changing the product watch configuration can be completed by modifying the config file (`/config/config.json`).