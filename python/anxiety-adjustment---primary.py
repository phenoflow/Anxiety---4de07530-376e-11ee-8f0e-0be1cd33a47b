# Matthew J Carr, Darren M Ashscroft, Evangelos Kontopantelis, David While, Yvonne Awenant, Jayne Cooper, Carolyn Chew-Graham, Nav Kapur, Roger T Webb, 2023.

import sys, csv, re

codes = [{"code":"E29..00","system":"readv2"},{"code":"E293000","system":"readv2"},{"code":"E293200","system":"readv2"},{"code":"E29y.00","system":"readv2"},{"code":"E29y200","system":"readv2"},{"code":"E29y400","system":"readv2"},{"code":"E29y500","system":"readv2"},{"code":"E29yz00","system":"readv2"},{"code":"E29z.00","system":"readv2"},{"code":"Eu43200","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('anxiety-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["anxiety-adjustment---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["anxiety-adjustment---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["anxiety-adjustment---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
