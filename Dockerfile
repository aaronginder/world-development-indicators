FROM python3.7
WORKDIR /app
COPY requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
ENV PYTHONPATH /app
ENTRYPOINT ["python3"]
CMD ["./testa.py"]