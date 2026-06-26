from llm import llm

from tools.web_search import search_web
from tools.pubmed_tool import search_pubmed


def research_agent(query):

    web_results = search_web(query)

    pubmed_results = search_pubmed(query)

    prompt = f"""
    You are a Pharmaceutical Research Agent.

    Analyze information from:

    WEB SEARCH:
    {web_results}

    PUBMED:
    {pubmed_results}

    Generate:

    - Research Summary
    - Latest Findings
    - Key Evidence
    - Important References

    Keep the answer concise.
    """

    response = llm.invoke(prompt)

    return response.content