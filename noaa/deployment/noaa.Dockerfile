# Run the docker build command at the farmbeats directory

FROM ubuntu:16.04

# Install python
RUN apt-get install -y python3.5
# Get pip
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y python3-pip
RUN python3.5 -m pip install pip --upgrade
# Install dependency packages
RUN pip3 install absl-py==0.7.1
RUN pip3 install azureml-opendatasets==1.0.81
RUN pip3 install azure-eventhub==5.0.0
RUN pip3 install azure-storage==0.36.0

# Make some symlinksgit 
RUN cd $(dirname $(which python)) \
    && ln -fs python3 python \
    && ln -fs python3-config python-config


# Copy the code
RUN mkdir -p /usr/local/farmbeats/noaa
COPY noaa /usr/local/farmbeats/noaa
RUN mkdir -p /usr/local/farmbeats/datahub_lib
COPY datahub_lib /usr/local/farmbeats/datahub_lib

# Add farmbeats to pythonpath
ENV PYTHONPATH "${PYTHONPATH}:/usr/local/farmbeats"

# Set the working directory
WORKDIR /usr/local/farmbeats

# Default command, will be overwritten if something else is provided.
ENV end_point "set_in_docker_run"
ENV function_url "set_in_docker_run"
CMD [ "/bin/bash", "-c", "python3 /usr/local/farmbeats/noaa/bootstrap/run.py ${end_point} ${function_url}" ]
