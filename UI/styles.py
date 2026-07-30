import streamlit as st


def load_css():
    st.markdown("""
<style>

/* ============================================================
   GOOGLE FONT
============================================================ */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]{
    font-family: 'Inter', sans-serif;
}


/* ============================================================
   MAIN APP
============================================================ */

.stApp{

    background:
    radial-gradient(circle at top right,#12363b 0%,transparent 40%),
    radial-gradient(circle at bottom left,#0b2024 0%,transparent 35%),
    #07171A;

    color:white;

}


/* remove streamlit header */

header{
    visibility:hidden;
}

footer{
    visibility:hidden;
}


/* ============================================================
   SIDEBAR
============================================================ */

[data-testid="stSidebar"]{

    background:rgba(13,32,37,.90);

    border-right:1px solid rgba(255,255,255,.05);

    backdrop-filter: blur(25px);

    box-shadow:8px 0px 30px rgba(0,0,0,.35);

}


[data-testid="stSidebar"] *{

    color:white;

}


/* sidebar title */

.sidebar-title{

    font-size:28px;

    font-weight:700;

    margin-bottom:6px;

}


.sidebar-subtitle{

    color:#7dbfc3;

    font-size:14px;

    margin-bottom:25px;

}


/* ============================================================
   FILE UPLOADER
============================================================ */

[data-testid="stFileUploader"]{

    background:#10282d;

    border:2px dashed #22D3C5;

    border-radius:20px;

    padding:18px;

    transition:.35s;

}

[data-testid="stFileUploader"]:hover{

    border-color:#65fff3;

    box-shadow:0 0 18px rgba(34,211,197,.35);

}


/* ============================================================
   BUTTONS
============================================================ */

.stButton>button{

    width:100%;

    border:none;

    border-radius:14px;

    padding:.7rem;

    color:white;

    font-weight:600;

    background:linear-gradient(135deg,#11c5bb,#0d7b88);

    transition:.3s;

}

.stButton>button:hover{

    transform:translateY(-3px);

    box-shadow:0 10px 25px rgba(34,211,197,.25);

}


/* ============================================================
   TEXT INPUT
============================================================ */

.stTextInput>div>div>input{

    background:#11282d;

    border:1px solid rgba(255,255,255,.05);

    border-radius:14px;

    color:white;

    padding:14px;

}

.stTextInput>div>div>input:focus{

    border:1px solid #22d3c5;

    box-shadow:0 0 10px rgba(34,211,197,.25);

}


/* ============================================================
   SELECTBOX
============================================================ */

.stSelectbox>div>div{

    background:#11282d;

    border-radius:14px;

}


/* ============================================================
   METRIC CARDS
============================================================ */

[data-testid="metric-container"]{

    background:linear-gradient(180deg,#10292f,#0b1f23);

    border-radius:20px;

    padding:20px;

    border:1px solid rgba(255,255,255,.05);

    box-shadow:0 10px 35px rgba(0,0,0,.20);

    transition:.3s;

}

[data-testid="metric-container"]:hover{

    transform:translateY(-5px);

    border:1px solid #22d3c5;

}


/* metric label */

[data-testid="metric-container"] label{

    color:#8bbdc1;

}


/* metric number */

[data-testid="metric-container"] [data-testid="stMetricValue"]{

    color:white;

    font-size:34px;

    font-weight:700;

}


/* ============================================================
   CARDS
============================================================ */

.custom-card{

    background:rgba(16,41,47,.92);

    border-radius:22px;

    padding:22px;

    border:1px solid rgba(255,255,255,.05);

    box-shadow:0px 15px 35px rgba(0,0,0,.25);

}


/* ============================================================
   DOCUMENT CARD
============================================================ */

.doc-card{

    background:#10282d;

    border-radius:18px;

    padding:16px;

    margin-bottom:12px;

    border-left:5px solid #22d3c5;

    transition:.3s;

}

.doc-card:hover{

    transform:translateX(5px);

    background:#123038;

}


/* ============================================================
   TITLES
============================================================ */

h1{

    font-weight:700;

    color:white;

}

h2{

    color:white;

}

h3{

    color:white;

}

h4{

    color:#d7f5f3;

}


/* ============================================================
   CAPTION
============================================================ */

.stCaption{

    color:#87b6ba;

}


/* ============================================================
   HORIZONTAL LINE
============================================================ */

hr{

    border-color:rgba(255,255,255,.08);

}


/* ============================================================
   SCROLLBAR
============================================================ */

::-webkit-scrollbar{

    width:10px;

}

::-webkit-scrollbar-track{

    background:#09171b;

}

::-webkit-scrollbar-thumb{

    background:#1aa99c;

    border-radius:10px;

}

::-webkit-scrollbar-thumb:hover{

    background:#3fe5d8;

}


/* ============================================================
   SPINNER
============================================================ */

.stSpinner>div{

    border-top-color:#22d3c5;

}


/* ============================================================
   LINKS
============================================================ */

a{

    color:#22d3c5;

    text-decoration:none;

}

a:hover{

    color:#67fff2;

}


/* ============================================================
   DIVIDERS
============================================================ */

[data-testid="stDivider"]{

    border-color:rgba(255,255,255,.05);

}

/* ============================================================
   TABS
============================================================ */

.stTabs [data-baseweb="tab-list"]{
    gap:14px;
    background:transparent;
    margin-bottom:20px;
}

.stTabs [data-baseweb="tab"]{
    background:#10282d;
    border-radius:14px;
    color:#A9C7CB;
    padding:10px 24px;
    border:1px solid rgba(255,255,255,.04);
    transition:.3s;
    font-weight:600;
}

.stTabs [data-baseweb="tab"]:hover{
    background:#14363d;
    color:white;
}

.stTabs [aria-selected="true"]{
    background:linear-gradient(135deg,#18C8BC,#0F8A94) !important;
    color:white !important;
    box-shadow:0 8px 20px rgba(24,200,188,.25);
}

.stTabs [data-baseweb="tab-highlight"]{
    display:none;
}


/* ============================================================
   DATAFRAME
============================================================ */

[data-testid="stDataFrame"]{

    border-radius:18px;

    overflow:hidden;

    border:1px solid rgba(255,255,255,.05);

    background:#10282d;

    box-shadow:0 15px 35px rgba(0,0,0,.25);

}


/* ============================================================
   EXPANDERS
============================================================ */

.streamlit-expanderHeader{

    background:#10282d;

    border-radius:14px;

    color:white;

    font-weight:600;

    padding:12px;

}

.streamlit-expanderContent{

    background:#0D2227;

    border-radius:0 0 14px 14px;

}


/* ============================================================
   ALERTS
============================================================ */

.stSuccess{

    background:rgba(16,185,129,.15);

    border-left:5px solid #10B981;

    border-radius:14px;

}

.stInfo{

    background:rgba(59,130,246,.12);

    border-left:5px solid #3B82F6;

    border-radius:14px;

}

.stWarning{

    background:rgba(245,158,11,.15);

    border-left:5px solid #F59E0B;

    border-radius:14px;

}

.stError{

    background:rgba(239,68,68,.12);

    border-left:5px solid #EF4444;

    border-radius:14px;

}


/* ============================================================
   CHAT / ANSWER CARD
============================================================ */

.answer-card{

    background:linear-gradient(180deg,#123037,#10262C);

    border-radius:22px;

    padding:24px;

    border:1px solid rgba(34,211,197,.25);

    box-shadow:0 20px 40px rgba(0,0,0,.25);

    margin-top:15px;

    margin-bottom:15px;

}

.answer-title{

    color:#22D3C5;

    font-size:18px;

    font-weight:700;

    margin-bottom:10px;

}


/* ============================================================
   SECTION TITLES
============================================================ */

.section-title{

    font-size:24px;

    font-weight:700;

    color:white;

    margin-top:10px;

    margin-bottom:20px;

}

.section-subtitle{

    color:#8DB7BB;

    font-size:14px;

    margin-bottom:25px;

}


/* ============================================================
   SIDEBAR DOCUMENT LIST
============================================================ */

.document-item{

    background:#11282D;

    border-radius:16px;

    padding:14px;

    margin-bottom:12px;

    transition:.3s;

    border:1px solid rgba(255,255,255,.04);

}

.document-item:hover{

    border:1px solid #22D3C5;

    transform:translateX(4px);

}


/* ============================================================
   DELETE BUTTON
============================================================ */

button[kind="secondary"]{

    border-radius:12px !important;

}

button[kind="secondary"]:hover{

    background:#E63946 !important;

    color:white !important;

}


/* ============================================================
   LINE CHART CONTAINER
============================================================ */

.element-container:has(canvas){

    background:#10282D;

    border-radius:18px;

    padding:18px;

    margin-top:10px;

    margin-bottom:20px;

    border:1px solid rgba(255,255,255,.04);

}


/* ============================================================
   HOVER ANIMATIONS
============================================================ */

.stButton>button,
[data-testid="metric-container"],
.document-item,
.doc-card,
.answer-card{

    transition:all .3s ease;

}

.answer-card:hover{

    transform:translateY(-4px);

    box-shadow:0 20px 45px rgba(34,211,197,.18);

}


/* ============================================================
   GLASS EFFECT
============================================================ */

.glass{

    background:rgba(255,255,255,.04);

    backdrop-filter:blur(18px);

    border:1px solid rgba(255,255,255,.06);

    border-radius:20px;

}


/* ============================================================
   FADE ANIMATION
============================================================ */

@keyframes fadeIn{

from{

opacity:0;

transform:translateY(10px);

}

to{

opacity:1;

transform:translateY(0);

}

}

.stMarkdown,
.stDataFrame,
[data-testid="metric-container"]{

animation:fadeIn .5s ease;

}


/* ============================================================
   RESPONSIVE
============================================================ */

@media (max-width:900px){

h1{

font-size:32px;

}

.stTabs [data-baseweb="tab"]{

padding:8px 12px;

font-size:13px;

}

[data-testid="metric-container"]{

padding:15px;

}

}


/* ============================================================
   NICE SELECTION COLOR
============================================================ */

::selection{

background:#22D3C5;

color:#07171A;

}
</style>
""", unsafe_allow_html=True)