# thai-word-segmentation-sentencepiece
thai word segmentation using sentencepiece

## Install

- sentencepiece : https://github.com/google/sentencepiece

then install pythaipiece

```
pip3 install https://github.com/wannaphongcom/thai-word-segmentation-sentencepiece/archive/master.zip
```



## Using

```python
>>> import pythaipiece
>>> pythaipiece.segment("ทดสอบการตัดคำภาษาไทยครับ แล้วคุณทำอะไร")
['ทดสอบ', 'การ', 'ตัด', 'คํา', 'ภาษาไทย', 'ครับ', '', 'แล้ว', 'คุณ', 'ทํา', 'อะไร']
```

