import streamlit as st
from test4_1_fin import talk_to_bot

st.title("AquaTwin")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("ask something...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Simple bot response logic
    # bot_response = "Line 1<br>Line 2<br>Line 3"
    # bot_response += "Line 1  \nLine 2  \nLine 3"
    temp_dict = talk_to_bot(user_input)
    to_print = ""
    for elem in temp_dict:
        to_print += f":blue-background[{'**' + elem.upper() + '**'}]"
        to_print += ":"
        to_print += f"  \n{temp_dict[elem]}"
        to_print += "  \n"
        to_print += "  \n"

    bot_response = to_print

    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.markdown(bot_response)
