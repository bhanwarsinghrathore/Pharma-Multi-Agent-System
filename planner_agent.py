from llm import llm


def planner_agent(query):

    prompt = f"""
    You are an expert Pharmaceutical Planning Agent.

    User Query:
    {query}

    Break the task into clear steps.

    Include:

    1. Research Requirements
    2. Medical Analysis
    3. Drug Interaction Analysis
    4. Regulatory Review
    5. Final Recommendation

    Return structured bullet points.
    """

    response = llm.invoke(prompt)

    return response.content
