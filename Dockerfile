# 293MB
FROM python:2.7-slim
# Update the ubuntu packages
RUN apt-get update
# Install git
RUN apt-get --yes install git-core
# Set the working directory to /app
WORKDIR /app
# Clone the latest software and change directory
RUN git clone https://github.com/cberger1/2048_ai_bot.git
RUN cd 2048_ai_bot
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt
# Run the python game app when the container launches
CMD [ "python", "./2048Game.py" ]
