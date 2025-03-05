# pdf-page-saver
Allows to save exact pages of PDF document

## How to invoke
python3 main.py -s "greek.pdf" -o out.pdf -p 55,12,127-129  
python3 main.py -s "greek.pdf" -o out.pdf -p 12  
python3 main.py -s "greek.pdf" -o out.pdf -p 127-129  
Please, pay attention, that it includes both boundaries, `127-129` will include `127,128,129` pages of the book  