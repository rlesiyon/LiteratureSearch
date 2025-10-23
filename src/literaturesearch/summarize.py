# !pip install -qU langchain langchain-openai langchain-tavily
import fire
from ollama import chat
from ollama import ChatResponse
from search_pmid import search_pubmed_by_term
def summarize_article(abstract):
    '''
    Summarize the article abstract using gemma3:1b model
    '''
    response: ChatResponse = chat(
        model='gemma3:1b', 
        messages=[
            {
                'role': 'user',
                'content': f"Summarize the title below \n {abstract}. Make it succinct. One sentence",
            },
        ]
    ) 
    return response.message.content

def rank_article_as_per_topic(abstract, topic): 
    '''
    Rank the abstract between 1 to 5 based on the its relevant to the topic
    '''
    response: ChatResponse = chat(
        model='gemma3:1b', 
        messages=[
            {
                'role': 'user',
                'content': f"Rank the abstract {abstract} from 1 to 5 based on relevance to {topic}",
            },
        ]
    ) 
    return response.message.content 

def main(topic):
   result = search_pubmed_by_term(topic)
   response = summarize_article(result[0]['abstract'])
   print(response)

if __name__ == "__main__":
    fire.Fire(main)
