from llm import llm


def medical_agent(query):

    prompt = f"""
    You are a Medical Specialist Agent.

    Analyze:

    {query}

    Include:

    - Disease Overview
    - Symptoms
    - Causes
    - Diagnosis
    - Treatment Options
    - Drug Classes
    - Mechanism of Action

    Provide a professional medical analysis.
    """

    response = llm.invoke(prompt)

    return response.content