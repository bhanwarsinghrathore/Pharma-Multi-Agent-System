from llm import llm


def report_agent(
    query,
    plan,
    research,
    medical,
    interaction,
    regulatory
):

    prompt = f"""
    Create a final professional pharmaceutical report.

    USER QUERY:
    {query}

    PLANNER:
    {plan}

    RESEARCH:
    {research}

    MEDICAL:
    {medical}

    INTERACTION:
    {interaction}

    REGULATORY:
    {regulatory}

    Format:

    # Executive Summary

    # Research Findings

    # Medical Analysis

    # Drug Interactions

    # Regulatory Review

    # Recommendations

    # Conclusion
    """

    response = llm.invoke(prompt)

    return response.content