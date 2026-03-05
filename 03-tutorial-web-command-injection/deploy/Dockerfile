FROM php:7.4-apache

# Install ping
RUN apt-get update && apt-get install -y iputils-ping && rm -rf /var/lib/apt/lists/*

# Copy source code
COPY ./src/ /var/www/html/

# Copy flag to root
COPY ./flag /flag

# Set permissions
RUN chown root:root /flag && chmod 644 /flag
