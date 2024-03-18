
FROM python:3.9

ADD Data_Analysis_IPC.py .

RUN pip install requests beautifulsoup4

CMD ["python", "./Data_Analysis_IPC.py"]