FROM chrischoy/minkowski_engine:latest

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt && pip install --no-index torch-scatter -f https://pytorch-geometric.com/whl/torch-1.12.0+cu113.html

COPY . .

CMD [ "bash" ]
