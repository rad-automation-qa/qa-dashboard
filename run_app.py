from streamlit.web import cli

# This import path depends on your Streamlit version
if __name__ == '__main__':
    cli._main_run_clExplicit('app.py', is_hello=False,
                             args=['streamlit', 'run'])
