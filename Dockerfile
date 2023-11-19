# Use the official Playwright image from Microsoft's container registry
FROM mcr.microsoft.com/playwright:focal

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Allure
RUN apt-get update && apt-get install -y allure

# Make port 80 available to the world outside this container
EXPOSE 80

# Run pytest when the container launches
CMD ["pytest" , "--alluredir=allure_results"]