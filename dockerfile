FROM python:3.7
RUN pip install pandas requests
WORKDIR .
COPY pipeline.py .

CMD [ "python", "pipeline.py" ] 