from duckduckgo_search import DDGS


def search_web(query: str):

    results = []

    try:
        with DDGS() as ddgs:

            search_results = ddgs.text(
                query,
                max_results=5
            )

            for item in search_results:

                body = item.get("body", "")

                if body:
                    results.append(body)

        return "\n".join(results)

    except Exception as e:

        return f"Search Error: {str(e)}"