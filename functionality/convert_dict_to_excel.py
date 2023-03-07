import xlsxwriter
from xlsx2html import xlsx2html


def create_hyperlinks_file(my_dict):

    workbook = xlsxwriter.Workbook('news.xlsx')
    worksheet = workbook.add_worksheet()
    print("dictionary is being converted to a xlsx file...")
    for i, (article, link) in enumerate(my_dict.items()):
        sheet_row = "A" + str(i+1)

        worksheet.write_url(sheet_row, link, string=article, tip='open this article')

    workbook.close()


def xlsx_to_html():
    out_stream = xlsx2html('news.xlsx')
    out_stream.seek(0)
    return out_stream.read()




