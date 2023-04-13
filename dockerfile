# Use a Python base image
FROM python:3.8-slim

# Copy the HTML files and CGI script to the container
COPY index.html /app/
COPY petmatcher.html /app/
COPY petfinder.html /app/
COPY cgi-bin/matcher_script.py /app/cgi-bin/
COPY cgi-bin/finder_script.py /app/cgi-bin/

# Install any dependencies
# Example: Uncomment the following lines if you need to install any Python dependencies
RUN apt-get update 

# Set the working directory
WORKDIR /app

# Expose port 80 for HTTP traffic
EXPOSE 80

# Start a web server to serve the HTML files
CMD ["python3", "-m", "http.server", "80"]
