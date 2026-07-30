import pandas as pd
import streamlit as st

from config import TOP_K

from datasource_manager import (
    add_file,
    delete_file,
    active_documents,
)

from retriever import retrieve
from llm_generator import generate_answer

from Knowledge_base import (
    save_qa,
    get_history,
)

from performance_monitor import (
    log_query,
    get_logs,
    summary,
)

# NEW
from UI.styles import load_css

# NEW
from UI.ui_components import (
    page_header,
    sidebar_header,
    section_title,
    document_card,
    answer_card,
    empty_documents,
)

# PAGE CONFIG
st.set_page_config(
    page_title="RAG Assistant",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)


load_css()

#header
page_header()

st.caption(
    "ChromaDB • HuggingFace Embeddings • Groq • Streamlit"
)

st.markdown("<br>", unsafe_allow_html=True)


#sidebar
with st.sidebar:

    sidebar_header()

    uploaded_files = st.file_uploader(
        "Upload PDF / TXT / DOCX",
        type=["pdf", "txt", "docx"],
        accept_multiple_files=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    if uploaded_files:

        if st.button(
            "Add to Knowledge Base",
            use_container_width=True,
        ):

            with st.spinner("Indexing documents..."):

                for file in uploaded_files:

                    result = add_file(file)

                    st.success(
                        f"Added {result['file']}"
                    )

    st.markdown("---")
    st.markdown("### 📂 Active Documents")

    with st.container(key="active_docs_box"):
        docs = active_documents()
        if docs:
          for name, chunks in docs.items():
            c1, c2 = st.columns([5,1])
            with c1:
                document_card(name, chunks)
            with c2:
                st.write("")
                st.write("")
                if st.button(
                    "🗑️",
                    key=f"delete_{name}",
                    use_container_width=True,
                ):
                    delete_file(name)
                    st.rerun()
        else:
           empty_documents()

#main tabs
tab_chat, tab_docs, tab_dashboard, tab_history = st.tabs(

    [

        "💬 Chat",

        "📄 Documents",

        "📊 Dashboard",

        "🕘 History",

    ]

)


#chat tab
with tab_chat:

    section_title(
        "💬 Chat with your Knowledge Base",
        "Search, retrieve, and explore information from your uploaded document!"
    )

    query = st.text_input(
        "",
        placeholder="Ask anything..."
    )

    st.markdown("<br>", unsafe_allow_html=True)

    ask = st.button(
        "Get Answer",
        use_container_width=True
    )

    if ask and query:

        active_count = len(active_documents())

        with st.spinner("Searching relevant documents..."):

            chunks, retrieval_time = retrieve(
                query,
                top_k=TOP_K
            )

        with st.spinner("Generating answer..."):

            answer, generation_time = generate_answer(
                query,
                chunks
            )

        save_qa(query, answer)

        metrics = log_query(
            query,
            answer,
            chunks,
            retrieval_time,
            generation_time,
            active_count,
        )

        st.markdown("<br>", unsafe_allow_html=True)

        answer_card(answer)

        st.markdown("<br>", unsafe_allow_html=True)

 # METRICS
        c1, c2, c3, c4 = st.columns(4)

        with c1:

            st.metric(
                "⚡ Retrieval",
                f"{retrieval_time:.2f}s"
            )

        with c2:

            st.metric(
                "🤖 Generation",
                f"{generation_time:.2f}s"
            )

        with c3:

            st.metric(
                "🎯 Retrieval Score",
                f"{metrics['avg_retrieval_score']:.3f}"
            )

        with c4:

            st.metric(
                "✅ Faithfulness",
                f"{metrics['faithfulness_score']:.2f}"
            )

        st.markdown("<br>", unsafe_allow_html=True)

       
# DOCUMENTS TAB
with tab_docs:

    section_title(
        "📄 Knowledge Base",
        "Overview of indexed documents."
    )

    docs = active_documents()

    if docs:

        df = pd.DataFrame(

            [

                {

                    "📄 Document": name,

                    "🧩 Indexed Chunks": chunks,

                }

                for name, chunks in docs.items()

            ]

        )

        st.dataframe(

            df,

            use_container_width=True,

            hide_index=True,

        )

        st.markdown("<br>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:

            st.metric(

                "📄 Documents",

                len(docs)

            )

        with col2:

            st.metric(

                "🧩 Total Chunks",

                sum(docs.values())

            )

    else:

        empty_documents()


# PERFORMANCE DASHBOARD
with tab_dashboard:

    section_title(
        "📊 Performance Dashboard",
        "Monitor retrieval quality and model performance."
    )

    stats = summary()

    if stats:

        c1, c2, c3, c4, c5 = st.columns(5)

        with c1:
            st.metric(
                "📝 Queries",
                stats["total_queries"]
            )

        with c2:
            st.metric(
                "⚡ Avg Latency",
                f"{stats['avg_total_latency']} s"
            )

        with c3:
            st.metric(
                "🔍 Avg Retrieval",
                f"{stats['avg_retrieval_time']} s"
            )

        with c4:
            st.metric(
                "🤖 Avg Generation",
                f"{stats['avg_generation_time']} s"
            )

        with c5:
            st.metric(
                "✅ Faithfulness",
                stats["avg_faithfulness"]
            )

        st.markdown("<br>", unsafe_allow_html=True)

        logs = get_logs(limit=200)

        if not logs.empty:

            logs = logs.sort_values("id")

          
# LATENCY CHART

            st.markdown("### ⚡ Latency Analysis")

            latency = logs.set_index("timestamp")[
                [
                    "retrieval_time",
                    "generation_time",
                    "total_latency",
                ]
            ]

            st.line_chart(
                latency,
                use_container_width=True
            )

            st.markdown("<br>", unsafe_allow_html=True)

# RETRIEVAL SCORE

            st.markdown("### 🎯 Retrieval Quality")

            retrieval = logs.set_index("timestamp")[
                [
                    "avg_retrieval_score",
                    "faithfulness_score",
                ]
            ]

            st.line_chart(
                retrieval,
                use_container_width=True
            )

            st.markdown("<br>", unsafe_allow_html=True)

           
# KNOWLEDGE BASE IMPACT
            
            st.markdown(
                "### 📈 Knowledge Base Growth Impact"
            )

            grouped = (
                logs.groupby(
                    "active_doc_count"
                )[
                    [
                        "retrieval_time",
                        "avg_retrieval_score",
                        "faithfulness_score",
                    ]
                ]
                .mean()
                .reset_index()
            )

            st.dataframe(
                grouped,
                use_container_width=True,
                hide_index=True,
            )

            st.markdown("<br>", unsafe_allow_html=True)

 # RAW LOGS           
            with st.expander(
                "📋 View Raw Performance Logs"
            ):

                st.dataframe(
                    logs,
                    use_container_width=True,
                    hide_index=True,
                )

    else:

        st.info(
            "Run a few queries to populate the dashboard."
        )

# QUERY HISTORY
with tab_history:

    section_title(
        "🕘 Query History",
        "Previously asked questions and generated answers."
    )

    history = get_history(limit=100)

    if not history.empty:

        st.dataframe(
            history,
            use_container_width=True,
            hide_index=True,
        )

        st.markdown("<br>", unsafe_allow_html=True)

        st.success(
            f"{len(history)} conversation(s) stored."
        )

    else:

        st.info(
            "No conversations found yet."
        )

# FOOTER
st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(
    """
<hr style="border:1px solid rgba(255,255,255,.08);">

<div style="text-align:center;color:#8FB6BB;font-size:14px;padding-bottom:20px;">

Built using
<b>Streamlit</b>,
<b>ChromaDB</b>,
<b>LangChain</b>,
<b>HuggingFace Embeddings</b>,
and <b>Groq LLM</b>

</div>
""",
    unsafe_allow_html=True,
)