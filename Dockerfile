FROM python3
RUN mkdir /app
WORKDIR /app
ADD requiremens.txt /app
ADD main.py /app
RUN pip3 install -r requiremens.txt
CMD ["gunicorn", "-w 4", "-b", "0.0.0.0:8000" "main:app"]