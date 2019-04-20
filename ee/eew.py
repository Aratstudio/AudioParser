
import os
import requests
import shutil




box2='.mp3'
for i in range(1, 100):
        s = 'https://m1.audiokniga.club/uploads/books/book1123/rus/reader199/128/00' + str(i) + str(box2)
        print(s)

        (dirname, filename) = os.path.split(s)
        r = requests.get(s, stream=True)
        i
        if r.status_code == 200:
            with open(filename, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
