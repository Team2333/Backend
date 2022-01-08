# Backend code for covid-polygraph.

![ci](https://github.com/Team2333/Backend/workflows/ci/badge.svg)
Covid-polygraph, a set of Machine Learning-driven fact-checking tools that aim to address the issue of misleading information related to COVID-19.

Project is extended based on our [CS3244 Team Project](https://github.com/FightCovid-SG/CS3244-Team15) 
and more on code reference and reuse can be found in the [Offline Training Pipeline Repository](https://github.com/Team2333/offline-training-pipeline).

## How to use
To run the code, use Docker:
```bash
docker build . -t covid-polygraph:latest
```
Afterwards, you can start the backend locally using the docker image built. For our team, we deploy this image onto our remote server for api access.

## More about our project
Frontend code can be found [here](https://github.com/Team2333/covid-polygraph-frontend)

Offline Training Pipeline code can be found [here](https://github.com/Team2333/offline-training-pipeline)

More information about our project can be found on [devpost](https://devpost.com/software/covid-polygraph)
