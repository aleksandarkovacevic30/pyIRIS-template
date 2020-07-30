FROM python:3

WORKDIR /usr/src/app


COPY globals.py ./globals.py

RUN set -ex \
    && wget -O irisnative-1.0.0-cp34-abi3-linux_x86_64.whl "https://github.com/intersystems/quickstarts-python/raw/master/Solutions/nativeAPI_wheel/irisnative-1.0.0-cp34-abi3-linux_x86_64.whl" \
    && pip install irisnative-1.0.0-cp34-abi3-linux_x86_64.whl \
    && rm irisnative-1.0.0-cp34-abi3-linux_x86_64.whl

CMD [ "python", "./globals.py" ]
