import streamlit as st
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))


from src.rag_chain import generate_test_plan, debug_code

st.set_page_config(
    page_title="AI TestPilot",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 AI TestPilot")
st.caption(
    "AI-Powered Test Plan Generator & Debug Assistant"
)

# matric cards

col1, col2, col3, col4 =  st.columns(4)

with col1:
    st.metric("Document", "2")

with col2:
    st.metric("Chunks", "2")

with col3:
    st.metric("Model", "Llama 3.3")

with col4:
    st.metric("Vector DB", "FAISS")


#Tabs
tab1, tab2 = st.tabs(
    ["🧪 Test Plan Generator", "🐞 Debug Assistant"]
)

with tab1:
    left, right = st.columns([1,2])

    with left:
        
        requirement = st.text_area(

            "Requirement",
            height = 250,
            placeholder="Paste softwere requirement..."
        )

        generate_btn = st.button(
            "Generate Test Plan"
        )
    
    with right:
        if generate_btn and requirement:

            with st.spinner(
                "Generating test plan..."
            ):
                result = generate_test_plan(
                    requirement
                )
            
            st.success("Genrated Successfully")

            st.markdown(result)
            st.download_button(
                "📥 Download Report",
                result,
                file_name="test_plan.txt"
            )

with tab2:

    left, right = st.columns([1, 2])

    with left:

        error = st.text_area(
            "Error Message",
            height=150
        )

        code = st.text_area(
            "Code",
            height=250
        )

        analyze_btn = st.button(
            "Analyze Error"
        )

    with right:

        if analyze_btn and error and code:

            with st.spinner(
                "Analyzing..."
            ):
                result = debug_code(
                    error,
                    code
                )

            st.success(
                "Analysis Completed"
            )

            st.markdown(result)

            st.download_button(
                "📥 Download Analysis",
                result,
                file_name="debug_report.txt"
            )