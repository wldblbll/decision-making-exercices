#Bonus Music : https://www.youtube.com/watch?v=qV6Wc_f1Cgo


import streamlit as st

st.header("How to update your beliefs ?")

if 'is_expanded' not in st.session_state:
    st.session_state['is_expanded'] = True

with st.expander('Exercice', expanded=st.session_state['is_expanded']):
	st.markdown("- 1% of women at age forty who participate have breast cancer.\n"
		"- 80% of women with breast cancer will get positive mammograms.\n"
		"- 9.6% of women without breast cancer will get positive mammograms.\n\n"
		"Suppose you randomly select a woman from that population.")

	status = st.empty()
	st.number_input('What is the probabibility that she have cancer ? (enter a number between 0 and 1)', min_value=0., max_value=1., step=0.1)


	st.number_input('The selected woman have passed a mammograms test and the result is positive. What is now the probability that she have cancer ?', 0., 1., 0.1)

	submitted = st.button('Submit your answers and see the solution')
	skip = st.button('Skip the exercice')

	if skip or submitted:
		#st.video("https://youtu.be/5-TXgClgkUA", format="video/mp4", start_time=0)
		st.success("Thank you for your answer. You can know watch the following video on Udemy to know if you answered correctly")

