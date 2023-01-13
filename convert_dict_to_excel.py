import pandas as pd

#testline:
my_dict = {
    'Ето как ChatGPT вместо мен реши теста по програмиране в интервюто за започване на работа': 'https://www.kaldata.com/it-%d0%bd%d0%be%d0%b2%d0%b8%d0%bd%d0%b8/%d0%b5%d1%82%d0%be-%d0%ba%d0%b0%d0%ba-chatgpt-%d0%b2%d0%bc%d0%b5%d1%81%d1%82%d0%be-%d0%bc%d0%b5%d0%bd-%d1%80%d0%b5%d1%88%d0%b8-%d1%82%d0%b5%d1%81%d1%82%d0%b0-%d0%bf%d0%be-%d0%bf%d1%80%d0%be%d0%b3-404070.html',
    'IMG DXT: нов мобилен графичен процесор с поддръжка на трасирането на лъчите': 'https://www.kaldata.com/%d1%82%d0%b5%d0%bb%d0%b5%d1%84%d0%be%d0%bd%d0%b8/img-dxt-%d0%bd%d0%be%d0%b2-%d0%bc%d0%be%d0%b1%d0%b8%d0%bb%d0%b5%d0%bd-%d0%b3%d1%80%d0%b0%d1%84%d0%b8%d1%87%d0%b5%d0%bd-%d0%bf%d1%80%d0%be%d1%86%d0%b5%d1%81%d0%be%d1%80-%d1%81-%d0%bf%d0%be%d0%b4%d0%b4-404079.html',
    'Заглушават GPS сигналите покрай българското крайбрежие – източникът за сега е неизвестен': 'https://www.kaldata.com/it-%d0%bd%d0%be%d0%b2%d0%b8%d0%bd%d0%b8/%d0%b7%d0%b0%d0%b3%d0%bb%d1%83%d1%88%d0%b0%d0%b2%d0%b0%d1%82-gps-%d1%81%d0%b8%d0%b3%d0%bd%d0%b0%d0%bb%d0%b8%d1%82%d0%b5-%d0%bf%d0%be%d0%ba%d1%80%d0%b0%d0%b9-%d0%b1%d1%8a%d0%bb%d0%b3%d0%b0%d1%80%d1%81-403838.html',
    'Проучване: 6G технологията ще се предава чрез … хората': 'https://www.kaldata.com/it-%d0%bd%d0%be%d0%b2%d0%b8%d0%bd%d0%b8/%d0%bf%d1%80%d0%be%d1%83%d1%87%d0%b2%d0%b0%d0%bd%d0%b5-6g-%d1%82%d0%b5%d1%85%d0%bd%d0%be%d0%bb%d0%be%d0%b3%d0%b8%d1%8f%d1%82%d0%b0-%d1%89%d0%b5-%d1%81%d0%b5-%d0%bf%d1%80%d0%b5%d0%b4%d0%b0%d0%b2%d0%b0-403767.html',
    'Intel чупи бариерата от 6GHz с процесора Core i9-13900KS с цена 699 долара': 'https://www.kaldata.com/%d1%85%d0%b0%d1%80%d0%b4%d1%83%d0%b5%d1%80/intel-%d1%87%d1%83%d0%bf%d0%b8-%d0%b1%d0%b0%d1%80%d0%b8%d0%b5%d1%80%d0%b0%d1%82%d0%b0-%d0%be%d1%82-6ghz-%d1%81-%d0%bf%d1%80%d0%be%d1%86%d0%b5%d1%81%d0%be%d1%80%d0%b0-core-i9-13900ks-%d1%81-%d1%86-404161.html',
    'Lenovo ThinkPad Z13: Еволюция в действие': 'https://www.kaldata.com/%d1%80%d0%b5%d0%b2%d1%8e%d1%82%d0%b0/lenovo-thinkpad-z13-%d0%b5%d0%b2%d0%be%d0%bb%d1%8e%d1%86%d0%b8%d1%8f-%d0%b2-%d0%b4%d0%b5%d0%b9%d1%81%d1%82%d0%b2%d0%b8%d0%b5-399936.html',
    'НАСА работи върху хибридната мисия до Титан и още над дузина проекти в космоса': 'https://www.kaldata.com/it-%d0%bd%d0%be%d0%b2%d0%b8%d0%bd%d0%b8/%d0%ba%d0%be%d1%81%d0%bc%d0%be%d1%81/%d0%bd%d0%b0%d1%81%d0%b0-%d1%80%d0%b0%d0%b1%d0%be%d1%82%d0%b8-%d0%b2%d1%8a%d1%80%d1%85%d1%83-%d1%85%d0%b8%d0%b1%d1%80%d0%b8%d0%b4%d0%bd%d0%b0%d1%82%d0%b0-%d0%bc%d0%b8%d1%81%d0%b8%d1%8f-%d0%b4%d0%be-404112.html',
    'Историческото първо изстрелване на ракета от британска територия претърпя провал': 'https://www.kaldata.com/it-%d0%bd%d0%be%d0%b2%d0%b8%d0%bd%d0%b8/%d0%b8%d1%81%d1%82%d0%be%d1%80%d0%b8%d1%87%d0%b5%d1%81%d0%ba%d0%be%d1%82%d0%be-%d0%bf%d1%8a%d1%80%d0%b2%d0%be-%d0%b8%d0%b7%d1%81%d1%82%d1%80%d0%b5%d0%bb%d0%b2%d0%b0%d0%bd%d0%b5-%d0%bd%d0%b0-%d1%80-403804.html',
    'Razer допълва линията си лаптопи с високотехнологичните Blade 16 и Blade 18': 'https://www.kaldata.com/%d1%85%d0%b0%d1%80%d0%b4%d1%83%d0%b5%d1%80/razer-%d0%b4%d0%be%d0%bf%d1%8a%d0%bb%d0%b2%d0%b0-%d0%bb%d0%b8%d0%bd%d0%b8%d1%8f%d1%82%d0%b0-%d1%81%d0%b8-%d0%bb%d0%b0%d0%bf%d1%82%d0%be%d0%bf%d0%b8-%d1%81-%d0%b2%d0%b8%d1%81%d0%be%d0%ba%d0%be%d1%82-403336.html',
    'Срокът за кандидатстване за космическия лагер Space Camp Turkey се удължава': 'https://www.kaldata.com/it-%d0%bd%d0%be%d0%b2%d0%b8%d0%bd%d0%b8/%d0%ba%d0%be%d1%81%d0%bc%d0%be%d1%81/%d1%81%d1%80%d0%be%d0%ba%d1%8a%d1%82-%d0%b7%d0%b0-%d0%ba%d0%b0%d0%bd%d0%b4%d0%b8%d0%b4%d0%b0%d1%82%d1%81%d1%82%d0%b2%d0%b0%d0%bd%d0%b5-%d0%b7%d0%b0-%d0%ba%d0%be%d1%81%d0%bc%d0%b8%d1%87%d0%b5%d1%81-404162.html',
    'Русия ще остави Союз в орбита! Ще издигне нов кораб, който да прибере руските астронавти на Земята': 'https://www.kaldata.com/it-%d0%bd%d0%be%d0%b2%d0%b8%d0%bd%d0%b8/%d1%80%d1%83%d1%81%d0%b8%d1%8f-%d1%89%d0%b5-%d0%be%d1%81%d1%82%d0%b0%d0%b2%d0%b8-%d1%81%d0%be%d1%8e%d0%b7-%d0%b2-%d0%be%d1%80%d0%b1%d0%b8%d1%82%d0%b0-%d1%89%d0%b5-%d0%b8%d0%b7%d0%b4%d0%b8%d0%b3%d0%bd-404052.html'}


def convert_dict_to_excel(my_dict):

    # convert into dataframe
    df = pd.DataFrame(data=my_dict, index=[1])

    # convert to excel
    df.to_excel("news.xlsx", index=True)
    #
    #
    #
    #
    #
    # # convert into excel
    # df.to_excel("students.xlsx", index=False)
    # print("Dictionary converted into excel...")

#testline:
convert_dict_to_excel(my_dict)