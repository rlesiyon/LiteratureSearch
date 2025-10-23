
# Function to search PMID using metapub given a particular term
from metapub import PubMedFetcher
import fire

def search_pubmed_by_term(topic, retmax = 10):
    '''
    Search PubMed for a given topic and retrieve article information.
    Args:
        topic (str): The search term or topic to query in PubMed.
        retmax (int, optional): Maximum number of article results to fetch. Defaults to 10.

    Returns:
        list[dict]: A list of dictionaries, where each dictionary contains
                    the PMID, title, and abstract of an article.
    '''
    fetch = PubMedFetcher() 
    pmids = fetch.pmids_for_query(topic, retmax=retmax)
    fetched_articles = [ fetch_article(pmid) for pmid in pmids]
    return fetched_articles 

def fetch_article(pmid):
    '''
    Fetch detailed information for a specific PubMed article using its PMID.

    Args:
        pmid (str): The PubMed ID of the article.

    Returns:
        dict: A dictionary containing:
            - "pmid": The article’s PubMed ID.
            - "title": The article’s title.
            - "abstract": The article’s abstract text.
    '''
    fetch = PubMedFetcher()
    article = fetch.article_by_pmid(pmid)

    article_dic = {
        "pmid" : pmid, 
        "title" : article.title, 
        "abstract" : article.abstract
    }
    return article_dic 

def main(topic):
    """
    Command-line entry point for searching PubMed.

    Args:
        topic (str): The topic or keyword to search in PubMed.
    Side Effects:
        Prints the list of fetched articles to the console.
    """
    result = search_pubmed_by_term(topic)
    print(result)


if __name__ == "__main__":
    fire.Fire(main)

