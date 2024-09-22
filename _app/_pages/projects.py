import streamlit as st
from _app.data import apps


@st.cache_data
def generate_app_cards():
    print('generate_app_cards'.upper())
    # Define fixed dimensions for the cards and images using percentages
    card_height = '30vh'  # Use viewport height for responsive design
    card_width = '100%'   # Full width of the column
    image_height = '90%'  # Relative to the card height
    image_width = '90%'   # Relative to the card width

    cards = []
    for app in apps:
        card_html = f"""
        <div style="
            display: flex; 
            flex-direction: column; 
            justify-content: space-between; 
            align-items: center; 
            background-color: grey; 
            padding: 20px; 
            border-radius: 10px; 
            box-shadow: 0 0 10px rgba(0,0,0,0.5); 
            height: {card_height}; /* Responsive height */
            width: {card_width}; /* Full width of the column */
            box-sizing: border-box; 
            margin-bottom: 20px;
        ">
            <a href="{app.links[0]}" target="_blank" style="text-decoration: none; width: 100%; height: {image_height}; display: flex; justify-content: center; align-items: center;">
                <img src="{app.image}" alt="{app.name}" style="width: {image_width}; height: {image_height}; object-fit: cover; border-radius: 10px;"/>
            </a>
            <div style="font-family: serif; color: black; font-size: x-large; font-weight: bold; text-align: center; margin-top: 10px;">
                {app.name}
            </div>
        </div>
        <br>
        """
        cards.append(card_html)
    return cards


@st.cache_data
def create_projects_page():
    app_cards = generate_app_cards()
    cols = st.columns(4)

    for i in range(0, len(app_cards)):
        with cols[i % len(cols)]:
            st.markdown(app_cards[i], unsafe_allow_html=True)


# @st.cache_data
# def create_apps_page():
#     # Generate app cards
#     app_cards = generate_app_cards()

#     # Display the cards in a Streamlit app
#     for i in range(0, len(app_cards), 4):
#         cols = st.columns(4)  # Create four columns

#         for idx, col in enumerate(cols):
#             if i + idx < len(app_cards):
#                 with col:
#                     st.markdown(app_cards[i + idx], unsafe_allow_html=True)

# quality-insight-dashboard
