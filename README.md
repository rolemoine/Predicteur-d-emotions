<div align="center">
  <h1>
    <br>
    <a href=""><img src="favicon.png" alt="Bad or Good" width="200"></a>
    <br>
      Detection emotion 
    <br>
  </h1>
</div>

<div align="center">
  <a href="#a-propos">A propos</a> •
  <a href="#installation">Installation</a> •
  <a href="#technologies">Technologie utilisé</a> 
</div>

## A propos

Ce repository est composé d'un serveur et d'un client.
Projet universitaire en groupe 

## A faire :

Voir le Jira du projet

## Technologies

Client : 
```
  # Framework : 
    - NuxtJS

  # Package :
    - axios
```

Server :
```
  # Environnement : 
    - NodeJS
  
  # Base de donnée : 
    - MySQL
  
  # Package : 
    - expressJS
    - cors
    - helmet
    - express-rate-limit
```

Model & Accuracy: 
```
  # Traditional methods : 
    - Logistic Regression 87.40
    - Naïve Bayes (in process)

  # Deep Learning methods :
    - RNN (LSTM) 77.07
    - DNN (BERT) 93.02
```
## Installation

Depuis votre terminal de commande : 

```bash
# Cloner le repertoire
$ git clone https://github.com/Andy-d-g/Form-Authentification.git

# Aller dans le repertoire
$ cd Predicteur-d-emotions/

# Installer les packages (server) [ / ]
$ cd Server
$ npm ci

# Lancer le server en hotload [ /Server ]
$ npm run start

# Installer les package (client) [ /Client ]
$ cd Client
$ npm ci

# Lancer le projet
$ npm run dev

# Se rendre sur la page web : http://localhost:3000/

```

Build & Run model with Docker : 
- [How to install docker](https://docs.docker.com/engine/install/)

```bash
# build docker image
sudo docker build -t mymodel -f Dockerfile .

# run docker image 
sudo docker run -p 8000:8000 mymodel

# use : 
http://localhost:8000/text/{text to predict}
```
Use this docker command to delete everything :
```bash
docker system prune -a --volumes

WARNING! This will remove:
    - all stopped containers
    - all networks not used by at least one container
    - all volumes not used by at least one container
    - all images without at least one container associated to them
    - all build cache
```

## Sources
- [Bert Model](https://skimai.com/fine-tuning-bert-for-sentiment-analysis/)

## Contributeurs

@Andy-d-g
