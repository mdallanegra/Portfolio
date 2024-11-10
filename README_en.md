<p align="center">
    <img src="_src/logo/neuro-pathways-rm-bg.png" width="200" alt="Neuro Pathways Logo">
</p>


# My Portfolio Web Page<!-- omit in toc --> 

<p align="center">
    <strong><a href="README_es.md">Versión en Español</a></strong><br>
    <strong><a href="README_en.md">English Version</a></strong><br>
    <strong><a href="README.md">Versione Italiana prossimamente</a></strong><br>
    <strong><a href="README.md">Deutsche Version kommt bald</a></strong><br>
</p>

## Index <!-- omit in toc --> 

- [Overview](#overview)
  - [Features](#features)
    - [Tech Stack](#tech-stack)
    - [Tools and Environments](#tools-and-environments)
    - [Languages](#languages)
  - [Hosting](#hosting)
  - [Deployment](#deployment)
    - [`Dockerfile`](#dockerfile)
    - [`app.yaml`](#appyaml)
    - [`docker-compose-deploy.yml`](#docker-compose-deployyml)
    - [`docker-compose.yml`](#docker-composeyml)
  - [Usage](#usage)
  - [Installation](#installation)
    - [Project Structure](#project-structure)
    - [Clone, install and run the repository](#clone-install-and-run-the-repository)
- [Contributions](#contributions)
- [Contact](#contact)
- [Licenses](#licenses)

---

# Overview

Welcome to my web portfolio, showcasing my professional projects, skills, and background in data science, machine learning, and software engineering. This site is designed with Django and Bootstrap to provide a responsive, modern experience.

## Features

- **Project Showcase:** A carousel-style display of my projects, highlighting key details and technologies used.
- **Multi-language Support**: Available in English and Spanish for greater accessibility, and coming soon German and Italian.
- **Downloadable Resources**: Includes downloadable links for my CV in both English and Spanish.
- **Responsive Design**: Optimized for various screen sizes such as desktop, tablet, and mobile devices.

### Tech Stack

* **Frontend:** HTML, CSS, JavaScript, Bootstrap
* **Backend:** Python, Django
* **Hosting:** Google Cloud Platform (GCP) App Engine
* **Tools:** Visual Studio Code, Docker

### Tools and Environments

- ```Django```: A high-level web development framework in Python that promotes fast and clean development. It facilitates the creation of robust and scalable web applications.
- ```Bootstrap```: A framework that simplifies the creation of responsive and modern user interfaces for websites and web applications, optimized for mobile devices.
- ```CSS```: Cascading Style Sheets language that enhances the visual presentation of HTML elements, improving design and user experience.
- ```JavaScript```: A programming language that creates interactive web experiences, allowing dynamic content manipulation and a richer user experience.
- ```Visual Studio Code```: A source code editor developed by Microsoft for Windows, Linux, and macOS. It offers extensions, integrated debugging, and is widely used in web application development.
- ```Docker```: Is used to create a consistent environment for deploying and running applications across different systems. It simplifies the process of packaging your project, dependencies, and configurations into containers that can be easily deployed on any machine that supports Docker.
- ```GCP App Engine```: A Google Cloud Platform service for hosting web applications. It provides a secure and scalable infrastructure for hosting applications in the cloud.

### Languages

- ```Python```: A high-level programming language widely used in web development, data science, and automation. Known for its readable syntax and support for libraries like Django.
- ```HTML```: The standard markup language for structuring content on web pages.
- ```CSS```: A language for styling and enhancing the visual presentation of HTML elements.
- ```JavaScript```: A browser programming language that enables the creation of interactive web applications.

## Hosting

The hosting service used is Google Cloud Platform (GCP), specifically hosted on App Engine. GCP offers a range of options to host websites, applications, and web services on Google’s global infrastructure. Google’s web hosting provides a flexible, scalable, and secure platform for hosting web applications and services. With a variety of service options, integration with other GCP services, and a high-performance global infrastructure, GCP is an excellent choice for hosting web projects in the cloud.

## Deployment

In this project, Docker is used to deploy the application to Google Cloud Platform (GCP) using the following files:

### `Dockerfile`
The `Dockerfile` defines the steps needed to build the Docker image for your application. It specifies the base image, installs required dependencies, copies the project files into the image, and sets up the environment to run your application. This file ensures that the app runs in a consistent environment regardless of where it is deployed.

### `app.yaml`
The `app.yaml` file is used for configuring the Google Cloud App Engine deployment. It defines settings like the runtime environment, instance class, and other parameters specific to GCP hosting. This file helps GCP understand how to handle the application and allocate resources.

### `docker-compose-deploy.yml`
The `docker-compose-deploy.yml` file is used for defining and running multi-container Docker applications in the deployment environment. It sets up how the Docker containers for the application will interact with each other in the cloud, making it easier to deploy complex applications that require more than one service.

### `docker-compose.yml`
The `docker-compose.yml` file is used for local development to define how the containers should be built and run on your local machine. It helps set up a local environment for testing and developing your application before deploying it to the cloud. This file specifies services, networks, and volumes used during development.

Together, these files allow the application to be built, tested, and deployed with Docker, ensuring a smooth and repeatable deployment process both locally and in the cloud.

## Usage

To explore the portfolio, navigate to the Projects section for a carousel view of various completed projects.
Use the navigation to access different sections and download files as needed.

## Installation

### Project Structure ###

- ```PortfolioWeb```: Contains the main application source code.
- ```src```: Contains files and documents from readme.md. 
- ```static```: Stores static files like CSS, JavaScript, and images.
- ```templates```: Houses HTML templates.
- ```requirements.txt```: Lists project dependencies.

### Clone, install and run the repository ###

```bash 
    git clone https://github.com/yourusername/your-repository.git
```
```bash 
    cd your-repository
```
```bash
    pip install -r requirements.txt
```
```bash
    python manage.py runserver
```

---

# Contributions

We welcome contributions! If you have improvement ideas, issues to report, or new features you’d like to add, feel free to open a pull request or an issue in this repository.

# Contact

If you have any questions, comments, or issues with the website, feel free to reach out to me.

- **Miguel Angel Dallanegra Vilches**
  - ![mail](_src/icons/mail.ico) [mdallanegra@icloud.com](mailto:mdallanegra@icloud.com)
  - <img src="https://img.icons8.com/globe--v1.png" width="16" height="16"> [mdallanegra.com](https://mdallanegra.com)
  - ![LinkedIn](_src/icons/linkedin.ico) [Miguel Dallanegra](https://www.linkedin.com/in/mdallanegra)
  - ![GitHub](_src/icons/github_mark_icon.ico) [mdallanegra](https://github.com/mdallanegra)
  
# Licenses

This project is under Licenses:

- [![Licencia GPL 3.0](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE-GPL)
- [![Licencia MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE-GPL)
- [![Licencia Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE-APACHE)

<p align="center">
    © 2024 Copyright: 
    <a href="https://mdallanegra.com">mdallanegra.com</a> | 
    <a href="https://mdallanegra.com.ar">mdallanegra.com.ar</a> | 
    <a href="https://mdallanegra.ar">mdallanegra.ar</a>
</p>

<p align="center">
    <a href="https://startbootstrap.com" title="WebTemplate">Web based on startbootstrap.com template under MIT license</a>
</p>