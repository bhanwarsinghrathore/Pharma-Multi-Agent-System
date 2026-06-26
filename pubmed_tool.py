from pymed import PubMed

pubmed = PubMed(
    tool="PharmaMultiAgent",
    email="your_email@example.com"
)


def search_pubmed(query: str):

    try:

        articles = pubmed.query(
            query,
            max_results=5
        )

        summaries = []

        for article in articles:

            title = article.title

            abstract = article.abstract

            summaries.append(
                f"Title: {title}\nAbstract: {abstract}"
            )

        return "\n\n".join(summaries)

    except Exception as e:

        return f"PubMed Error: {str(e)}"