# Use official Python 3 image as base
FROM python:3

# Set working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

RUN pip install .

CMD ["python", "-m", "yfinance_mcp_server"]
