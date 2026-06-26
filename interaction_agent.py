from llm import llm


def interaction_agent(query):

    prompt = f"""
    You are a Drug Interaction Specialist.

    Analyze:

    {query}

    Provide:

    - Possible Drug Interactions
    - Contraindications
    - Adverse Effects
    - Safety Warnings
    - Monitoring Recommendations

    Return a structured report.
    """

    response = llm.invoke(prompt)

    return response.content