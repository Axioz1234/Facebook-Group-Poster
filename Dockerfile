# Use the official Apify Python base image.
FROM apify/actor-python:3.9

# Install necessary system dependencies including Chromium and its driver
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    libnss3 \
    libgconf-2-4 \
    libxi6 \
    libxcursor1 \
    libxrandr2 \
    libxcomposite1 \
    libxdamage1 \
    libpangocairo-1.0-0 \
    libatk1.0-0 \
    libgtk-3-0 \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

# Set environment variables for Chromium
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_BIN=/usr/bin/chromium-driver

# Set working directory in the container
WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Define the command to run your actor
CMD ["python", "main.py"]
