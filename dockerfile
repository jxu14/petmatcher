#Author: Jeremy Xu

# Use a Python base image
FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive
# Install Apache web server
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get install -y apache2
RUN apt-get install python3-requests -y

# Enable CGI module
RUN a2enmod cgi

# Copy the HTML files and CGI script to the container
COPY index.html /var/www/html/
COPY petmatcher.html /var/www/html/
COPY petfinder.html /var/www/html/
COPY cgi-bin/matcher_script.py /usr/lib/cgi-bin/
COPY cgi-bin/finder_script.py /usr/lib/cgi-bin/

# Set the working directory
WORKDIR /var/www/html

# Expose port 80 for HTTP traffic
EXPOSE 80

# Start Apache web server
CMD ["apache2ctl", "-D", "FOREGROUND"]
