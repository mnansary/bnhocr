# bnhocr
Optical Character Recognition for bangla handwritten and printed documents
> Single Grapheme Prediction based model, Bangla HOCR

```python
   version:0.0.1
   authors:MD.Nazmuddoha Ansary, (team ovijatrik,apsis solutions ltd,bengali.ai)
           MD.Mobassir Hossain,  (team ovijatrik,apsis solutions ltd,bengali.ai) 
           MD.Aminul Islam       (team ovijatrik)
```
**This project was created in association with**:
* [Apsis Solutions LTD](https://apsissolutions.com/)
* [Bengali.ai](https://bengali.ai/)

![](/resources/apsis.png)
![](/resources/bai.png)

# Environment
* For **ubuntu** install tesseract bangla: ```install tesseract-ocr-ben```
* For **windows** (**Untested** [source](https://stackoverflow.com/questions/63048908/how-do-i-install-a-new-language-pack-for-tesseract-on-windows)):
    * Download and install tesseract-ocr-w64-setup-v5.0.0-rc1.20211030.exe (or the latest one)
    * Open https://github.com/tesseract-ocr/tessdata and download your language. For example, for Bangla download ben.traineddata.
    * Copy the downloaded file to the tessreact_ocr installation location, some location like: C:\Program Files\Tesseract-OCR\tessdata
    * Don't forget to use the traineddata name for the language. For bangla, I use lang='ben'.

**python requirements**

* **pip requirements**: ```pip install -r requirements.txt``` 

> Its better to use a virtual environment 
> Some of the pip requirements may not work properly due to locally saved modules
> OR use conda-

* Preffered way: **conda**: use environment.yml: ```conda env create -f environment.yml```


**model requirements**
* Download [model.h5 file](https://drive.google.com/file/d/1urxvfuO3edpW4HDzFTIIhcFPPmos1hcG/view?usp=sharing)
* place the **model.h5** file under **models** folder


**LOCAL ENVIRONMENT/TESTING ENVIRONMENT**  

```python
OS          : Ubuntu 20.04.3 LTS       
Memory      : 23.4 GiB 
Processor   : Intel® Core™ i5-8250U CPU @ 1.60GHz × 8    
Graphics    : Intel® UHD Graphics 620 (Kabylake GT2)  
Gnome       : 3.36.8
```

# About bnhocr: Printed and Handwritten text recognition
There are available models such as : [tesseract](https://github.com/tesseract-ocr/tesseract),[Easy OCR](https://github.com/JaidedAI/EasyOCR). that covers bangla printed text to a considerable accuracy.In this project we solely focus on handwritten texts.

* The idea of **bnhocr** project is to convert handwritten graphemes to a unique representational space (in our example font faced image).
* Converting single graphemes **does not cover words**. Separated graphemes can be used if a grapheme localization model is used.[Watch This Video To For The Basic Idea](https://www.youtube.com/watch?v=7Ye9oV1MqbU) 

![](/resources/idea.png)

* To extend for words, we build on single grapheme transformation model and extend on handwritten words.
* Then we use an existing recognizer (in our example-tesseract)

![](/resources/implementation.png)

* A short presentation about this work is available at **resources/slides.pdf**



# Demo
* clone the repo
* install dependencies 
* ``` streamlit run app.py```

![](/resources/demo.png)

# Graphemes
* To understand the concept of bangla graphemes: [A large multi-target dataset of common bengali handwritten graphemes](https://www.springerprofessional.de/en/a-large-multi-target-dataset-of-common-bengali-handwritten-graph/19631662)
* Cite the paper if you find it useful in your research
```bibtext
@inproceedings{alam2021large,
  title={A large multi-target dataset of common bengali handwritten graphemes},
  author={Alam, Samiul and Reasat, Tahsin and Sushmit, Asif Shahriyar and Siddique, Sadi Mohammad and Rahman, Fuad and Hasan, Mahady and Humayun, Ahmed Imtiaz},
  booktitle={International Conference on Document Analysis and Recognition},
  pages={383--398},
  year={2021},
  organization={Springer}
}
```

# Known Issues
* **model is not cached while running in streamlit**
* **only launched for tesseract**
  * Easy OCR and Detection models can be easily added for wide applications 