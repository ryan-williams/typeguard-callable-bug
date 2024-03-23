FROM python:3.11.8
RUN git clone https://github.com/ryan-williams/typeguard-issues
WORKDIR typeguard-issues
RUN pip install -e .
RUN pytest src/test_typeddict.py  # ❌ TypeError: TypedDict does not support instance and class checks
