#Bonus Music : https://www.youtube.com/watch?v=qV6Wc_f1Cgo


import streamlit as st

st.header("Dealing with uncertainty")

if 'is_expanded' not in st.session_state:
    st.session_state['is_expanded'] = True

with st.expander('Exercice', expanded=st.session_state['is_expanded']):
	st.markdown("You are the CEO of a company which is about to launch a new product.\n"
		"You need to take the decision concerning the size of the plant to build.\n\n"
		"Market research shows that the demand for the new product can varry between 50k unit/year to 150k unit/year with an average of 100k unit/year.\n\n"
		"If you choose to build a plant with a capacity of 100k units, what would be the average margin you will get each year (knowing that the product unit margin is equal to 10 euros).\n"
		)

	status = st.empty()
	st.radio('Select one answer:', ["1 Million euros", "Higher than 1 Million euros", "Lower than 1 Million euros"])


	submitted = st.button('Submit your answers')
	skip = st.button('Skip the exercice')
	if skip or submitted:
		#st.video("https://youtu.be/PY4jgiV5EzA", format="video/mp4", start_time=0)
		st.success("Thank you for your answer. You can know watch the following video on Udemy to know if you answered correctly")

