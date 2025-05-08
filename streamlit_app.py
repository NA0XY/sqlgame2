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
    
    # Example queries to help players get started
    with st.expander("Example Queries"):
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
        """)
    
    # SQL query input
    query = st.text_area('Enter your SQL query here:', height=150)
    
    if st.button('Execute Query'):
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
    case_notes = st.text_area("Keep track of your findings here:", height=300, 
                             value=st.session_state.get('case_notes', ''))
    
    if case_notes != st.session_state.get('case_notes', ''):
        st.session_state['case_notes'] = case_notes
    
    st.markdown('---')
    
    # Solution submission
    st.subheader('Submit Your Solution')
    st.write("Once you're confident you know who the murderer is, submit their ID:")
    
    murderer_id = st.text_input('Enter the PersonID of the murderer:')
    
    if st.button('Check Solution'):
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
