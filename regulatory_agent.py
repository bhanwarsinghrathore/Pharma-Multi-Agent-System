from llm import llm


def regulatory_agent(query):

    prompt = f"""
    You are a Pharmaceutical Regulatory Expert.

    Analyze:

    {query}

    Include:

    - FDA Considerations
    - EMA Considerations
    - Approval Status
    - Regulatory Risks
    - Safety Compliance

    Return concise professional analysis.
    """

    response = llm.invoke(prompt)

    return response.content