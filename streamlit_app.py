import streamlit as st
import requests
import pandas as pd

API_URL = 'http://localhost:5000'

# Set page title and configuration
st.set_page_config(
    page_title="SQL Murder Mystery",
    page_icon="🔍",
    layout="wide"
)

# Set custom theme with light mode
st.markdown("""
<style>
    .stApp {
        background-color: #FFFFFF;
        color: #31333F;
    }
    .stButton>button {
        background-color: #FF4B4B;
        color: white;
    }
    .st-bw {
        background-color: #F0F2F6;
    }
    * {
        font-family: 'sans-serif';
    }
</style>
""", unsafe_allow_html=True)

st.title('SQL Murder Mystery Game')

# Game introduction and backstory
st.markdown("""
## The Crime
On May 1, 2025, businessman John Smith was found dead in Room 302 of the Downtown Hotel with blunt force trauma to the head. 
Detective James Green is investigating the case, and you are assisting as a database analyst.

## Your Task
Use SQL queries to investigate the database and find the murderer. The database contains information about:
- People (suspects, witnesses, the victim)
- The crime scene and evidence
- Interviews with witnesses and suspects
- Alibis provided
- Relationships between individuals
- Phone call records

## Available Tables
- Person: Contains information about all individuals
- Crime: Details about the crime being investigated
- Evidence: Physical evidence found at the crime scene
- Interviews: Statements from witnesses and suspects
- Alibis: Claimed alibis of suspects
- Relationships: Connections between different people
- PhoneRecords: Call logs relevant to the investigation

**Tip**: Start by examining the crime scene and then exploring connections between the suspects and the victim.
""")

# Create a two-column layout
col1, col2 = st.columns([3, 2])

with col1:
    st.subheader('Investigation Terminal')
    
    # Initialize query variable if not in session state
    if 'current_query' not in st.session_state:
        st.session_state.current_query = ""
    
    # Create predefined query buttons
    st.write("Quick Query Buttons:")
    
    # Create rows of buttons, 2 buttons per row
    button_col1, button_col2 = st.columns(2)
    
    # Row 1
    with button_col1:
        if st.button("📋 View all tables", help="Shows all tables in the database"):
            st.session_state.current_query = "SELECT name FROM sqlite_master WHERE type='table';"
    
    with button_col2:
        if st.button("🔎 Crime details", help="Shows details about the crime"):
            st.session_state.current_query = "SELECT * FROM Crime;"
    
    # Row 2
    button_col3, button_col4 = st.columns(2)
    
    with button_col3:
        if st.button("🧪 All evidence", help="Shows all evidence collected"):
            st.session_state.current_query = "SELECT * FROM Evidence;"
    
    with button_col4:
        if st.button("👥 All persons", help="Shows information about all persons"):
            st.session_state.current_query = "SELECT * FROM Person;"
    
    # Row 3
    button_col5, button_col6 = st.columns(2)
    
    with button_col5:
        if st.button("⏱️ Check alibis", help="Shows alibis for all suspects"):
            st.session_state.current_query = "SELECT p.Name, a.* FROM Alibis a JOIN Person p ON a.PersonID = p.PersonID;"
    
    with button_col6:
        if st.button("🔄 View relationships", help="Shows relationships between people"):
            st.session_state.current_query = "SELECT * FROM Relationships;"
            
    # Row 4
    button_col7, button_col8 = st.columns(2)
    
    with button_col7:
        if st.button("📱 Phone records", help="Shows phone call records"):
            st.session_state.current_query = "SELECT * FROM PhoneRecords;"
    
    with button_col8:
        if st.button("🎤 Interviews", help="Shows interview statements"):
            st.session_state.current_query = "SELECT * FROM Interviews;"
    
    # Example queries to help players get started
    with st.expander("Advanced Query Examples"):
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
        """)
    
    # SQL query input
    query = st.text_area('Enter your SQL query here:', value=st.session_state.current_query, height=150)
    
    if st.button('Execute Query', type="primary"):
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
                        df = pd.DataFrame(results)
                        st.dataframe(df)
                    else:
                        st.info('Query executed successfully but returned no results.')
            except Exception as e:
                st.error(f'Failed to execute query: {e}')

with col2:
    st.subheader('Case Notes')
    
    # Case notes section where players can keep track of findings
    if 'case_notes' not in st.session_state:
        st.session_state.case_notes = ""
        
    case_notes = st.text_area("Keep track of your findings here:", height=300, 
                             value=st.session_state.case_notes)
    
    if case_notes != st.session_state.case_notes:
        st.session_state.case_notes = case_notes
    
    st.markdown('---')
    
    # Solution submission
    st.subheader('Submit Your Solution')
    st.write("Once you're confident you know who the murderer is, submit their ID:")
    
    murderer_id = st.text_input('Enter the PersonID of the murderer:')
    
    if st.button('Check Solution', type="primary"):
        if not murderer_id.strip():
            st.error('Please enter a PersonID.')
        elif not murderer_id.strip().isdigit():
            st.error('Please enter a valid numeric PersonID.')
        else:
            try:
                response = requests.post(f'{API_URL}/api/check-solution', json={'murdererId': int(murderer_id)})
                data = response.json()
                
                if data.get('correct'):
                    st.balloons()
                    st.success(data.get('message'))
                else:
                    st.warning(data.get('message'))
            except Exception as e:
                st.error(f'Failed to check solution: {e}')
