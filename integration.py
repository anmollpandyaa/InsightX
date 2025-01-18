from langflow import LangFlow
import json

def generate_insights(keyword):
    langflow = LangFlow()
    
    insights = langflow.get_insights(keyword) 
    
    return {
        "keyword": keyword,
        "insights": insights
    }

if __name__ == "__main__":
    keyword = "cloud computing"
    result = generate_insights(keyword)
    print(json.dumps(result))
