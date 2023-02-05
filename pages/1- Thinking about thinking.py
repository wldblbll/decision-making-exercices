import streamlit as st

st.header("Thinking about thinking")

eureka = st.empty()
if 'is_expanded' not in st.session_state:
    st.session_state['is_expanded'] = True

with st.expander('Exercice', expanded=st.session_state['is_expanded']):
	st.markdown("Could you guess the rule empoyed to generate the following sequence of numbers: \n**2, 4, 6**")
	st.markdown("To do so, you can generate three-number sequences and test with the following button whether the sequence you generated conform to the rule.")
	status = st.empty()
	seq = st.text_input('Enter a sequence of 3 numbers separated with commas:')
	submitted = st.button('Test the sequence')
	st.markdown("Once you think you have found the rule, describe the rule you have found and click on the 'Eureka' button.")
	rule = st.text_input('Enter a description of the rule you have found:')
	eureka = st.button('Eureka !')
	skip = st.button('Skip the exercice')

	if submitted:
		try:
			list_numbers = seq.replace(";",",").replace(" ","").split(",")
			if len(list_numbers)!=3:
				status.warning("You should enter a sequence of 3 numbers separated with commas. Example : 10,12,40")
				st.stop()
			list_numbers = [int(x) for x in list_numbers]
			if (list_numbers[2]>list_numbers[1]) and (list_numbers[1]>list_numbers[0]):
				status.success(f"Yes, the sequence ({seq}) is conform to the rule.")
			else:
				status.error(f"Sorry, the sequence (f{seq}) does not conform to the rule. Try again ;)")
		except:
				status.warning("You should enter a sequence of 3 numbers separated with commas. Example : 10,12,40")
	if skip or eureka:
		st.session_state['is_expanded'] = False
		#st.video("https://youtu.be/9pDxn6hj8ZE", format="video/mp4", start_time=0)
		st.success("Thank you for your answer. You can know watch the following video on Udemy to know if you answered correctly")
