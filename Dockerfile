FROM mcr.microsoft.com/azure-functions/python:4-python3.9
ENV AzureWebJobsScriptRoot=/home/site/wwwroot \
AzureFunctionsJobHost__Logging__Console__IsEnabled=true
COPY requirements.txt /
RUN pip install -r /requirements.txt
RUN apt-get update && apt-get install -y libglib2.0-0 -y
COPY . /home/site/wwwroot