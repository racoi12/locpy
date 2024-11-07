# Dockerfile

# Use the official lightweight Python image.
FROM python:3.9-slim

# Set the working directory.
WORKDIR /app

# Copy the requirements file.
COPY requirements.txt .

# Install dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code.
COPY app.py .

# Expose port 5000.
EXPOSE 5000

# Set the command to run the application.
CMD ["python", "app.py"]
