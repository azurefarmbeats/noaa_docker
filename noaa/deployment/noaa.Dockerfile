# Run the docker build command at the farmbeats directory

FROM ubuntu:16.04
LABEL maintainer="abmallic@microsoft.com"
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

# Make some symlinksgit 
RUN cd $(dirname $(which python)) \
    && ln -fs python3 python \
    && ln -fs python3-config python-config


# Copy the code
RUN mkdir -p /usr/local/farmbeats/noaa
COPY noaa /usr/local/farmbeats/noaa
RUN mkdir -p /usr/local/farmbeats/datahub_lib
COPY datahub_lib /usr/local/farmbeats/datahub_lib

# Set the working directory
WORKDIR /usr/local/farmbeats/partners

