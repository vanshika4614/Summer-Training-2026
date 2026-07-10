# import streamlit as st
# st.title("Hello GeeksForGeeks !!!")
# st.header("This is a header") 
# st.subheader("This is a subheader")
# st.text("Hello GeeksForGeeks!!!")
# st.markdown("### This is a markdown")
# st.success("Success")

# st.info("Information")

# st.warning("Warning")

# st.error("Error")

# exp = ZeroDivisionError("Trying to divide by Zero")
# st.exception(exp)

# st.write("Text with write")

# # Writing python inbuilt function range()
# st.write(range(10))

# from PIL import Image  # Import Image from Pillow
# img = Image.open("D:\\STUDY_HUB\\PROJECTS\\Summer-Training-2026\\OIP.jpg") # Open the image file
# st.image(img, width=200) # Display the image with a specified width


# # Display a checkbox with the label 'Show/Hide'
# if st.checkbox("Show/Hide"):
#     # Show this text only when the checkbox is checked
#     st.text("Showing the widget")

#     # Create a radio button to select gender
# status = st.radio("Select Gender:", ['Male', 'Female'])

# # Display the selected option using success message
# if status == 'Male':
#     st.success("Male")
# else:
#     st.success("Female")

#     # Create a dropdown menu for selecting a hobby
# hobby = st.selectbox("Select a Hobby:", ['Dancing', 'Reading', 'Sports'])

# # Display the selected hobby
# st.write("Your hobby is:", hobby)

# # Create a multiselect box for choosing hobbies
# hobbies = st.multiselect("Select Your Hobbies:", ['Dancing', 'Reading', 'Sports'])

# # Display the number of selected hobbies
# st.write("You selected", len(hobbies), "hobbies")

# # A simple button that does nothing
# st.button("Click Me")

# # A button that displays text when clicked
# if st.button("About"):
#     st.text("Welcome to GeeksForGeeks!")

#     # Create a text input box with a default placeholder
# name = st.text_input("Enter your name", "Type here...")

# # Display the name after clicking the Submit button
# if st.button("Submit"):
#     result = name.title()  # Capitalize the first letter of each word
#     st.success(result)


#     # Create a slider to select a level between 1 and 5
# level = st.slider("Choose a level", min_value=1, max_value=5)

# # Display the selected level
# st.write(f"Selected level: {level}")

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("📊 Simple Bar Graph Generator")

# Upload CSV
file = st.file_uploader("Upload CSV File", type=["csv"])

if file is not None:

    # Read CSV
    df = pd.read_csv(file)

    # Show data
    st.subheader("Dataset")
    st.dataframe(df)

    # Select column
    column = st.selectbox("Select a Column", df.columns)

    # Count values
    counts = df[column].value_counts()

    # Show table
    st.subheader("Value Counts")
    st.write(counts)

    # Create graph
    fig, ax = plt.subplots()

    ax.bar(counts.index.astype(str), counts.values)

    ax.set_title("Bar Graph")
    ax.set_xlabel(column)
    ax.set_ylabel("Count")

    plt.xticks(rotation=45)

    st.pyplot(fig)

else:
    st.info("Please upload a CSV file.")