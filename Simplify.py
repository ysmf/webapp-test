from pythainlp.tokenize import Tokenizer

# เปิดไฟล์ custom dictionary และอ่านคำในไฟล์
with open("words_th.txt", encoding="utf-8") as f:
    custom_words = f.read().splitlines()

# สร้างตัว Tokenizer ด้วย custom dictionary
tokenizer = Tokenizer(custom_words)

textN = "คำว่า ของจริง นั้น เป็นคำของคำนามที่สือแทนถึงความรักที่แท้จริงในการ์ตูนเรื่อง Yahari ซึ่งเป็นสิ่งที่ได้เปิดเผยคำว่า ของจริง ครั้งแรกเมื่อมีซีซั่นสองของการ์ตูนเรื่องนี้ ทำให้ ของจริงเป็น"
textN = textN.replace(" ", "")
tokensN = tokenizer.word_tokenize(textN)
b_join = ''.join(tokensN)
a_join = [b_join]
print(a_join)

