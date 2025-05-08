import streamlit as st
import requests
import pandas as pd

API_URL = 'http://localhost:5000'

st.title('SQL Murder Mystery Game')

st.markdown("""
Welcome to the SQL Murder Mystery game! Use your SQL skills to investigate the crime and find the murderer.

Enter your SQL SELECT queries below to explore the database.
""")

query = st.text_area('Enter your SQL query here:', height=150)

if st.button('Execute Query'):
    if not query.strip().lower().startswith('select'):
        st.error('Only SELECT queries are allowed.')
    else:
        try:
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

st.markdown('---')

st.subheader('Submit Your Solution')
murderer_id = st.text_input('Enter the PersonID of the murderer:')

if st.button('Check Solution'):
    if not murderer_id.isdigit():
        st.error('Please enter a valid numeric PersonID.')
    else:
        try:
            response = requests.post(f'{API_URL}/api/check-solution', json={'murdererId': int(murderer_id)})
            data = response.json()
            if data.get('correct'):
                st.success(data.get('message'))
            else:
                st.warning(data.get('message'))
        except Exception as e:
            st.error(f'Failed to check solution: {e}')
