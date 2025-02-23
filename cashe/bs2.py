from bs4 import BeautifulSoup

# Чтение HTML-кода из файла
with open("page_source.html", "r", encoding="utf-8") as file:
    html = file.read()

# Парсим HTML с помощью BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Поиск таблицы с классом "main" в <body>
body = soup.body
if body:
    table = body.find("table", class_="main")
    if table:
        # print("Found the table with class 'main'. Searching for elements with classes 'rcnt tr_0' and 'rcnt tr_1'...")
        # results = []
        # results.append(table.t)
        # Поиск всех div с классами "rcnt tr_0" и "rcnt tr_1"
        # print(table.text.strip())
        elements = table.find_all("div", class_=["rcnt tr_0", "rcnt tr_1", "rcnt tr_2"])
        
        print(f"Total elements found: {len(elements)}")
        results = []
        count_false = 0
        count_true = 0
        count_none = 0
        
        for element in elements:

            # Извлечение команды из class="tnms"
            tnms_div = element.find("div", class_="tnms")
            team_name = None
            if tnms_div:
                meta_tag = tnms_div.find("meta", itemprop="name")
                if meta_tag and meta_tag.has_attr("content"):
                    
                    team_name = meta_tag["content"]

            # Извлечение вероятности из class="fprc"
            probability_div = element.find("div", class_="fprc")
            probability = None
            if probability_div:
                probability_span = probability_div.find("span", class_="fpr")
                if probability_span == None:
                    probability_span = probability_div.find("b")    
                if probability_span:
                    
                    probability = probability_span.text.strip()

            # Извлечение прогноза из class="predict"
            predict_div = element.find("div", class_=["predict", "predict_y","predict_no"])
            prediction = None
            if predict_div:
                forepr_span = predict_div.find("span", class_="forepr")
                if forepr_span:
                    nested_span = forepr_span.find("span")
                    if nested_span:
                        prediction = nested_span.text.strip()

            # Извлечение прогноза из class="lscr_td"
            scores_div = element.find("div", class_="lscr_td")
            
            scores = None
            if scores_div:
                scores_span = scores_div.find("span", class_="lscrsp")
                if scores_span:
                    nested_span = scores_span.find("b", class_="l_scr")
                    if(scores_span):
                        scores = scores_span.text.strip()

            # Проверка результата
            if team_name or probability or prediction or scores:
                if(probability):
                        if int(probability)>=0:
                            is_success = None
                            if(scores):
                                parts = scores.split("-")
                                part1 = int(parts[0])
                                part2 = int(parts[1])
                                if not(part1 == 0) and not (part2 == 0):
                                    is_both_team_score = True
                                else:
                                    is_both_team_score = False
                                if prediction == "Yes":
                                    prediction_bool = True
                                if prediction == "No":
                                    prediction_bool = False
                                if is_both_team_score is not None and prediction_bool is not None:
                                    if is_both_team_score == prediction_bool:
                                        is_success = True
                                        count_true = 1 + count_true

                                    else:
                                        is_success = False
                                        count_false = 1 + count_false
                            if is_success is None:
                                
                                count_none = count_none + 1
                

            # Собираем данные, если они найдены
            if team_name or probability or prediction or scores:
                if(probability):
                    if int(probability)>=0 :
                        results.append({
                            "Team": team_name,
                            "Probability": probability,
                            "Prediction": prediction,
                            "Scores": scores,
                            "IsSuccess": is_success
                            
                        })
        
        print("***************"*8)
        # Сохраняем результаты в файл
        if results:
            print(f"Found {len(results)} records. Saving results to file...")
            with open("extracted_results.txt", "w", encoding="utf-8") as output_file:
                for result in results:
                    output_file.write(f"Team: {result['Team']}, Probability: {result['Probability']}, Prediction: {result['Prediction']}, Scores: {result["Scores"]}, IsSuccess: {result["IsSuccess"]}\n")
                output_file.write(f"count True : {count_true},   count False : {count_false}, count None : {count_none}")
            print("Results saved to 'extracted_results.txt'.")
        else:
            print("No matching elements found.")
    else:
        print("No table with class 'main' found in the body.")
else:
    print("<body> tag not found in the HTML document.")