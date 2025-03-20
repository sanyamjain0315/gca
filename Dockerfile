FROM chrischoy/minkowski_engine:latest

WORKDIR /root

COPY ./requirements.txt /root

RUN pip install --no-cache-dir -r requirements.txt && pip install --no-index torch-scatter -f https://pytorch-geometric.com/whl/torch-1.12.0+cu113.html

COPY . /root

CMD [ "bash" ]
