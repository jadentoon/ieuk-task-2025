FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and installs them
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy script and log file
COPY analyse-log.py ./
COPY sample-log.log ./

# Run the script
CMD ["python", "analyse-log.py"]
