# Use the official Playwright image from Microsoft's container registry
FROM mcr.microsoft.com/playwright:focal

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container
COPY . .

RUN apk update && \
    apk add openjdk11-jre curl tar && \
    curl -o allure-2.13.8.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.8/allure-commandline-2.13.8.tgz && \
    tar -zxvf allure-2.13.8.tgz -C /opt/ && \
    ln -s /opt/allure-2.13.8/bin/allure /usr/bin/allure && \
    rm allure-2.13.8.tgz

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run pytest when the container launches
CMD ["pytest"]