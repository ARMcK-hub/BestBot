
# Pinned to version supported in Databricks 7.0 runtime https://docs.microsoft.com/en-us/azure/databricks/release-notes/runtime/7.0
FROM python:3.7.5-stretch

# Set Workspace directory
ARG WORKSPACE=/workspaces/BestBot
ENV WORKSPACE=${WORKSPACE}

# Avoid warnings by switching to noninteractive
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get -y install --no-install-recommends apt-utils dialog 2>&1 \
    
    # Install poetry
    && pip --disable-pip-version-check --no-cache-dir install poetry \
    # Clean up
    && apt-get autoremove -y \
    && apt-get clean -y 

COPY poetry.lock pyproject.toml ${WORKSPACE}/
RUN cd $WORKSPACE && poetry install --no-root

WORKDIR ${WORKSPACE}

# Switch back to dialog for any ad-hoc use of apt-get
ENV DEBIAN_FRONTEND=dialog

# Adding workspace to the PYTHONPATH
ENV PYTHONPATH ${WORKSPACE}
