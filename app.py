import streamlit as st

from agents.planner_agent import planner_agent
from agents.research_agent import research_agent
from agents.medical_agent import medical_agent
from agents.interaction_agent import interaction_agent
from agents.regulatory_agent import regulatory_agent
from agents.report_agent import report_agent
from agents.pdf_export import export_pdf

# UI Streamlit Configuration
st.set_page_config(
    page_title="Pharma Multi-Agent System",
    layout="wide"
)

st.title("💊 Pharma Multi-Agent System")

st.caption(
    "Planner • Research • Medical • Interaction • Regulatory • Report"
)

query = st.text_area(
    "Enter Pharmaceutical Query",
    height=150,
    placeholder="Example: Compare Metformin and Ozempic for Type 2 Diabetes"
)

if st.button("Analyze"):

    if not query.strip():

        st.warning("Please enter a query.")

    else:

        with st.spinner("Planner Agent Running..."):
            plan = planner_agent(query)

        with st.spinner("Research Agent Running..."):
            research = research_agent(query)

        with st.spinner("Medical Agent Running..."):
            medical = medical_agent(query)

        with st.spinner("Interaction Agent Running..."):
            interaction = interaction_agent(query)

        with st.spinner("Regulatory Agent Running..."):
            regulatory = regulatory_agent(query)

        with st.spinner("Generating Final Report..."):
            report = report_agent(
                query,
                plan,
                research,
                medical,
                interaction,
                regulatory
            )

        st.success("Analysis Complete")

        with st.expander("📋 Planner Agent"):
            st.write(plan)

        with st.expander("🔬 Research Agent"):
            st.write(research)

        with st.expander("🩺 Medical Agent"):
            st.write(medical)

        with st.expander("⚠️ Interaction Agent"):
            st.write(interaction)

        with st.expander("📜 Regulatory Agent"):
            st.write(regulatory)

        st.subheader("📄 Final Report")

        st.markdown(report)

        pdf_path = export_pdf(report)

        with open(pdf_path, "rb") as file:

            st.download_button(
                label="📥 Download PDF Report",
                data=file,
                file_name="pharma_report.pdf",
                mime="application/pdf"
            )
            