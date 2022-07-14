# Photo Translation Web App 

The main objective of this study is to develop “PicSlate”, a photo translation web application that can take scene images with text in Chavacano, Kinaray-a, 
and Hiligaynon languages and translate them into Filipino, applied with image text extraction and text translation algorithms.

## Specific Objectives:
<ul>
<li>To apply image pre-processing techniques used in computer vision to minimize noise on scene images before text extraction process;</li>
<li>To apply Stroke Width Transform (SWT) with Canny Edge Detector for the text feature extraction process; </li>
<li>To build a moderately developed parallel corpus for the low resource languages Cavite Chavacano, Hiligaynon and Kinaray-a; </li>
<li>To make use of the Seq2Seq LSTM-RNN for neural machine translation.</li>
</ul>

<hr>

1. Clone repository 
2. Install Tesseract on machine 

_NOTE: If you are using mac, `brew install tesseract` into your terminal._

3. Install requirements.txt 
4. Set environment variable for FLASK_APP

_On Linux and macOS, `export FLASK_APP=flask_factory`;_

_On Windows, `set FLASK_APP=flask_factory` or `$env:FLASK_APP = "flask_factory"`_

5. `flask run`


## Demo



https://user-images.githubusercontent.com/66836831/179000565-ce1a5515-cc10-4d33-bfb0-2508d68f9a75.mp4




