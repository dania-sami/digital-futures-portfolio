import streamlit as st

st.set_page_config(page_title="AI Research Assistant", layout="wide")

st.title("AI Research Assistant")
st.write("Analyze research text with summaries, keywords, and structured insights.")

text_input = st.text_area("Paste research paper text here", height=200)

def generate_summary(text):
    return f"This paper discusses {text[:80]}... focusing on key patterns, systems, and insights."

def extract_keywords(text):
    words = text.split()
    return list(set(words[:10]))

def extract_sections(text):
    return {
        "Problem": "Addresses challenges related to data and systems.",
        "Method": "Applies analytical and computational techniques.",
        "Results": "Shows improvements in efficiency and scalability.",
        "Applications": "Can be applied in real-world systems and digital platforms."
    }

if st.button("Analyze"):
    if text_input:
        st.subheader("Summary")
        st.write(generate_summary(text_input))

        st.subheader("Key Insights")
        st.write("- Focus on scalability and system design")
        st.write("- Emphasis on efficiency and automation")
        st.write("- Relevant for real-world applications")

        st.subheader("Keywords")
        st.write(extract_keywords(text_input))

        st.subheader("Structured Analysis")
        sections = extract_sections(text_input)
        for k, v in sections.items():
            st.write(f"**{k}:** {v}")
    else:
        st.warning("Please enter some text.")
