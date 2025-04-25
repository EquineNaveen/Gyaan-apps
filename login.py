import streamlit as st
from ldap3 import Server, Connection, ALL, NTLM, SIMPLE, ALL_ATTRIBUTES, SUBTREE, core

def ldap_authenticate(username: str, password: str):
    # server_uri = "ldap://10.21.6.164:389"
    # base_dn = "dc=dos"
    # user_dn = f"mailacceptinggeneralid={username},{base_dn}"
    # try:
    #     server = Server(server_uri, get_info=ALL)
    #     conn = Connection(server, user=user_dn, password=password, authentication=SIMPLE, auto_bind=True)
    #     conn.unbind()
    return True
    # except core.exceptions.LDAPBindError:
    #     return False
    # except Exception as error:
    #     st.error(f"LDAP error: {error}")
    #     return False

def login():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_btn = st.button("Login")

    if login_btn:
        if ldap_authenticate(username, password):
            st.session_state['user'] = username
            st.session_state['role'] = "USER"
            st.success("Login successful!")
            # Redirect to apps.py after successful login
            st.switch_page("pages/apps.py")
        else:
            st.error("Invalid credentials.")

if 'user' in st.session_state:
    # Redirect to apps.py if already logged in
    st.switch_page("pages/apps.py")
    st.stop()
else:
    login()