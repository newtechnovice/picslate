import io
from flask import Blueprint
from flask import render_template, request

import cv2
import numpy as np
from swtloc import SWTLocalizer
import pytesseract

bp = Blueprint('activity', __name__, template_folder='templates')


@bp.route('/', methods=['POST'])
def do_something():
    if request.method == 'POST' and 'photo' in request.files:
        photo = request.files['photo']  # the posted image will be stored here
        in_memory = io.BytesIO()
        photo.save(in_memory)

        data = np.fromstring(in_memory.getvalue(), dtype=np.uint8)
        img = cv2.imdecode(data, cv2.IMREAD_COLOR)

        # Resize image
        scale_percent = 80
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)

        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

        # Text extraction process
        swt = SWTLocalizer()

        if 'dark-text' in request.form:
            mode = 'lb_df'
        else:
            mode = 'db_lf'

        swt.swttransform(image=resized, edge_func='ac', ac_sigma=1.0, text_mode=mode,
                             gs_blurr=True, blurr_kernel=(5, 5), minrsw=3,
                             maxCC_comppx=5000, maxrsw=200, max_angledev=np.pi / 6,
                             acceptCC_aspectratio=5.0, save_results=False, save_rootpath='home/picslateqa/picslate/SWTResults/')

        # Text identification (OCR)
        result = pytesseract.image_to_string(swt.swt_mat, lang='eng', config='--psm 4')

        return render_template(
            '/index.html',
            phrase_output=result.strip(),
            isSubmit=True
        )
