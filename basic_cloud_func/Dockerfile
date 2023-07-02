FROM python:3.11-slim-bookworm

# copy the local requirements file to set up the testing environment with required python modules
COPY local/requirements.txt .
RUN pip install -r requirements.txt 
RUN rm requirements.txt

# copy the basic_func source requirements to install required python modules
COPY src/requirements.txt . 
RUN pip install -r requirements.txt
 
# set flask environment variables
ENV FLASK_ENV=development
ENV FLASK_APP=local.py
ENV API_KEY=changeme

# set up volumes that will be mounted by the caller
VOLUME ["/basic_func", "/basic_func/src"]

ENTRYPOINT python /basic_func/local.py