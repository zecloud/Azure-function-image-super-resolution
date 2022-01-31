import logging
import ddddsr
import azure.functions as func
from PIL import Image
import io
from numpy import asarray

def main(msg: func.QueueMessage,inputImg:bytes,outputImg:func.Out[func.InputStream]) -> None:
    logging.info('Python queue trigger function processed a queue item: %s',
                 msg.get_body().decode('utf-8'))
    PilimageGangogh = Image.open(io.BytesIO(inputImg))
    numpydata = asarray(PilimageGangogh)
    Hdnumpydata=ddddsr.SR(scale=4)(numpydata)
    PilImgHd = Image.fromarray(Hdnumpydata)
    dataout = io.BytesIO()
    PilImgHd.save(dataout,'jpeg')
    dataout.seek(0)
    outputImg.set(dataout)


