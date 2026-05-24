import logging

logging.basicConfig(filename='logs.log', filemode='w', level=logging.DEBUG)

def hello(name):
    logging.info(f"Hello {name}")

hello("World")
hello("World")
hello("World")
hello("World")
