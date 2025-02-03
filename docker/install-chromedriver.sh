#!/bin/bash

CHROME_VERSION="132.0.6834.159"

set -xe

# install chrome

# FROM python:3
#apt-get install -y libxss1 libappindicator1 libgconf-2-4 \
#  fonts-liberation libasound2 libnspr4 libnss3 libx11-xcb1 libxtst6 lsb-release xdg-utils \
#  libgbm1 libnss3 libatk-bridge2.0-0 libgtk-3-0 libx11-xcb1 libxcb-dri3-0

# FROM ubuntu:latest
apt-get install -y libxss1   \
  fonts-liberation libnspr4 libnss3 libx11-xcb1 libxtst6 lsb-release xdg-utils \
  libgbm1 libnss3 libatk-bridge2.0-0 libgtk-3-0 libx11-xcb1 libxcb-dri3-0

cd /opt && \
wget -O chrome.zip https://storage.googleapis.com/chrome-for-testing-public/${CHROME_VERSION}/linux64/chrome-linux64.zip && \
unzip chrome.zip && \
rm -v chrome.zip && \
ln -s "$(pwd)"/*/chrome /usr/local/sbin/chrome && \
chrome --version

# install chromedriver
# https://googlechromelabs.github.io/chrome-for-testing/#stable
cd /opt && \
wget -q -O chromedriver.zip https://storage.googleapis.com/chrome-for-testing-public/${CHROME_VERSION}/linux64/chromedriver-linux64.zip && \
unzip chromedriver.zip && \
ln -sf "$(pwd)"/*/chromedriver /usr/local/sbin/chromedriver && \
chromedriver -v
