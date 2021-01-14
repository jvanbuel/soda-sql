FROM python:3.7-slim

ENV PYTHONPATH "${PYTHONPATH}:/soda"

ADD sodasql /soda/sodasql
ADD tests /soda/tests
ADD README.md /soda
ADD requirements.txt /soda
ADD setup.py /soda

WORKDIR /soda

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "sodasql/cli/cli.py"]