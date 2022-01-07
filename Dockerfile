FROM continuumio/miniconda3:latest as conda-node
SHELL ["/bin/bash", "-c"]
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV BACKEND=/app/backend
EXPOSE 80
COPY ./script/ $BACKEND
WORKDIR $BACKEND
RUN . /root/.bashrc && conda init bash && conda env create -f environment.yml
# deployed version
CMD . /root/.bashrc && conda activate covid-polygraph && uvicorn main:app --host 0.0.0.0 --port 80