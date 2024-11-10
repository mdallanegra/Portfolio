<p align="center">
    <img src="_src/logo/neuro-pathways-rm-bg.png" width="200" alt="Neuro Pathways Logo">
</p>


# Mi Portafolio Web<!-- omit in toc --> 

<p align="center">
    <strong><a href="README_es.md">Versión en Español</a></strong><br>
    <strong><a href="README_en.md">English Version</a></strong><br>
    <strong><a href="README.md">Versione Italiana prossimamente</a></strong><br>
    <strong><a href="README.md">Deutsche Version kommt bald</a></strong><br>
</p>

## Indice <!-- omit in toc --> 

- [Descripción general](#descripción-general)
  - [Características](#características)
    - [Stack tecnológico](#stack-tecnológico)
    - [Herramientas y entornos](#herramientas-y-entornos)
    - [Lenguajes](#lenguajes)
  - [Hosting](#hosting)
  - [Despliegue](#despliegue)
    - [`Dockerfile`](#dockerfile)
    - [`app.yaml`](#appyaml)
    - [`docker-compose-deploy.yml`](#docker-compose-deployyml)
    - [`docker-compose.yml`](#docker-composeyml)
- [Uso](#uso)
  - [Instalación](#instalación)
    - [Estructura del proyecto](#estructura-del-proyecto)
    - [Clonar, instalar y ejecutar el repositorio](#clonar-instalar-y-ejecutar-el-repositorio)
- [Contribuciones](#contribuciones)
- [Contacto](#contacto)
- [Licencias](#licencias)


---

# Descripción general

Bienvenido a mi portafolio web, que muestra mis proyectos profesionales, habilidades y experiencia en ciencia de datos, aprendizaje automático e ingeniería de software. Este sitio está diseñado con Django y Bootstrap para proporcionar una experiencia moderna y responsiva.

## Características

- **Exhibición de proyectos:** Una presentación estilo carrusel de mis proyectos, destacando los detalles clave y las tecnologías utilizadas.
- **Soporte multilingüe:** Disponible en inglés y español para mayor accesibilidad, y próximamente en alemán e italiano.
- **Recursos descargables:** Incluye enlaces descargables para mi CV en inglés y español.
- **Diseño responsivo:** Optimizado para varios tamaños de pantalla, como escritorio, tabletas y dispositivos móviles.

### Stack tecnológico

* **Frontend:** HTML, CSS, JavaScript, Bootstrap
* **Backend:** Python, Django
* **Hosting:** Google Cloud Platform (GCP) App Engine
* **Herramientas:** Visual Studio Code, Docker

### Herramientas y entornos

- ```Django```: Framework de desarrollo web de alto nivel en Python que fomenta el desarrollo rápido y limpio. Facilita la creación de aplicaciones web robustas y escalables.
- ```Bootstrap```: Framework que facilita la creación de interfaces de usuario responsivas y modernas para sitios y aplicaciones web, optimizado para dispositivos móviles.
- ```CSS```: Lenguaje de estilos en cascada que facilita la presentación visual de los elementos HTML, mejorando el diseño y la experiencia de usuario.
- ```JavaScript```: Lenguaje de programación para crear experiencias interactivas en la web, permitiendo manipulación dinámica del contenido de la página y una experiencia de usuario más rica.
- ```Visual Studio Code```: Editor de código fuente desarrollado por Microsoft para Windows, Linux y macOS. Ofrece extensiones, depuración integrada, y es ampliamente utilizado en el desarrollo de aplicaciones web.
- ```Docker```: Se utiliza para crear un entorno consistente para desplegar y ejecutar aplicaciones en diferentes sistemas. Simplifica el proceso de empaquetar tu proyecto, dependencias y configuraciones en contenedores que pueden ser fácilmente desplegados en cualquier máquina que soporte Docker.
- ```GCP App Engine```: Servicio de Google Cloud Platform para el hosting de aplicaciones web. Proporciona una infraestructura segura y escalable para alojar aplicaciones en la nube.

### Lenguajes

- ```Python```: Lenguaje de programación de alto nivel ampliamente utilizado en desarrollo web, ciencia de datos, y automatización. Es conocido por su sintaxis legible y su soporte a bibliotecas como Django.
- ```HTML```: Lenguaje de marcado estándar para estructurar el contenido de las páginas web.
- ```CSS```: Lenguaje que permite estilizar y mejorar la presentación visual de los elementos HTML.
- ```JavaScript```: Lenguaje para programación en el navegador que permite la creación de aplicaciones web interactivas.

## Hosting

Se utilizará el servicio de hosting web de Google Cloud Platform (GCP), mas precisamente se alojará en el servicio de App Engine. Que ofrece una variedad de opciones para alojar sitios, aplicaciones y servicios web en la infraestructura global de Google. El hosting web de Google ofrece una plataforma flexible, escalable y segura, para alojar aplicaciones y servicios web. Con una variedad de opciones de servicio, integración con otros servicios de GCP y una infraestructura global de alto rendimiento, GCP es una excelente opción para alojar proyectos web en la nube.

## Despliegue

En este proyecto, Docker se utiliza para desplegar la aplicación en Google Cloud Platform (GCP) utilizando los siguientes archivos:

### `Dockerfile`
El `Dockerfile` define los pasos necesarios para construir la imagen Docker de tu aplicación. Especifica la imagen base, instala las dependencias necesarias, copia los archivos del proyecto a la imagen y configura el entorno para ejecutar la aplicación. Este archivo asegura que la app se ejecute en un entorno consistente sin importar dónde se despliegue.

### `app.yaml`
El archivo `app.yaml` se utiliza para configurar el despliegue en Google Cloud App Engine. Define parámetros como el entorno de ejecución, la clase de instancia y otros parámetros específicos del hosting en GCP. Este archivo ayuda a GCP a entender cómo manejar la aplicación y asignar recursos.

### `docker-compose-deploy.yml`
El archivo `docker-compose-deploy.yml` se utiliza para definir y ejecutar aplicaciones Docker con múltiples contenedores en el entorno de despliegue. Establece cómo los contenedores Docker para la aplicación interactuarán entre sí en la nube, facilitando el despliegue de aplicaciones complejas que requieren más de un servicio.

### `docker-compose.yml`
El archivo `docker-compose.yml` se utiliza para el desarrollo local, definiendo cómo se deben construir y ejecutar los contenedores en tu máquina local. Ayuda a configurar un entorno local para probar y desarrollar la aplicación antes de desplegarla en la nube. Este archivo especifica los servicios, redes y volúmenes utilizados durante el desarrollo.

Juntos, estos archivos permiten que la aplicación sea construida, probada y desplegada con Docker, asegurando un proceso de despliegue fluido y repetible tanto localmente como en la nube.

# Uso

Para explorar el portafolio, navega a la sección de Proyectos para ver un carrusel con diversos proyectos completados. 
Usa la navegación para acceder a diferentes secciones y descargar archivos según sea necesario.

## Instalación

### Estructura del proyecto ###

- ```PortfolioWeb```: Contiene el código fuente de la aplicación principal.
- ```src```: Contiene archivos y documentos del readme.md.
- ```static```: Almacena archivos estáticos como CSS, JavaScript e imágenes.
- ```templates```: Contiene las plantillas HTML.
- ```requirements.txt```: Lista las dependencias del proyecto.

### Clonar, instalar y ejecutar el repositorio ###

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

# Contribuciones

¡Estamos abiertos a contribuciones! Si tienes ideas de mejora, problemas que reportar o características nuevas que te gustaría añadir, no dudes en abrir una solicitud de extracción o un problema en este repositorio.

# Contacto

Si tienes alguna pregunta, comentario o problema con la página web, no dudes en ponerte en contacto conmigo.

- **Miguel Angel Dallanegra Vilches**
  - ![mail](_src/icons/mail.ico) [mdallanegra@icloud.com](mailto:mdallanegra@icloud.com)
  - <img src="https://img.icons8.com/globe--v1.png" width="16" height="16"> [mdallanegra.com](https://mdallanegra.com)
  - ![LinkedIn](_src/icons/linkedin.ico) [Miguel Dallanegra](https://www.linkedin.com/in/mdallanegra)
  - ![GitHub](_src/icons/github_mark_icon.ico) [mdallanegra](https://github.com/mdallanegra)
  
# Licencias

Este proyecto está bajo las Licencias:

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
    <a href="https://startbootstrap.com">Web basada en plantilla de startbootstrap.com bajo licencia MIT</a>
</p>