import streamlit as st
import requests
import pandas as pd
import time
import random
from datetime import datetime

API_URL = 'http://localhost:5000'

# Set page title and configuration
st.set_page_config(
    page_title="SQL Murder Mystery",
    page_icon="🔍",
    layout="wide"
)

# Set up detective theme and styling with noir theme
st.markdown("""
<style>
    /* Main background and text */
    body {
        font-family: 'Georgia', serif;
    }
    
    .stApp {
        background-color: #141414;
        color: #E0E0E0;
        background-image: linear-gradient(rgba(0, 0, 0, 0.85), rgba(0, 0, 0, 0.85)), 
                          url("https://images.unsplash.com/photo-1588345921523-c2dcdb7f1dcd?ixlib=rb-1.2.1&auto=format&fit=crop&q=80");
        background-size: cover;
        background-attachment: fixed;
    }
    
    /* Headers styling */
    h1, h2, h3 {
        color: #FF3B3B;
        font-family: 'Georgia', serif;
        text-shadow: 2px 2px 4px #000000;
    }
    
    /* Custom button styling */
    .stButton>button {
        background-color: #AA0000;
        color: white;
        border: 2px solid #FF3B3B;
        border-radius: 5px;
        padding: 8px 15px;
        font-weight: bold;
        transition: all 0.3s;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
    }
    
    .stButton>button:hover {
        background-color: #FF3B3B;
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.5);
    }
    
    /* Text input and text area */
    .stTextInput input, .stTextArea textarea {
        background-color: #2D2D2D;
        color: #E0E0E0;
        border: 1px solid #FF3B3B;
        border-radius: 5px;
    }
    
    /* Main container styling */
    .main-container {
        background-color: rgba(20, 20, 20, 0.8);
        border: 3px solid #AA0000;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 0 20px rgba(170, 0, 0, 0.5);
        margin-bottom: 20px;
    }
    
    /* Section container styling */
    .section-container {
        background-color: rgba(30, 30, 30, 0.9);
        border-left: 5px solid #FF3B3B;
        padding: 15px;
        margin: 15px 0;
        border-radius: 0 10px 10px 0;
    }
    
    /* Evidence card styling */
    .evidence-card {
        background-color: #2D2D2D;
        border: 1px solid #555;
        border-radius: 5px;
        padding: 10px;
        margin: 10px 0;
    }
    
    /* Dataframe styling */
    .dataframe {
        background-color: rgba(45, 45, 45, 0.9);
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background-color: #2D2D2D;
        color: #E0E0E0;
        border-radius: 5px;
    }
    
    /* Progress bar */
    .stProgress > div > div {
        background-color: #FF3B3B;
    }
    
    /* Win animation container */
    @keyframes pulse {
        0% { box-shadow: 0 0 10px #FF3B3B; }
        50% { box-shadow: 0 0 20px #FF3B3B, 0 0 40px #FF3B3B; }
        100% { box-shadow: 0 0 10px #FF3B3B; }
    }
    
    .win-container {
        animation: pulse 2s infinite;
        background-color: rgba(0, 0, 0, 0.8);
        border: 3px solid #FF3B3B;
        border-radius: 10px;
        padding: 30px;
        text-align: center;
        margin: 20px 0;
    }
    
    .win-container h1 {
        color: #FF3B3B;
        font-size: 3rem;
    }
    
    /* Badge styling */
    .detective-badge {
        background-color: #AA0000;
        color: white;
        padding: 5px 10px;
        border-radius: 20px;
        font-weight: bold;
        margin-right: 5px;
        display: inline-block;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state variables
if 'case_notes' not in st.session_state:
    st.session_state.case_notes = ""
if 'current_query' not in st.session_state:
    st.session_state.current_query = ""
if 'start_time' not in st.session_state:
    st.session_state.start_time = time.time()
if 'discovered_clues' not in st.session_state:
    st.session_state.discovered_clues = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
if 'wrong_guesses' not in st.session_state:
    st.session_state.wrong_guesses = 0

# Funny game over messages
game_over_messages = [
    "Your detective skills are more mysterious than the murder itself!",
    "Holmes would be rolling in his fictional grave right now...",
    "Maybe you should stick to finding your lost car keys instead?",
    "The only case you're solving today is the case of the mistaken detective!",
    "Even the victim would be disappointed in your investigation...",
    "Your detective badge just turned into a participation trophy!",
    "The murderer is still out there, laughing at your deduction skills!",
    "Your detective career is now as dead as the victim!",
    "Did you learn your detective skills from watching cartoons?",
    "The real mystery is how you became a detective in the first place!"
]

# Top header with title and timer
st.markdown('<div class="main-container">', unsafe_allow_html=True)
col_title, col_timer = st.columns([3, 1])
with col_title:
    st.title('🔍 SQL Murder Mystery')
    st.markdown('<span class="detective-badge">TOP SECRET</span> <span class="detective-badge">CASE #25052</span>', unsafe_allow_html=True)
with col_timer:
    elapsed_time = int(time.time() - st.session_state.start_time)
    minutes = elapsed_time // 60
    seconds = elapsed_time % 60
    st.markdown(f"<h2 style='color:#FF3B3B;'>⏱️ {minutes:02d}:{seconds:02d}</h2>", unsafe_allow_html=True)

# Investigation progress bar
investigation_progress = min(st.session_state.discovered_clues * 10, 100)
st.markdown("<p style='margin-bottom:5px'><b>Investigation Progress:</b></p>", unsafe_allow_html=True)
st.progress(investigation_progress/100)
st.markdown('</div>', unsafe_allow_html=True)

# Main content divided into sections but all on one page
main_col1, main_col2 = st.columns([2, 1])

with main_col1:
    # Case Brief Section
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.subheader("🗂️ Case Brief: Downtown Hotel Homicide")
    
    st.markdown("""
    ## The Crime
    On May 1, 2025, businessman **John Smith** was found dead in Room 302 of the Downtown Hotel with blunt force trauma to the head. 
    Detective James Green is investigating the case, and you are assisting as a database analyst.

    ## Your Task
    Use SQL queries to investigate the database and find the murderer. The database contains information about:
    - People (suspects, witnesses, the victim)
    - The crime scene and evidence
    - Interviews with witnesses and suspects
    - Alibis provided
    - Relationships between individuals
    - Phone call records
    """)
    
    # Database table information
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    st.markdown("## Available Database Tables")
    
    table_col1, table_col2 = st.columns(2)
    
    with table_col1:
        st.markdown("""
        - **Person**: Information about all individuals
        - **Crime**: Details about the crime
        - **Evidence**: Physical evidence found
        - **Interviews**: Witness statements
        """)
    
    with table_col2:
        st.markdown("""
        - **Alibis**: Claimed alibis of suspects
        - **Relationships**: Connections between people
        - **PhoneRecords**: Call logs
        """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.info("**Tip**: Start by examining the crime scene and then explore connections between the suspects and the victim.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Investigation Terminal
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.subheader("🔎 Investigation Terminal")
    
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    st.write("Select a query to get started or write your own SQL query:")
    
    # Create a 4x2 grid of buttons (8 buttons total)
    button_rows = 2
    cols_per_row = 4
    
    query_buttons = [
        {"label": "📋 All tables", "query": "SELECT name FROM sqlite_master WHERE type='table';", "help": "Shows all tables in the database"},
        {"label": "🕵️ Crime details", "query": "SELECT * FROM Crime;", "help": "Shows details about the crime"},
        {"label": "🧪 Evidence", "query": "SELECT * FROM Evidence;", "help": "Shows all evidence collected"},
        {"label": "👥 Persons", "query": "SELECT * FROM Person;", "help": "Shows information about all persons"},
        {"label": "⏱️ Alibis", "query": "SELECT p.Name, a.* FROM Alibis a JOIN Person p ON a.PersonID = p.PersonID;", "help": "Shows alibis for all suspects"},
        {"label": "🔄 Relationships", "query": "SELECT * FROM Relationships;", "help": "Shows relationships between people"},
        {"label": "📱 Phone Records", "query": "SELECT * FROM PhoneRecords;", "help": "Shows phone call records"},
        {"label": "🎤 Interviews", "query": "SELECT * FROM Interviews;", "help": "Shows interview statements"}
    ]
    
    for row in range(button_rows):
        cols = st.columns(cols_per_row)
        for col in range(cols_per_row):
            button_index = row * cols_per_row + col
            if button_index < len(query_buttons):
                button = query_buttons[button_index]
                if cols[col].button(button["label"], help=button["help"]):
                    st.session_state.current_query = button["query"]
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Advanced query examples in expander
    with st.expander("📚 Advanced Query Examples"):
        st.code("""
-- View all tables in the database
SELECT name FROM sqlite_master WHERE type='table';

-- Get details about the crime
SELECT * FROM Crime;

-- Find all evidence
SELECT * FROM Evidence;

-- Get information about all persons
SELECT * FROM Person;

-- Check alibis of suspects
SELECT p.Name, a.* 
FROM Alibis a
JOIN Person p ON a.PersonID = p.PersonID;

-- Find relationships for a specific person
SELECT r.*, p1.Name as Person1Name, p2.Name as Person2Name
FROM Relationships r
JOIN Person p1 ON r.Person1ID = p1.PersonID
JOIN Person p2 ON r.Person2ID = p2.PersonID
WHERE p1.PersonID = 1 OR p2.PersonID = 1;

-- Check people who called each other on the day of the murder
SELECT pr.*, p1.Name as Caller, p2.Name as Receiver
FROM PhoneRecords pr
JOIN Person p1 ON pr.CallerID = p1.PersonID
JOIN Person p2 ON pr.ReceiverID = p2.PersonID
WHERE CallDate = '2025-05-01';
        """)
    
    # SQL query input
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    query = st.text_area('Enter your SQL query here:', value=st.session_state.current_query, height=100)
    
    if st.button('🔍 Execute Query', type="primary"):
        if not query.strip():
            st.error('Please enter a query.')
        elif not query.strip().lower().startswith('select'):
            st.error('Only SELECT queries are allowed for security reasons.')
        else:
            try:
                with st.spinner('Executing query...'):
                    response = requests.post(f'{API_URL}/api/execute-query', json={'query': query})
                
                data = response.json()
                if 'error' in data:
                    st.error(f"Error: {data['error']}")
                else:
                    results = data.get('results', [])
                    if results:
                        # Increment discovered clues when new query succeeds
                        st.session_state.discovered_clues += 1
                        
                        df = pd.DataFrame(results)
                        st.dataframe(df, use_container_width=True)
                        
                        # Show a success banner with a timestamp
                        current_time = datetime.now().strftime("%H:%M:%S")
                        st.success(f"✅ Query executed successfully at {current_time}")
                    else:
                        st.info('Query executed successfully but returned no results.')
            except Exception as e:
                st.error(f'Failed to execute query: {e}')
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with main_col2:
    # Detective's Notes and solution submission
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.subheader("📔 Detective's Notebook")
    
    # Case notes
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    st.markdown("### Your Case Notes")
    case_notes = st.text_area("Document your findings and theories here:", height=200, value=st.session_state.case_notes)
    
    if case_notes != st.session_state.case_notes:
        st.session_state.case_notes = case_notes
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Solution submission
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    st.markdown("### Submit Your Solution")
    st.write("Once you're confident you know who the murderer is, submit their ID:")
    
    murderer_id = st.text_input('Enter the PersonID of the murderer:')
    
    if st.button('🔍 Solve the Case', type="primary"):
        if not murderer_id.strip():
            st.error('Please enter a PersonID.')
        elif not murderer_id.strip().isdigit():
            st.error('Please enter a valid numeric PersonID.')
        else:
            try:
                response = requests.post(f'{API_URL}/api/check-solution', json={'murdererId': int(murderer_id)})
                data = response.json()
                
                if data.get('correct'):
                    st.session_state.game_over = True
                    st.session_state.win = True
                else:
                    st.session_state.wrong_guesses += 1
                    st.warning(data.get('message'))
                    st.warning(random.choice(game_over_messages))
            except Exception as e:
                st.error(f'Failed to check solution: {e}')
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Evidence card section
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    st.markdown("### Key Evidence Collected")
    
    evidence_count = min(st.session_state.discovered_clues, 5)
    if evidence_count > 0:
        evidence_items = [
            "Fingerprints on the murder weapon",
            "Suspicious phone call at 10:23 PM",
            "Hotel room keycard access log",
            "Security camera footage from lobby",
            "Witness statement with timeline discrepancy"
        ]
        
        for i in range(evidence_count):
            st.markdown(f'<div class="evidence-card"><b>Evidence #{i+1}:</b> {evidence_items[i]}</div>', unsafe_allow_html=True)
    else:
        st.info("No evidence collected yet. Start executing queries to gather evidence.")
    
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Victory screen that appears when game is won
if st.session_state.get('game_over') and st.session_state.get('win'):
    st.markdown('<div class="win-container">', unsafe_allow_html=True)
    st.markdown("""
    # 🎉 CASE SOLVED! 🎉
    
    ## Congratulations, Detective!
    
    You've successfully solved the Downtown Hotel Murder case!
    
    The murderer has been arrested and justice has been served.
    Your brilliant deductive skills and SQL mastery have earned you 
    a promotion to Chief Detective!
    
    ### 🏆 DETECTIVE OF THE YEAR 🏆
    """)
    
    # Calculate final score based on time and number of queries
    elapsed_time = int(time.time() - st.session_state.start_time)
    minutes = elapsed_time // 60
    seconds = elapsed_time % 60
    
    st.markdown(f"""
    **Final Stats:**
    - Time to solve: {minutes} minutes and {seconds} seconds
    - Queries executed: {st.session_state.discovered_clues}
    - Wrong guesses: {st.session_state.wrong_guesses}
    """)
    
    # Add celebratory effects
    st.balloons()
    
    if st.button("🏆 Claim Your Badge", type="primary"):
        st.snow()
        st.markdown("""
        ## 🕵️‍♂️ MASTER DETECTIVE CERTIFICATE 🕵️‍♀️
        This certifies that you have demonstrated exceptional 
        detective skills and database investigation prowess.
        
        The Police Department thanks you for your service!
        """)
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #888;">
    <p>SQL Murder Mystery Game | Created by Detective Agency</p>
</div>
""", unsafe_allow_html=True)
