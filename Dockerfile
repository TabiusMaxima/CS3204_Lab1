# Use an official Python runtime as a parent image
FROM python:3.8

ADD Factorial.py .

# Run hello.py when the container launches
CMD ["python", "Factorial.py"]