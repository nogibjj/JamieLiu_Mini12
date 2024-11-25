# Use a lightweight Python base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents to the container
COPY . .

# Install dependencies using requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 (the port your Flask app runs on)
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
