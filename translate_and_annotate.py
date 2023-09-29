#%%
import json
import openai

functions = [{
    "name": "translate_and_annotate",
    "description": "Translates the text from Chinese to English and annotates it incisively with annotation using unique prefix [@ft1], [@ft2] etc.",
    "parameters": {
        "type": "object",
        "properties": {
            "translated_text": {
                "type": "string",
                "description": "The translated text, with annotations in appropriate places using format [@ft1], [@ft2] etc."
            },
            "annotations": {
                "type": "array",
                "description": "Array of translator annotations to the text, each having an 'id', in format @ft1, @ft2, and 'text', which is the English-language annotation. The 'text' clarifies translation choices and ambiguities in the original language.",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "string",
                            "description": "The unique identifier for the annotation, in the format @ft1, @ft2 etc."
                        },
                        "text": {
                            "type": "string",
                            "description": "The text of the annotation."
                        }
                    }
                }
            }
        }
    }
}]

# example_paragraph_1 = "话说天下大势，分久必合，合久必分。周末七国分争，并入于秦。及秦灭之后，楚、汉分争，又并入于汉。汉朝自高祖斩白蛇而起义，一统天下，后来光武中兴，传至献帝，遂分为三国。"

# example_response_1 = {
#   "translated_text": "The grand trend of the world is that what has been long divided will eventually unite, and what has been long united will eventually divide. The seven states contended towards the end of the Zhou dynasty and were ultimately unified by Qin[@ft1]. After the fall of Qin, Chu and Han fought and were eventually unified by Han[@ft2]. From the time of its founding by Emperor Gao, who rose against a white serpent, the Han dynasty unified China, experienced a revival under Emperor Guangwu, and by the time of Emperor Xian, had divided into the Three Kingdoms[@ft3].",
#   "annotations": [
#     {
#       "id": "@ft1",
#       "text": "Qin dynasty was the first imperial dynasty of China, lasting from 221 to 206 BCE. The unification marked the end of the Warring States period."
#     },
#     {
#       "id": "@ft2",
#       "text": "The Han dynasty followed the Qin and was established in 202 BCE. It lasted until 220 CE and was one of the longest-lasting and most influential dynasties in Chinese history."
#     },
#     {
#       "id": "@ft3",
#       "text": "The Three Kingdoms period was from 220 to 280 CE. It followed the end of the Han dynasty and is famous for its military and strategic complexities."
#     }
#   ]
# }

#%%
# example_response_1_str = json.dumps(example_response_1, ensure_ascii=False)


# Replace 'example_source_text' with the Chinese text you want to translate and annotate
paragraph = "——此开卷第一回也。作者自云：曾历过一番梦幻之后，故将真事隐去，而借 通灵说此《石头记》一书也，故曰“甄士隐”云云。但书中所记何事何人?自己又 云：“今风尘碌碌，一事无成，忽念及当日所有之女子：一一细考较去，觉其行止 见识皆出我之上。我堂堂须眉诚不若彼裙钗，我实愧则有馀，悔又无益，大无可如 何之日也。当此日，欲将已往所赖天恩祖德，锦衣纨之时，饫甘餍肥之日，背父 兄教育之恩，负师友规训之德，以致今日一技无成、半生潦倒之罪，编述一集，以 告天下；知我之负罪固多，然闺阁中历历有人，万不可因我之不肖，自护己短，一 并使其泯灭也。所以蓬牖茅椽，绳床瓦灶，并不足妨我襟怀；况那晨风夕月，阶柳 庭花，更觉得润人笔墨。我虽不学无文，又何妨用假语村言敷演出来?亦可使闺阁 昭传。复可破一时之闷，醒同人之目，不亦宜乎？”故曰“贾雨村”云云。更于篇 中间用“梦”“幻”等字，却是此书本旨，兼寓提醒阅者之意。"

api_response_data = None

#%%
    
    # Call the API
try:
    # Set up the messages list
    messages = [
        {"role": "system", "content": "You are a large language model with vast knowledge of Chinese civilization and culture, trained to translate text and provide careful annotations in the format [@ft1], [@ft2]. Your annotations are incisive and they are intended to clarify ambiguities or deeper meanings in texts. Every translation must include at least one annotation!"},
        # {"role": "user", "content": example_paragraph_1},
        # {"role": "function", "name": "translate_and_annotate", "content": example_response_1_str},
        {"role": "user", "content": paragraph}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        # model="gpt-4",
        messages=messages,
        functions=functions,
        function_call={"name": "translate_and_annotate"},
        temperature=0
    )

    # functions[0]['parameterload
    # Store the full API response data
    
    loadsloadloadsloadloadloaloads

    data_str = response["choices"][0]["message"]["function_call"]["arguments"]
    decoded_data = json.loads(data_str)
    print(decoded_data)
    with open(f"no_example--{response['model']}--{response['created']}.json", 'w') as f:
        json.dump(api_response_data, f, indent=4)
except Exception as e:
    print(f"Exception: {e}")

# The 'decoded_data' object should contain the translated and annotated text

# %%
