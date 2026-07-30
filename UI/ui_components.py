"""
ui_components.py
----------------
Reusable UI components for the RAG Assistant.
"""
import base64
import streamlit as st


# =====================================================
# PAGE HEADER
# =====================================================

import base64

def page_header():

    with open("assets/icon.png", "rb") as img:
        logo = base64.b64encode(img.read()).decode()

    st.markdown(
        f"""
<div style="
display:flex;
align-items:flex-start;
gap:25px;
margin-bottom:25px;
">

<img src="data:image/png;base64,{logo}"
     style="
     width:120px;
     height:120px;
     margin-top:6px;
">

<div>

<h1 style="
margin:0;
font-size:42px;
font-weight:700;
color:white;
line-height:1.2;
">
RAG Assistant
</h1>

<p style="
margin-top:-5px;
color:#90B6BB;
font-size:17px;
">
Real-Time Source Control & Performance Benchmarking
</p>

</div>

</div>
""",
        unsafe_allow_html=True,
    )
# =====================================================
# SIDEBAR HEADER
# =====================================================

def sidebar_header():

    st.markdown("""
    <div class="sidebar-title">
        📁 Data Source Manager
    </div>

    <div class="sidebar-subtitle">
        Upload documents and manage your knowledge base
    </div>
    """, unsafe_allow_html=True)


# =====================================================
# SECTION TITLE
# =====================================================

def section_title(title, subtitle=""):

    st.markdown(f"""
    <div class="section-title">
        {title}
    </div>

    <div class="section-subtitle">
        {subtitle}
    </div>
    """, unsafe_allow_html=True)


# =====================================================
# DOCUMENT CARD
# =====================================================

def document_card(filename, chunks):

    st.markdown(f"""
    <div class="document-item">

<b style="font-size:16px;">📄 {filename}</b>

<br>

<span style="color:#90B7BC;">
🧩 {chunks} chunks indexed
</span>

</div>
    """, unsafe_allow_html=True)


# =====================================================
# METRIC CARD
# =====================================================

def metric_card(title, value):

    st.markdown(f"""
    <div class="custom-card">

<div style="
font-size:14px;
color:#8DB7BB;
margin-bottom:8px;
">

{title}

</div>

<div style="
font-size:34px;
font-weight:700;
color:white;
">

{value}

</div>

</div>
    """, unsafe_allow_html=True)


# =====================================================
# ANSWER CARD
# =====================================================

def answer_card(answer):

    st.markdown(f"""
    <div class="answer-card">

<div class="answer-title">
🤖 Answer
</div>

<div style="
font-size:16px;
line-height:1.8;
color:white;
">

{answer}

</div>

</div>
    """, unsafe_allow_html=True)


# =====================================================
# INFO CARD
# =====================================================

def info_card(text):

    st.markdown(f"""
    <div class="glass"
    style="padding:18px;margin-bottom:15px;">

{text}

</div>
    """, unsafe_allow_html=True)


# =====================================================
# EMPTY STATE
# =====================================================

def empty_documents():

    st.markdown("""
<div class="glass"
style="
padding:40px;
text-align:center;
">

<div style="
font-size:50px;
margin-bottom:15px;
">

📂

</div>

<div style="
font-size:22px;
font-weight:600;
margin-bottom:10px;
">

No Documents Uploaded

</div>

<div style="
color:#89B5B9;
">

Upload your first PDF, TXT, or DOCX file
to begin building your knowledge base.

</div>

</div>
    """, unsafe_allow_html=True)


# =====================================================
# SUCCESS CARD
# =====================================================

def success_card(message):

    st.markdown(f"""
<div style="
background:#0F312F;
border-left:5px solid #22D3C5;
padding:16px;
border-radius:14px;
margin-bottom:12px;
">

✅ {message}

</div>
    """, unsafe_allow_html=True)


# =====================================================
# WARNING CARD
# =====================================================

def warning_card(message):

    st.markdown(f"""
<div style="
background:#342818;
border-left:5px solid orange;
padding:16px;
border-radius:14px;
margin-bottom:12px;
">

⚠️ {message}

</div>
    """, unsafe_allow_html=True)


# =====================================================
# DELETE BUTTON
# =====================================================

def delete_button(key):

    return st.button(
        "🗑️",
        key=key,
        use_container_width=True
    )


# =====================================================
# DASHBOARD HEADER
# =====================================================

def dashboard_header(title):

    st.markdown(f"""
<h2 style="
margin-bottom:25px;
color:white;
">

📊 {title}

</h2>
    """, unsafe_allow_html=True)


# =====================================================
# CHAT HEADER
# =====================================================

def chat_header():

    st.markdown("""
<h2 style="
color:white;
margin-bottom:20px;
">

💬 Ask Questions

</h2>
    """, unsafe_allow_html=True)


# =====================================================
# HISTORY HEADER
# =====================================================

def history_header():

    st.markdown("""
<h2 style="
color:white;
margin-bottom:20px;
">

🕘 Query History

</h2>
    """, unsafe_allow_html=True)


# =====================================================
# DOCUMENT HEADER
# =====================================================

def document_header():

    st.markdown("""
<h2 style="
color:white;
margin-bottom:20px;
">

📄 Knowledge Base

</h2>
    """, unsafe_allow_html=True)