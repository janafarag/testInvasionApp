# testInvasionApp

Test application to showcase different instances of a webserver

# For the Docker section

Recommended: create a virtualenv to dowload dependencies

in Windows:

python -m venv .\venv

venv\Scripts\Activate.ps1

pip install -r requirements.txt

# Folder structure

## Images for containers
app-cats is a Fast-API app for the cats web page
app-dogs is a Fast-API app for the dogs web page

Both of these can be packaged into Docker container by changing th following line in the Dockerfile (of the root folder) to app-dogs or app-cats
`COPY ./app-dogs /code/app`


## EC2 instance server files
cats and dogs folder are  folders with only the picture and index.html. These are both pulled by the EC2 instances from this exact file structure for the 2 web server instances

## Kubernetes declarations
This folder contains yaml files used in each Kubernetes chapter of the workshop. These are all sample definitions of the most common Kubernetes objects introduced in the KuberNETes workshop.