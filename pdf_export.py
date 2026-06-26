import os

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def export_pdf(report_text):

    os.makedirs(
        "outputs/reports",
        exist_ok=True
    )

    filename = "outputs/reports/pharma_report.pdf"

    pdf = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    for line in report_text.split("\n"):

        if line.strip():

            story.append(
                Paragraph(
                    line,
                    styles["BodyText"]
                )
            )

            story.append(
                Spacer(1, 6)
            )

    pdf.build(story)

    return filename