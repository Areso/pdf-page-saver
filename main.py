import argparse
import re
import sys
from PyPDF2 import PdfReader, PdfWriter

def prepare_array(raw_pages):
    pattern_allowed_symbols = r'^[0-9\-,]+$'
    pattern_range           = r'^[1-9]\d*-[1-9]\d*$'
    prepared_pages = []
    if not re.match(pattern_allowed_symbols, raw_pages):
        return "", 1
    
    pages_arr: str    = raw_pages.split(",")

    for pages_record in pages_arr:
        if "-" in pages_record:
            if not re.match(pattern_range, pages_record):
                return "", 1
            hyphen_index = pages_record.find("-")
            left_no      = int(pages_record[:hyphen_index])
            right_no     = int(pages_record[hyphen_index+1:])
            for current_p in range(left_no,right_no+1):
                prepared_pages.append(current_p)
        else:
            prepared_pages.append(int(pages_record))
    return sorted(prepared_pages), 0


def resave_pdf(input_path: str, output_path: str, raw_pages)->int:
    prep_pages, err = prepare_array(raw_pages)
    if err == 1:
        return 1
    reader = PdfReader(input_path)
    writer = PdfWriter()
    # Iterate through all pages and add them to the writer
    for page in reader.pages:
        if i in prep_pages:
            writer.add_page(page)
    # Add metadata (optional)
    writer.add_metadata(reader.metadata)
    # Write the compressed PDF
    with open(output_path, "wb") as compressed_pdf:
        writer.write(compressed_pdf)
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s","--source_file", help="source filename",
                        type=str)
    parser.add_argument("-o","--output_file", help="source filename",
                        type=str)
    parser.add_argument("-p","--pages", 
                        help="pages to save, divided by comma or X-Y notation",
                        type=str)
    args = parser.parse_args()
    print(args.source_file)
    print(args.output_file)
    print(args.pages)
    if args.source_file is None:
        print("Please, provide source filename. Exiting")
        sys.exit()
    if args.output_file is None:
        print("Please, provide output filename. Exiting")
        sys.exit()
    if args.pages is None:
        print("Please, provide pages numbers to save, comma or hyphen divided. Exiting")
        sys.exit()
    resave_pdf(args.source_file, args.output_file, args.pages)
