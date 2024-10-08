# COVID-19 Data Visualization

This project uses Gitlab CI/CD to automate the deployment of a dockerized application that downloads and displays COVID-19 data from the CSSEGISandData repository.

## Architecture

The application consists of a Python script that downloads the data, a Docker container that runs the script, and an Ansible playbook that deploys the container to an EC2 instance.

## Deployment

The deployment process involves the following steps:

1. Build the Docker image using the `Dockerfile`.
2. Run the Docker container using the `docker run` command.
3. Deploy the container to an EC2 instance using Ansible.
4. Upload the data to an S3 bucket using Terraform.

## Todo

* Make the application highly available by using a load balancer and multiple instances.
* Replace the simple Docker container with a container orchestrator like Kubernetes.
