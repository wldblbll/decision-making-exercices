#Bonus Music : https://www.youtube.com/watch?v=qV6Wc_f1Cgo


import streamlit as st
from PIL import Image
import numpy as np
import os

st.header("Algorithms for better decisions")

nb_total_images = 10
path = os.path.dirname(__file__)
list_images_path = [path+"/images/planet_ (%d).png" % (x+1) for x in range(nb_total_images)]
list_images = [Image.open(x) for x in list_images_path]

def _update_slider(value):
	st.session_state["image_index"] += 1
	st.session_state.list_answers.append(answer)
	st.session_state["default_answer"] = 50 # reset slider

if "default_answer" not in st.session_state:
    st.session_state["default_answer"] = 50

if 'image_index' not in st.session_state:
	st.session_state["image_index"] = 0
	image_index = 0
else:
	image_index = st.session_state["image_index"]

if 'list_answers' not in st.session_state:
	st.session_state["list_answers"] = []

with st.expander('Exercice', expanded=True):
	if image_index==nb_total_images:
		same_images_index = [0, 3, 6, 9]
		answers = [st.session_state.list_answers[x] for x in same_images_index]
		variance = np.array(answers).max()-np.array(answers).min()
		st.success("Congratulation for completing the exercice.\n"
			"Let's see now the results.\n\n"
			"This exercice was designed to measure noise in our judgment.\n"
			"The images #1, #4, #7 and #10 were all the same. We just rotate the image each time.\n"
			)
		cols = st.columns(4)
		for col_index in range(4):
			image_index = same_images_index[col_index]
			cols[col_index].image(list_images[image_index], 
				caption="Your answer for image #%d was %d%%" % (image_index+1, answers[col_index]), width=100)

		#st.write(st.session_state.list_answers)
		st.warning("The maximum variance in your answers for the same image is equal to %d%%" % variance)
		#st.video("https://youtu.be/f0bRcd7NA6U", format="video/mp4", start_time=0)

	else:
		col1, col2 = st.columns(2)
		col1.markdown("You will be presented 10 images of a planet and you should estimate each time the pourcentage of its surface which is covered by the ocean.\n"
			"For example, the right answer for following image would be something close to 50%.\n"
			)
		image_50_50 = Image.open(path+'/images/50-50.png')
		col2.image(image_50_50, caption="Example", width=100)

		st.markdown('Use the slider to pick the pourcentage that seems correct to you then click the "Next" button to validate your answer and see the following question\n\n'
			'After you finish answering the 10 questions you will be directed to the course explaining how is this exercice corelated to the quality of your decisions')

		st.subheader("Question %d / %d" % (image_index+1, nb_total_images))
		
		col1, col2 = st.columns(2)
		col2.image(list_images[image_index], caption="Image %d / %d" % (image_index+1, nb_total_images), width=200)
		#status = st.empty()
		answer = col1.slider("Use the slider to pick the right pourcentage of surface covered by ocean:", 
			key="default_answer", min_value=0, max_value=100, step=1)

		next_btn = col1.button("Next question", on_click=_update_slider, kwargs={"value": answer})

	#st.write(st.session_state.list_answers)
	#if submitted:
	#	st.video("https://www.youtube.com/watch?v=z-LLQrzGkWI", format="video/mp4", start_time=0)
