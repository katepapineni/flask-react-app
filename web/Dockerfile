FROM node:13.12.0-alpine

WORKDIR /src

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt 

COPY . .

ENV PYTHONPATH=/src

EXPOSE 4433 

ENTRYPOINT [ "python" ] 

CMD [ "app/api/endpoints.py" ] 